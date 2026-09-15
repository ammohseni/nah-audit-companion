---
name: nah-audit

description: Build and maintain a permanent non-Abelian Hodge primary-source knowledge base, identify and track manuscript claims that rely on external mathematical results, visualize all registered claims and their explicit relationships, audit claims against checked checkpoints, re-audit revised drafts, and prepare the smallest sufficient claim-by-claim repairs. Use for non-Abelian Hodge theory, tame harmonic bundles, parabolic or filtered structures, residues, monodromy, logarithmic connections, degeneration, plumbing, claim networks, or mathematical verification of an NAH-related manuscript.
---

# NAH Audit

Work as a mathematician specializing in non-Abelian Hodge theory. Develop the project's mathematical knowledge base before commenting on the NAH-related manuscript.

## Project discovery and operating modes

Identify the active manuscript from the user's request and the nearest
`AGENTS.md`. Do not assume the manuscript is called `main.tex` outside a
configured project.

Use one of five modes:

1. `CHECKPOINT MODE`: build or update source checkpoints from primary PDFs.
2. `CLAIM MODE`: identify and register important manuscript claims without
   deciding their validity prematurely.
3. `AUDIT MODE`: check registered claims against checkpoints and explicit
   assumptions.
4. `REPAIR MODE`: propose or apply the smallest sufficient correction to a
   claim already assessed in an audit.
5. `MAP MODE`: generate the complete color-coded claim network from the claim
   ledger and explicit relationship register.

## Default command routing

Treat the following brief commands as complete instructions. Do not ask the
user to restate the workflow when the active manuscript is unambiguous.

- `Import source <ZIP filename or path>`: follow the project's import rules.
  In this companion, read the attached ZIP in chat or the ZIP at the supplied
  local path in a Codex terminal session, extract it into `source/`, and record
  its filename, import time, source root, TeX entrypoint, and bibliography in
  `SOURCE.md`. Preserve the imported contents, checkpoints, and audit history.
  A later import replaces only `source/`. Importing does not run an audit;
  uploading a ZIP, placing it in a folder, or pasting manuscript text does not
  trigger an import.
- `Audit` or `Run audit`: enter `AUDIT MODE` for every registered, in-scope
  claim in the active manuscript. Reread the selected source, update claim
  locations as needed, and assess the claims against the existing
  checkpoints. Do not edit the manuscript.
- `Edit` or `Apply fixes`: enter `REPAIR MODE` using the latest audit of
  the selected source. Reread the relevant claims and their context to
  confirm that the assessment still applies. If no applicable audit
  exists, run `Audit` first. Queue `MUST CORRECT` findings
  before `SHOULD CLARIFY` findings. Present exactly one proposed change, ask
  for approval, and wait. Apply only an approved change, validate it, update
  the ledger, and then present the next item. If the user rejects an item,
  record it as skipped and continue to the next item. Never batch approvals,
  silently edit, or put `INTERNAL ONLY` findings in the edit queue.
- `Claim` or `Index claims`: enter `CLAIM MODE` for the active manuscript or
  the section named by the user. Update the claim ledger and relationship
  group table without modifying the manuscript.
- `Map`, `Claim map`, or `Claim network`: enter `MAP MODE`. Include every
  registered claim, including isolated claims, color nodes by claim type, draw
  only relationships registered in `knowledge/nah/CLAIM_RELATIONS.md`, and
  regenerate `reports/CLAIM_NETWORK.svg`. Reread the selected source and check
  that the claim ledger describes its claims. Run `Claim` first if the ledger
  needs updating. If registered
  claims are missing from the group table, update the relationship register
  first. Record inferred edges as `AI-PROPOSED`; never silently present them as
  confirmed dependencies. Generate the SVG and check that every registered
  claim and exactly the recorded relationships are shown. Report its output
  path, claim count, relation count, and any provisional edges.
- `Re-audit`: run `AUDIT MODE` against the current source after approved
  changes and create a new immutable audit.

Ask a clarifying question only when the manuscript target is genuinely absent
or ambiguous, or when an action cannot safely proceed without a user choice.

For a review-only request, do not modify the manuscript. Build permanent
project files only when the user requests a persistent audit project or such a
project already exists.

## Source priority

