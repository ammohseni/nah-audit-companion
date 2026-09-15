#!/usr/bin/env python3
"""Generate a complete, color-coded SVG network of manuscript claims.

The script reads the authoritative claim ledger and the explicit relationship
register. It includes every claim, including claims with no registered edge.
It does not infer mathematical dependencies.
"""

from __future__ import annotations

import argparse
import json
import re
import textwrap
from dataclasses import dataclass
from pathlib import Path
from xml.sax.saxutils import escape


TYPE_STYLE = {
    "THEOREM CONSEQUENCE": ("#dbeafe", "#1d4ed8"),
    "MODEL CALCULATION": ("#dcfce7", "#15803d"),
    "MODEL ASSUMPTION": ("#ffedd5", "#c2410c"),
    "STANDARD BACKGROUND": ("#f3f4f6", "#4b5563"),
    "PHYSICAL PROPOSAL": ("#ede9fe", "#7c3aed"),
    "PHYSICAL ANSATZ": ("#fce7f3", "#be185d"),
}

VALID_EVIDENCE = {"MANUSCRIPT-EXPLICIT", "AUTHOR-CONFIRMED", "AI-PROPOSED"}


@dataclass(frozen=True)
class Claim:
    claim_id: str
    normalized: str
    claim_type: str
    status: str
    last_audit: str
    audited_source: str


@dataclass(frozen=True)
class Relation:
    source: str
    label: str
    target: str
    evidence: str
    explanation: str


def clean_cell(value: str) -> str:
    return value.strip().strip("`").strip()


def table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def parse_claims(path: Path) -> dict[str, Claim]:
    claims: dict[str, Claim] = {}
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not re.match(r"^\|\s*`?NAH-C\d{3,}`?\s*\|", line):
            continue
        cells = table_cells(line)
        if len(cells) < 10:
            raise ValueError(f"Malformed claim-ledger row: {line}")
        claim_id = clean_cell(cells[0])
        claim_type = clean_cell(cells[3])
        if claim_type not in TYPE_STYLE:
            raise ValueError(f"Unknown claim type for {claim_id}: {claim_type}")
        if claim_id in claims:
            raise ValueError(f"Duplicate claim ID: {claim_id}")
        claims[claim_id] = Claim(
            claim_id=claim_id,
            normalized=clean_cell(cells[2]).replace("`", ""),
            claim_type=claim_type,
            status=clean_cell(cells[7]),
            last_audit=clean_cell(cells[8]),
            audited_source=clean_cell(cells[9]),
        )
    if not claims:
        raise ValueError("No claims found in CLAIM_LEDGER.md")
    return claims


def parse_relationships(
    path: Path,
) -> tuple[dict[str, tuple[str, int]], list[Relation]]:
    groups: dict[str, tuple[str, int]] = {}
    relations: list[Relation] = []
    seen_relations: set[tuple[str, str, str]] = set()
    section = ""
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("## Claim groups"):
            section = "groups"
            continue
        if line.startswith("## Registered relations"):
            section = "relations"
            continue
        if line.startswith("## "):
            section = ""
            continue
        if not line.startswith("|") or re.match(r"^\|\s*---", line):
            continue
        cells = table_cells(line)
        if section == "groups" and re.fullmatch(r"`?NAH-C\d{3,}`?", cells[0]):
            claim_id = clean_cell(cells[0])
            if claim_id in groups:
                raise ValueError(f"Duplicate group assignment: {claim_id}")
            group_name = clean_cell(cells[1])
            if not group_name:
                raise ValueError(f"Empty group name for {claim_id}")
            groups[claim_id] = (group_name, int(clean_cell(cells[2])))
        elif section == "relations" and re.fullmatch(
            r"`?NAH-C\d{3,}`?", cells[0]
        ):
            if len(cells) < 5:
                raise ValueError(f"Malformed relationship row: {line}")
            evidence = clean_cell(cells[3])
            if evidence not in VALID_EVIDENCE:
                raise ValueError(f"Unknown relationship evidence: {evidence}")
            source = clean_cell(cells[0])
            label = clean_cell(cells[1])
            target = clean_cell(cells[2])
            if source == target:
                raise ValueError(f"Self-relationship is not allowed: {source}")
            relation_key = (source, label, target)
            if relation_key in seen_relations:
                raise ValueError(
                    f"Duplicate relationship: {source} --{label}--> {target}"
                )
            seen_relations.add(relation_key)
            relations.append(
                Relation(
                    source=source,
                    label=label,
                    target=target,
                    evidence=evidence,
                    explanation=clean_cell(cells[4]),
                )
            )
    return groups, relations


