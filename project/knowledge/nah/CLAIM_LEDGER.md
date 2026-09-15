# Manuscript claim ledger

This file records important manuscript claims and connects them to source
checkpoints, calculations, assumptions, or physical proposals.

## Indexed manuscript

- Source root (relative to project/): `source/`
- Manuscript: `main.tex`
- Bibliography: `references.bib`
- Source ZIP: Class_S - 2026-09-15T131046.747.zip
- Last indexed: 2026-09-15

## Claim types

- `THEOREM CONSEQUENCE`
- `MODEL CALCULATION`
- `MODEL ASSUMPTION`
- `STANDARD BACKGROUND`
- `PHYSICAL PROPOSAL`
- `PHYSICAL ANSATZ`

## Audit statuses

- `SUPPORTED`
- `SUPPORTED WITH CONVENTION`
- `ASSUMPTION EXPLICIT`
- `PROPOSAL CLEARLY LABELED`
- `SHOULD CLARIFY`
- `MUST CORRECT`
- `INTERNAL ONLY`
- `OUTSIDE NAH SCOPE`

| Claim ID | Stable manuscript anchor | Normalized claim | Claim type | Required support | Current support | Hypotheses or limitations | Audit status | Last audit | Audited source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `NAH-C001` | `SEC: NAH intro`; “associated vector-bundle form”; `subsec:physical-interpretation-cusp-label` | The tame associated vector-bundle correspondence supplies a flat connection up to gauge from fixed Higgs and parabolic data. | `THEOREM CONSEQUENCE` | Compact and tame vector-bundle correspondences and uniqueness, with the appropriate stability and characteristic hypotheses | `SIM92-THM-1`, `SIM92-COR-1.3`, `SIM92-METRIC-CONSTRUCTIONS`, `SIM90-MAIN-THM`, `MOC04-THM-1.4`, `MOC04-PROP-5.2`, `MOC09-THM-1.1` | Full Higgs and parabolic data are fixed; does not invoke a full punctured principal-`G` category | `SUPPORTED` | 2026-09-15 | source/main.tex (Class_S - 2026-09-15T131046.747.zip) |
| `NAH-C002` | “Logarithmic singularities”; `M_p=\exp(2\pi iR_p)` | For `nabla=d-R dz/z`, the chosen convention gives `M=exp(2 pi i R)`. | `MODEL CALCULATION` | Direct horizontal-section calculation and source convention translation | `DEL70-DEF-1.14-1.17`, `DEL70-PROP-3.11`, `SIM90-LEM-3.2`, `SIM90-RESIDUE-TABLE` | Chosen logarithmic model and branch; `R` is the negative connection-matrix residue, not the Higgs residue alone | `SUPPORTED WITH CONVENTION` | 2026-09-15 | source/main.tex (Class_S - 2026-09-15T131046.747.zip) |
| `NAH-C003` | `eq:leading-flat-section-growth`; `eq:generic-tube-transfer`; `eq:single-tube-factor-multivariable` | In the logarithmic model, u-to-v transfer has factor `q^R=q^alpha exp(e log q)`; general tame growth requires the cited estimates. | `MODEL CALCULATION` | Direct solution plus the correct asymptotic source hierarchy | `DEL70-DEF-1.14-1.17`, `SIM90-WEIGHT-NORM`, `MOC02-THM-9.3`, `MOC03-THM-13.1`, `MOC03-THM-13.2` | Fixed cutoff factors are absorbed; general tame estimates are sectorial and require compatible KMS/weight data | `SUPPORTED` | 2026-09-15 | source/main.tex (Class_S - 2026-09-15T131046.747.zip) |
| `NAH-C004` | “Logarithmic singularities”; “is encoded by a parabolic, or filtered, extension” | Tame growth is encoded by a filtered/parabolic extension with filtration data beyond a chosen logarithmic exponent. | `THEOREM CONSEQUENCE` | Filtered-object definitions and KMS comparison | `SIM90-DEF-FILTERED-HIGGS`, `SIM90-DEF-FILTERED-LOCAL`, `MOC03-DEF-2.1-2.3`, `MOC09-LEM-6.1-6.4-COR-6.5` | Growth weights and filtrations are additional data | `SUPPORTED` | 2026-09-15 | source/main.tex (Class_S - 2026-09-15T131046.747.zip) |
| `NAH-C005` | `sec:nah-asymptotics`; “base-coordinate loops and the corresponding Dehn twists” | Distinct disjoint fiberwise tubes need not obey the intersecting-SNC residue commutation condition. | `MODEL CALCULATION` | Geometric distinction plus the exact scope of the SNC theorem | `DEL70-DEF-3.8-PROP-3.10`, `DEL70-THM-4.1-DEF-4.2`, `MOC03-THM-12.2-COR-12.5-12.7-THM-12.3` | Does not assert a noncommuting multivariable SNC residue system | `SUPPORTED` | 2026-09-15 | source/main.tex (Class_S - 2026-09-15T131046.747.zip) |
| `NAH-C006` | `eq:ordered-multitube-singular`; “We assume that the off-tube matching matrices” | Off-tube matching matrices remain regular and invertible. | `MODEL ASSUMPTION` | Explicit assumption; local NAH sources do not prove global family regularity | `DEL70-THM-1.19-COR-1.20`, `MOC03-THM-13.2` provide only local support | Conclusions using the ordered singular factor depend on this assumption | `ASSUMPTION EXPLICIT` | 2026-09-15 | source/main.tex (Class_S - 2026-09-15T131046.747.zip) |
| `NAH-C007` | `eq:indexed-jordan-centralizer` | The type-A reductive quotient of the monodromy centralizer has the displayed Jordan-block multiplicity formula. | `STANDARD BACKGROUND` | Lie-theory/Jordan-centralizer calculation | External Lie-theory reference in `references.bib`; not an NAH checkpoint | Requires a separate Lie-theory audit if formal certification is desired | `OUTSIDE NAH SCOPE` | 2026-09-15 | source/main.tex (Class_S - 2026-09-15T131046.747.zip) |
| `NAH-C008` | `eq:monodromy-gauge-full-stabilizer`; “We motivate compatibility” | `h_i subseteq c_i` is a compatibility condition for an independently specified weak gauging and does not determine the gauge group. | `PHYSICAL PROPOSAL` | Clear separation of monodromy preservation from fixture/gluing data | NAH supplies monodromy data; class-S physics supplies `h_i` | Identifying weak-gauge generators with flat tube symmetries is a physical requirement; realization depends on fixture/gluing data, matter, and conformality | `PROPOSAL CLEARLY LABELED` | 2026-09-15 | source/main.tex (Class_S - 2026-09-15T131046.747.zip) |
| `NAH-C009` | `subsec:physical-interpretation-cusp-label`; `eq:schematic-localization-cusp`; “Monodromy-sensitive observables” | Finer monodromy-sensitive observables are proposed for future work; the leading cusp estimate uses independent weak-gauge data. | `PHYSICAL PROPOSAL` | Clear separation of the future monodromy-sensitivity proposal from NAH and the conditional physics estimate | Outside the NAH theorem ledger; C001 supplies only the associated flat object | Leading localization estimate assumes a regular nonzero gluing factor; localization, sewing, and observable dependence require separate physics analysis | `PROPOSAL CLEARLY LABELED` | 2026-09-15 | source/main.tex (Class_S - 2026-09-15T131046.747.zip) |