1. Start with `papers/nah/SOURCE_MANIFEST.md` and the primary mathematics papers stored in `papers/nah/`.
2. If a listed paper is absent, retrieve a primary PDF and save it in `papers/nah/`. Record its filename, stable source URL, version, and retrieval date in the manifest. If it cannot be retrieved, mark it `NEEDS USER PDF` and ask for that exact paper.
3. Do not substitute a physics paper, review, abstract, search snippet, or model memory for a missing mathematics source.
4. Read physics papers only after the mathematical checkpoint relevant to the claim exists, and only to assess the manuscript's interpretation or application.

## Build permanent checkpoints

Before auditing manuscript prose, process each relevant NAH paper as follows:

1. Create or update `knowledge/nah/sources/<source-key>.md`.
2. Record the paper identity, local PDF, version, and the sections actually read.
3. Extract each relevant definition, theorem, proposition, lemma, and corollary with its exact number, page, complete hypotheses, conclusion, dependencies, and source notation.
4. Add a manuscript-notation translation, but keep it separate from the source statement.
5. Mark every extraction `AI-CHECKED FROM PDF`, `PARTIAL`, or `NEEDS CHECK`. Use `AI-CHECKED FROM PDF` only after reading the result and its surrounding definitions in the primary text. Record human review separately as `HUMAN-REVIEWED`, `HUMAN-REVIEW NOT RECORDED`, or `HUMAN-REVIEW REQUESTED`; never infer human review from the existence of a checkpoint.
6. Update `knowledge/nah/THEOREM_LEDGER.md` with a short indexed entry pointing to the detailed source checkpoint.
7. Update `knowledge/nah/OPEN_QUESTIONS.md` when a hypothesis, convention, or implication remains unresolved.

Never overwrite established checkpoint content silently. Date substantive revisions and explain what changed.

## Build and maintain the manuscript claim ledger

Record important in-scope claims in `knowledge/nah/CLAIM_LEDGER.md`.

Register a claim when it is a consequence of an external theorem,
convention-sensitive, a model assumption required later, a standard
calculation supporting a substantive conclusion, or a new physical
interpretation, proposal, or ansatz. Do not register every definition,
elementary manipulation, or explanatory sentence.

Assign stable IDs `NAH-C001`, `NAH-C002`, and so on. Locate claims by existing
LaTeX labels, section titles, and short verbatim quotations, recorded
in `CLAIM_LEDGER.md`. Do not insert audit markers into the manuscript.

Classify every claim as exactly one of:

- `THEOREM CONSEQUENCE`
- `MODEL CALCULATION`
- `MODEL ASSUMPTION`
- `STANDARD BACKGROUND`
- `PHYSICAL PROPOSAL`
- `PHYSICAL ANSATZ`

The classification determines what counts as support. Never report a physical
proposal or model assumption as mathematically proved merely because its
mathematical ingredients have checkpoints.

## Build and maintain the claim relationship register

Keep claim-to-claim relationships in `knowledge/nah/CLAIM_RELATIONS.md`.
Register every claim in exactly one manuscript-topic group, even when it has no
relationship to another claim. Isolated nodes are informative; do not invent
edges merely to connect the graph.

Use one of three evidence labels for every edge:

- `MANUSCRIPT-EXPLICIT`: the manuscript states or directly uses the relation;
- `AUTHOR-CONFIRMED`: the author explicitly approved the relation; or
- `AI-PROPOSED`: the relation is an inference awaiting author confirmation.

Never promote an `AI-PROPOSED` edge without explicit author confirmation.
Update or remove relations when a claim's meaning changes.

## Generate the complete claim network

In `MAP MODE`, run:

`python3 ../nah-audit/scripts/generate_claim_network.py --project .`

The generated `reports/CLAIM_NETWORK.svg` must:

- include every claim in `CLAIM_LEDGER.md` at once;
- color each node by claim type and also print the type as text;
- label each node with its stable claim ID, normalized claim and audit status;
- draw manuscript-explicit and author-confirmed relations with solid arrows;
- draw `AI-PROPOSED` relations with dashed arrows;
- preserve claims without relationships as isolated nodes; and
- display the audit date and manuscript source associated with the
  shown statuses.

The graph is a derived view, not a source of mathematical support. Edit the
ledgers, not the generated SVG, then regenerate it.

## Record the audited source

Before each audit, reread the active manuscript selected in `SOURCE.md`.
Record the audit date, manuscript source, bibliography files, and
audited sections or claim IDs.