def claim_number(claim_id: str) -> int:
    return int(claim_id.rsplit("C", 1)[1])


def dependency_order(claims: list[Claim], relations: list[Relation]) -> list[Claim]:
    """Return a stable source-before-target order for one visual group.

    Only relationships whose endpoints both belong to the group affect the
    order.  If the registered relationships contain a cycle, the remaining
    claims fall back to claim-number order instead of making map generation
    fail.
    """

    by_id = {claim.claim_id: claim for claim in claims}
    remaining = set(by_id)
    incoming = {claim_id: set() for claim_id in by_id}
    for relation in relations:
        if relation.source in by_id and relation.target in by_id:
            incoming[relation.target].add(relation.source)

    ordered: list[Claim] = []
    while remaining:
        ready = sorted(
            (
                claim_id
                for claim_id in remaining
                if not (incoming[claim_id] & remaining)
            ),
            key=claim_number,
        )
        if not ready:
            ready = sorted(remaining, key=claim_number)
        for claim_id in ready:
            ordered.append(by_id[claim_id])
            remaining.remove(claim_id)
    return ordered


def wrapped_claim(text: str, width: int = 47, maximum: int = 3) -> list[str]:
    text = re.sub(r"\s+", " ", text).strip()
    lines = textwrap.wrap(text, width=width, break_long_words=False)
    if len(lines) > maximum:
        lines = lines[:maximum]
        lines[-1] = lines[-1].rstrip(" .") + "..."
    return lines