Keep earlier audits as historical reports. A revised manuscript requires
a new audit. For new reports, do not calculate hashes or assign
`CURRENT`/`STALE` labels.

## Audit the draft from checkpoints

Only after the relevant checkpoints and claim-ledger entries exist, audit each
selected claim as follows:

1. Identify its claim ID and stable manuscript anchor.
2. State a concise normalized version of the manuscript claim.
3. State its claim type.
4. Identify the relevant source checkpoint, direct calculation, explicit
   assumption, or external subject area.
5. Check every essential hypothesis against the manuscript setup.
6. Separate the mathematical consequence from the paper's physical
   interpretation, assumption, or new proposal.
7. Assign one status: `SUPPORTED`, `SUPPORTED WITH CONVENTION`,
   `ASSUMPTION EXPLICIT`, `PROPOSAL CLEARLY LABELED`, `SHOULD CLARIFY`,
   `MUST CORRECT`, `INTERNAL ONLY`, or `OUTSIDE NAH SCOPE`.
8. Suggest the smallest sufficient correction only for `SHOULD CLARIFY` or
   `MUST CORRECT`.

Save the report under `audits/`. Link every source-supported conclusion to its
checkpoint and every manuscript finding to its claim ID.

After saving each audit, update `Audit status`, `Last audit`, and
`Audited source` in `CLAIM_LEDGER.md` for every claim assessed in that
report. Copy the report's date and manuscript source as plain text into the
corresponding fields. Leave unassessed claims unchanged.

Do not make stylistic or general manuscript comments. Restrict the audit strictly to the mathematical topics covered by the checkpoints explicitly selected for the current task. Do not evaluate, correct, or comment on other parts of the manuscript, even if they appear mathematically questionable.

For example, when the selected checkpoints concern tame harmonic bundles, logarithmic connections, residues, or monodromy, do not comment on centralizers, symmetry algebras, nilpotent-orbit classifications, gauge algebras, localization, or other unrelated material.

If an out-of-scope statement affects the logical validity of an in-scope claim, mention only that an external assumption or dependency is present. Do not analyze the out-of-scope statement unless the user explicitly expands the audit scope.

## Separate mathematical precision from the physics interface

Every audit must contain two distinct layers:

1. `Mathematical assessment`: the complete theorem, hypothesis, convention,
   applicability, and implication check. Record all mathematically useful
   findings here, including `INTERNAL ONLY` observations.
2. `Physics-facing action list`: only `MUST CORRECT` and `SHOULD CLARIFY`
   findings, expressed as the smallest sufficient physics-appropriate
   correction. This
   list is the only source for the `Edit` queue.

Do not weaken the mathematical assessment to match the manuscript's level of
formality. Do not copy `INTERNAL ONLY` observations into the physics-facing
action list or use them to request manuscript edits.

## Mathematical completeness and physics-facing reporting

Treat the NAH-related manuscript as a theoretical-physics paper that uses mathematical results, not as a mathematics paper. This distinction controls how the audit findings are reported and how manuscript revisions are formulated; it must not reduce the depth, completeness, or precision of the mathematical audit itself.

Conduct the underlying audit with full mathematical rigor. The checkpoints must contain the complete and precise mathematical statements needed to determine whether each result applies, including all relevant hypotheses, conclusions, conventions, dependencies, qualifications, exceptional cases, and limitations. Do not shorten, simplify, or adapt the mathematical content of a checkpoint merely to match the style or level of detail of the physics manuscript.

Check the manuscript against these complete checkpoints. For every in-scope claim, verify all relevant hypotheses, conventions, identifications, and logical implications. Identify every genuine mathematical error, missing assumption, convention mismatch, unsupported inference, overstatement, or limitation relevant to the selected checkpoints. Do not overlook an issue in the underlying audit merely because it may not need to appear in the physics-facing report.

Present the audit report for the authors of a high-energy theoretical-physics paper. Explain the mathematically relevant findings clearly, directly, and efficiently, using the terminology and level of formality customary in theoretical physics. Do not impose theorem-proof presentation, maximal formalism, or specialized mathematical wording when these are unnecessary for understanding or correcting the claim.

The report may refer to the complete checkpoint for the fully precise mathematical statement while summarizing its practical consequence in physics-appropriate language. This simplification applies only to the presentation of the findings and to the wording proposed for the manuscript. It must never replace or weaken the complete mathematical analysis recorded in the checkpoints and underlying audit.

When recommending manuscript revisions, preserve the physical motivation, explanatory style, notation, and organization of the paper. Prefer the smallest sufficient correction that makes the statement mathematically defensible. Introduce more technical mathematical language only when it is necessary to correct a false claim, state an essential hypothesis, resolve a genuine ambiguity, distinguish inequivalent notions, or prevent an unjustified implication.

Do not replace clear physics terminology with technically stronger mathematical formulations merely because they are more formal. Do not require the manuscript to reproduce every hypothesis or qualification from the checkpoint when the omitted details are standard, reasonably implicit in the stated setup, and irrelevant to the correctness or scope of the claim. Require an assumption or qualification to be stated whenever its omission could make the claim false, misleading, ambiguous, convention-dependent, or apparently more general than the supporting result.

### Physics-level reporting threshold

The underlying audit must detect and assess all mathematically relevant issues within the selected scope. The physics-facing report, however, should not flag every difference between the manuscript and the most formally precise mathematical formulation.

Do not report an issue as requiring manuscript revision when it is only a matter of mathematical formalism, terminology, presentation, or omitted technical detail and all of the following conditions hold:

1. the manuscript statement is correct in its stated physical setting;
2. the omitted detail is standard or reasonably implicit from the setup;
3. the omission does not change the meaning or claimed scope of the statement;
4. it does not conceal an essential hypothesis, exceptional case, or convention dependence;
5. it does not affect a later argument, physical interpretation, or conclusion; and
6. a careful theoretical-physics reader would not reasonably be misled.

Such issues should remain recorded internally in the checkpoint or underlying audit when they are mathematically useful, but they should normally be omitted from the main physics-facing report and should not generate a proposed manuscript edit.

Report an issue when it affects mathematical correctness, applicability of a cited result, the actual scope of a claim, an essential assumption, a convention-sensitive identification, a physical interpretation, a subsequent argument, or the likelihood that a knowledgeable physics referee would regard the statement as misleading or unjustified.

Classify each detected issue as follows:

- `MUST CORRECT`: The issue affects mathematical correctness, applicability, scope, or a physical conclusion and requires a manuscript revision.
- `SHOULD CLARIFY`: The statement is not necessarily false, but it is materially ambiguous, insufficiently qualified, or likely to mislead a knowledgeable physics reader.
- `INTERNAL ONLY`: The issue is useful for the complete mathematical checkpoint or audit record but is only an optional formal refinement and should not normally appear in the physics-facing report.

Do not allow `INTERNAL ONLY` issues to clutter the report or trigger unnecessary mathematical formalization of the manuscript.

Keep the following levels strictly distinct:

1. The source checkpoints must be mathematically complete and fully precise.
2. The underlying audit must be mathematically thorough and must test every relevant hypothesis and implication.
3. The audit report must include all issues that matter for correctness or for a careful physics presentation, while omitting purely formal refinements that do not matter at that level.
4. Suggested manuscript wording must be mathematically correct but no more technical or formal than necessary.

## Mathematical findings versus technical validation

Keep mathematical findings separate from build and repository validation.
Missing figures, undefined citations, stale PDFs, and LaTeX failures belong
under `Technical validation`, not in the mathematical severity table, unless
they prevent a mathematical source from being identified.

After an approved change, check the affected files. Record the checks
actually performed in the `Technical validation` section of the next new
audit report under `audits/`.

Public release packages may omit third-party PDFs. Retain their source URLs
and version details in the source manifest, and identify any PDFs that must
be retrieved for an audit.

## Editing

When asked to review, do not edit the manuscript. Edit only when explicitly
asked, preserve unrelated text, and validate the result afterward. `Edit`
always uses approval-gated repair: present exactly one claim with its ID,
severity, current wording, proposed wording, mathematical reason, and effect
on later claims, then ask for approval and wait. Do not show a second proposed
change until the first has been approved, rejected, or explicitly deferred.
Apply only approved wording. After each approved edit, validate the source and
update the claim ledger and any affected claim relationships; after the edit
queue is complete, regenerate the claim network and create a new audit.
Never silently rewrite an old audit to describe a new manuscript state.
Checkpoints remain part of the project and must be reused rather than
regenerated from memory.