def render_svg(
    claims: dict[str, Claim],
    groups: dict[str, tuple[str, int]],
    relations: list[Relation],
) -> str:
    unknown_groups = sorted(set(groups) - set(claims))
    ungrouped = sorted(set(claims) - set(groups))
    unknown_edges = sorted(
        {
            claim_id
            for relation in relations
            for claim_id in (relation.source, relation.target)
            if claim_id not in claims
        }
    )
    if unknown_groups:
        raise ValueError("Unknown claims in group table: " + ", ".join(unknown_groups))
    if ungrouped:
        raise ValueError("Claims missing from group table: " + ", ".join(ungrouped))
    if unknown_edges:
        raise ValueError("Unknown claims in relationships: " + ", ".join(unknown_edges))

    grouped: dict[tuple[int, str], list[Claim]] = {}
    for claim_id, claim in claims.items():
        group_name, group_order = groups[claim_id]
        grouped.setdefault((group_order, group_name), []).append(claim)
    ordered_groups = sorted(grouped)
    for key in ordered_groups:
        grouped[key] = dependency_order(grouped[key], relations)

    max_columns = 3
    node_w = 390
    audit_lines = {
        claim_id: [
            line
            for label, value in (
                ("Last audit", claim.last_audit),
                ("Audited source", claim.audited_source),
            )
            for line in textwrap.wrap(
                f"{label}: {value or 'not recorded'}",
                width=52,
                break_long_words=True,
                break_on_hyphens=False,
            )
        ]
        for claim_id, claim in claims.items()
    }
    node_h = 132 + 16 * max(len(lines) for lines in audit_lines.values())
    node_gap = 58
    column_gap = 160
    # The generous outer margin gives long within-group relations a clean
    # routing gutter outside the columns instead of mixing them with
    # cross-group arrows.
    margin_x = 180
    header_h = 102
    group_title_h = 44
    row_gap = 78
    footer_h = 118

    group_rows: list[list[tuple[int, str]]] = [
        ordered_groups[index : index + max_columns]
        for index in range(0, len(ordered_groups), max_columns)
    ]
    row_heights = [
        group_title_h
        + max(len(grouped[key]) for key in row) * (node_h + node_gap)
        - node_gap
        for row in group_rows
    ]
    columns = min(max_columns, max(1, len(ordered_groups)))
    canvas_w = margin_x * 2 + columns * node_w + (columns - 1) * column_gap
    canvas_h = header_h + sum(row_heights) + row_gap * (len(group_rows) - 1) + footer_h

    positions: dict[str, tuple[float, float]] = {}
    group_titles: list[tuple[str, float, float]] = []
    current_y = header_h
    for row_index, row in enumerate(group_rows):
        for column_index, key in enumerate(row):
            x = margin_x + column_index * (node_w + column_gap)
            group_titles.append((key[1], x + node_w / 2, current_y))
            for claim_index, claim in enumerate(grouped[key]):
                y = current_y + group_title_h + claim_index * (node_h + node_gap)
                positions[claim.claim_id] = (x, y)
        current_y += row_heights[row_index] + row_gap

    parts: list[str] = []
    parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas_w}" '
        f'height="{canvas_h}" viewBox="0 0 {canvas_w} {canvas_h}" '
        'role="img" aria-labelledby="network-title network-desc">'
    )
    parts.append('<title id="network-title">Complete NAH manuscript claim network</title>')
    parts.append(
        '<desc id="network-desc">Every registered manuscript claim, colored by '
        'claim type, with explicitly registered claim-to-claim relationships.</desc>'
    )
    metadata = json.dumps(
        {
            "claim_count": len(claims),
            "relation_count": len(relations),
        },
        sort_keys=True,
    )
    parts.append(f"<metadata>{escape(metadata)}</metadata>")
    parts.append(
        """<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5"
          markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 z" fill="#64748b"/>
  </marker>
</defs>"""
    )
    parts.append('<rect width="100%" height="100%" fill="#ffffff"/>')
    parts.append(
        f'<text x="{margin_x}" y="42" font-family="system-ui, sans-serif" '
        'font-size="26" font-weight="600" fill="#111827">Complete claim network</text>'
    )
    parts.append(
        f'<text x="{margin_x}" y="70" font-family="system-ui, sans-serif" '
        f'font-size="15" fill="#475569">All {len(claims)} registered claims and '
        f'{len(relations)} registered relations are shown; color encodes claim type.</text>'
    )

    for title, x, y in group_titles:
        parts.append(
            f'<text x="{x}" y="{y + 25}" text-anchor="middle" '
            'font-family="system-ui, sans-serif" font-size="18" font-weight="600" '
            f'fill="#111827">{escape(title)}</text>'
        )

    # Choose an attachment side for every edge before assigning ports.  This
    # prevents multiple arrows from sharing one central anchor and makes long
    # same-column relations travel through separate lanes beside the nodes.
    edge_routes: list[tuple[str, str, int | None]] = []
    lane_count: dict[tuple[float, str], int] = {}
    side_edges: dict[tuple[str, str], list[int]] = {}
    column_x_values = sorted({x for x, _ in positions.values()})
    for edge_index, relation in enumerate(relations):
        sx, sy = positions[relation.source]
        tx, ty = positions[relation.target]
        dx = tx - sx
        dy = ty - sy
        if abs(dx) > 80:
            if dx > 0:
                source_side, target_side = "right", "left"
            else:
                source_side, target_side = "left", "right"
            lane = None
        else:
            row_step = node_h + node_gap
            is_long = abs(dy) > row_step + 1
            if is_long:
                # Route long relations outside the outer columns.  This keeps
                # the gutters between groups available for cross-group edges.
                lane_side = "left" if sx == column_x_values[0] else "right"
                source_side = target_side = lane_side
                lane_key = (sx, lane_side)
                lane = lane_count.get(lane_key, 0)
                lane_count[lane_key] = lane + 1
            else:
                if dy >= 0:
                    source_side, target_side = "bottom", "top"
                else:
                    source_side, target_side = "top", "bottom"
                lane = None
        edge_routes.append((source_side, target_side, lane))
        side_edges.setdefault((relation.source, source_side), []).append(edge_index)
        side_edges.setdefault((relation.target, target_side), []).append(edge_index)

    def port(claim_id: str, side: str, edge_index: int) -> tuple[float, float]:
        """Return a distinct, deterministic attachment point on a node side."""

        x, y = positions[claim_id]
        users = side_edges[(claim_id, side)]
        slot = users.index(edge_index)
        count = len(users)
        if side in {"top", "bottom"}:
            spacing = min(58.0, node_w * 0.54 / max(1, count))
            offset = (slot - (count - 1) / 2) * spacing
            return x + node_w / 2 + offset, y if side == "top" else y + node_h
        spacing = min(30.0, node_h * 0.46 / max(1, count))
        offset = (slot - (count - 1) / 2) * spacing
        return x if side == "left" else x + node_w, y + node_h / 2 + offset

    edge_labels: list[tuple[str, float, float]] = []
    for edge_index, relation in enumerate(relations):
        sx, sy = positions[relation.source]
        tx, ty = positions[relation.target]
        source_side, target_side, lane = edge_routes[edge_index]
        x1, y1 = port(relation.source, source_side, edge_index)
        x2, y2 = port(relation.target, target_side, edge_index)
        if source_side != target_side and source_side in {"left", "right"}:
            mid = (x1 + x2) / 2
            path = f"M {x1} {y1} C {mid} {y1}, {mid} {y2}, {x2} {y2}"
            label_x, label_y = mid, (y1 + y2) / 2 - 9
        elif source_side in {"left", "right"}:
            direction = 1 if source_side == "right" else -1
            lane_x = (
                (sx + node_w if direction > 0 else sx)
                + direction * (30 + 28 * int(lane or 0))
            )
            turn = 13 * direction
            path = (
                f"M {x1} {y1} "
                f"C {x1 + turn} {y1}, {lane_x - turn} {y1}, {lane_x} {y1} "
                f"L {lane_x} {y2} "
                f"C {lane_x - turn} {y2}, {x2 + turn} {y2}, {x2} {y2}"
            )
            label_x, label_y = lane_x, (y1 + y2) / 2
        else:
            distance = y2 - y1
            path = (
                f"M {x1} {y1} "
                f"C {x1} {y1 + distance * 0.42}, "
                f"{x2} {y2 - distance * 0.42}, {x2} {y2}"
            )
            label_x, label_y = (x1 + x2) / 2 + 78, (y1 + y2) / 2 + 4
        dash = ' stroke-dasharray="8 6"' if relation.evidence == "AI-PROPOSED" else ""
        parts.append(
            f'<path d="{path}" fill="none" stroke="#64748b" stroke-width="2.2"'
            ' stroke-linecap="round" stroke-linejoin="round"'
            f'{dash} marker-end="url(#arrow)"><title>{escape(relation.evidence)}: '
            f'{escape(relation.explanation)}</title></path>'
        )
        label = relation.label.lower()
        if len(label) > 31:
            label = label[:28].rstrip() + "..."
        edge_labels.append((label, label_x, label_y))

    for claim_id in sorted(claims, key=claim_number):
        claim = claims[claim_id]
        x, y = positions[claim_id]
        fill, stroke = TYPE_STYLE[claim.claim_type]
        stroke_width = 2
        stroke_dash = ""
        if claim.status == "MUST CORRECT":
            stroke = "#b91c1c"
            stroke_width = 5
        elif claim.status == "SHOULD CLARIFY":
            stroke = "#b45309"
            stroke_width = 4
            stroke_dash = ' stroke-dasharray="9 6"'
        elif claim.status == "OUTSIDE NAH SCOPE":
            stroke_dash = ' stroke-dasharray="6 5"'
        parts.append(
            f'<g id="{claim_id}"><title>{escape(claim.normalized)}</title>'
            f'<rect x="{x}" y="{y}" width="{node_w}" height="{node_h}" rx="15" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"{stroke_dash}/>'
        )
        parts.append(
            f'<text x="{x + 18}" y="{y + 27}" font-family="system-ui, sans-serif" '
            f'font-size="17" font-weight="700" fill="#111827">{claim_id}</text>'
        )
        parts.append(
            f'<text x="{x + node_w - 18}" y="{y + 26}" text-anchor="end" '
            'font-family="system-ui, sans-serif" font-size="11" font-weight="600" '
            f'fill="#374151">{escape(claim.claim_type)}</text>'
        )
        for index, line in enumerate(wrapped_claim(claim.normalized)):
            parts.append(
                f'<text x="{x + 18}" y="{y + 54 + index * 18}" '
                'font-family="system-ui, sans-serif" font-size="14" '
                f'fill="#111827">{escape(line)}</text>'
            )
        parts.append(
            f'<text x="{x + 18}" y="{y + 120}" '
            'font-family="system-ui, sans-serif" font-size="11" '
            f'fill="#4b5563">{escape(claim.status)}</text>'
        )
        for index, line in enumerate(audit_lines[claim_id]):
            parts.append(
                f'<text x="{x + 18}" y="{y + 136 + index * 16}" '
                'font-family="system-ui, sans-serif" font-size="11" '
                f'fill="#4b5563">{escape(line)}</text>'
            )
        parts.append("</g>")

    # Draw labels after nodes so every relationship remains readable.  A small
    # neutral pill masks the line beneath the label without hiding its style.
    for label, label_x, label_y in edge_labels:
        label_w = min(214.0, max(62.0, len(label) * 6.15 + 16))
        parts.append(
            f'<g><rect x="{label_x - label_w / 2}" y="{label_y - 13}" '
            f'width="{label_w}" height="20" rx="7" fill="#ffffff" '
            'stroke="#cbd5e1" stroke-width="1"/>'
            f'<text x="{label_x}" y="{label_y + 1}" text-anchor="middle" '
            'font-family="system-ui, sans-serif" font-size="11" fill="#475569">'
            f'{escape(label)}</text></g>'
        )

    legend_y = canvas_h - 78
    legend_x = margin_x
    parts.append(
        f'<text x="{legend_x}" y="{legend_y - 18}" font-family="system-ui, sans-serif" '
        'font-size="13" font-weight="600" fill="#111827">Claim types</text>'
    )
    for index, (claim_type, (fill, stroke)) in enumerate(TYPE_STYLE.items()):
        column = index % 3
        row = index // 3
        x = legend_x + column * 355
        y = legend_y + row * 30
        parts.append(
            f'<rect x="{x}" y="{y - 13}" width="18" height="18" rx="4" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
            f'<text x="{x + 27}" y="{y + 1}" font-family="system-ui, sans-serif" '
            f'font-size="12" fill="#111827">{escape(claim_type)}</text>'
        )
    parts.append(
        f'<text x="{canvas_w - margin_x}" y="{canvas_h - 39}" text-anchor="end" '
        'font-family="system-ui, sans-serif" font-size="11" fill="#475569">'
        'Solid arrows: manuscript-explicit or author-confirmed. Dashed arrows: AI-proposed.</text>'
    )
    parts.append(
        f'<text x="{canvas_w - margin_x}" y="{canvas_h - 20}" text-anchor="end" '
        'font-family="system-ui, sans-serif" font-size="11" fill="#475569">'
        'Node border: red = must correct; amber dashed = should clarify; gray dashed = outside NAH scope.</text>'
    )
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    project = args.project.resolve()
    claim_path = project / "knowledge/nah/CLAIM_LEDGER.md"
    relation_path = project / "knowledge/nah/CLAIM_RELATIONS.md"
    output = args.output or project / "reports/CLAIM_NETWORK.svg"

    claims = parse_claims(claim_path)
    groups, relations = parse_relationships(relation_path)
    svg = render_svg(
        claims,
        groups,
        relations,
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(svg, encoding="utf-8")
    print(f"Wrote {output} with {len(claims)} claims and {len(relations)} relations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
