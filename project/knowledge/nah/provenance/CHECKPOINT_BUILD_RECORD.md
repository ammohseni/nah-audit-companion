# Checkpoint construction and prompt record

## Purpose

This file preserves the prompts used to create the permanent non-Abelian Hodge source 
checkpoints and documents the procedure for maintaining and extending the collection.

This is a provenance record, not mathematical evidence. A checkpoint is
supported by the identified primary PDF and the exact passages read from that
PDF. The prompt that caused the extraction does not itself verify the extracted
statement.

## Recommended location

Keep this file at:

`knowledge/nah/provenance/CHECKPOINT_BUILD_RECORD.md`

Prompt and workflow history belongs under `provenance/`, separately from:

- `knowledge/nah/sources/`, which contains mathematical source checkpoints;
- `knowledge/nah/THEOREM_LEDGER.md`, which indexes extracted results;
- `knowledge/nah/OPEN_QUESTIONS.md`, which records unresolved mathematical
  issues; and
- `audits/`, which contains manuscript-specific findings.

## Current checkpoint-production procedure

The original prompts below implement the correct source-first architecture.
For a new or rebuilt checkpoint collection, use the following sequence.

### Stage 1: acquire and register primary sources

1. Read `papers/nah/SOURCE_MANIFEST.md`.
2. Retrieve only the identified primary mathematics papers.
3. Save each PDF under the prescribed stable filename in `papers/nah/`.
4. Record the exact paper identity, version, stable source URL, retrieval date,
   local filename, and SHA-256 hash.
5. If a PDF is unavailable, mark it `NEEDS USER PDF`; do not substitute a
   review, physics paper, abstract, snippet, or remembered statement.

### Stage 2: build one source checkpoint at a time

For each primary paper:

1. Record the bibliographic identity, local PDF filename and version.
2. Record the sections and page ranges actually read.
3. Extract each relevant definition, theorem, proposition, lemma and corollary
   with its exact number and page.
4. Preserve the complete hypotheses, conclusion, dependencies and source
   notation.
5. Put the translation into manuscript notation in a separate subsection.
6. Record limitations, convention choices and unresolved implications.
7. Add a short index entry to `THEOREM_LEDGER.md` pointing back to the detailed
   checkpoint.
8. Add unresolved questions to `OPEN_QUESTIONS.md`.
9. Date substantive checkpoint revisions and explain what changed; never
   silently overwrite an established extraction.

### Stage 3: assign evidence and human-review status

The current project terminology is:

- `AI-CHECKED FROM PDF`: the AI read the numbered result and the surrounding
  definitions directly in the identified primary PDF;
- `PARTIAL`: only part of the statement, hypotheses or dependency chain was
  checked;
- `NEEDS CHECK`: the extraction is not yet sufficient for manuscript support;
- `HUMAN-REVIEWED`: a human reviewer explicitly confirmed the extraction;
- `HUMAN-REVIEW NOT RECORDED`: no human-review status is known; and
- `HUMAN-REVIEW REQUESTED`: independent human review has been requested.

The historical prompts used `VERIFIED FROM PDF` and `NEEDS VERIFICATION`.
Those labels described an AI source check under the earlier workflow. For new
work, use `AI-CHECKED FROM PDF` and `NEEDS CHECK`, and record human review
separately. Do not interpret an AI check as independent human certification.

### Stage 4: consolidate without merging incompatible results

After individual source files exist:

1. check duplicate ledger entries;
2. reconcile notation translations while retaining each source convention;
3. compare sign and `2 pi i` conventions explicitly;
4. distinguish compact from punctured settings;
5. distinguish trivial from nontrivial parabolic data;
6. distinguish special nilpotent results from general tame/KMS results;
7. keep `PARTIAL` and `NEEDS CHECK` limitations visible; and
8. move unresolved cross-source comparisons to `OPEN_QUESTIONS.md`.

Do not combine statements from different papers unless their hypotheses,
objects and conventions have been checked for compatibility.

## Recommended reusable prompts

These prompts use the current project terminology and may be reused when the
checkpoint collection is rebuilt or extended.

### A. Store and register the source PDFs

> Use NAH Audit in CHECKPOINT MODE.
>
> Do not review or edit `main.tex`.
>
> Read `papers/nah/SOURCE_MANIFEST.md`. Retrieve the listed primary mathematics
> papers and save each accessible PDF permanently in `papers/nah/` under the
> prescribed filename. For every source, record its exact bibliographic
> identity, version, stable source URL, retrieval date, local filename and
> SHA-256 hash.
>
> Do not substitute physics papers, reviews, abstracts, search snippets or
> remembered summaries for a primary mathematics source.
>
> If a paper cannot be retrieved, mark it `NEEDS USER PDF` and provide the
> exact list of PDFs that I must supply. Do not begin checkpoint extraction
> from an unavailable source.

### B. Build one source checkpoint

> Use NAH Audit in CHECKPOINT MODE. Process only `<SOURCE-KEY>` in this run.
>
> Do not audit or edit `main.tex`. Inspect it only when a separate translation
> into manuscript notation is required.
>
> Read the relevant definitions and results directly in the locally stored
> primary PDF. Create or update
> `knowledge/nah/sources/<source-key>.md`. Record the paper identity, PDF
> version, local filename, and every section and page range actually read.
>
> For each relevant definition, theorem, proposition, lemma or corollary,
> record its exact number, page, complete hypotheses, conclusion, dependencies
> and source notation. Put the manuscript-notation translation in a separate
> subsection. Record limitations and unresolved convention or applicability
> questions explicitly.
>
> Mark each extraction `AI-CHECKED FROM PDF`, `PARTIAL`, or `NEEDS CHECK`.
> Record human-review status separately and do not infer human review.
>
> Update `knowledge/nah/THEOREM_LEDGER.md` with short entries pointing to the
> detailed checkpoint and update `knowledge/nah/OPEN_QUESTIONS.md` for every
> unresolved issue. Date substantive revisions and explain what changed. Do
> not silently overwrite existing checkpoint content or add results from
> memory.

### C. Process the compact and curve foundations

> Use NAH Audit in CHECKPOINT MODE.
>
> Process `SIM92`, `COR88`, and `SIM90` from their locally stored primary PDFs,
> one source at a time. Apply the complete one-source checkpoint protocol to
> each paper.
>
> Pay particular attention to the objects being compared, compact versus
> punctured hypotheses, stability or semisimplicity conditions, characteristic
> class assumptions, prescribed puncture behavior, and the precise scope of
> each correspondence.
>
> Do not audit or edit `main.tex`, use physics sources, or merge compact and
> punctured statements without an explicit compatibility check.

### D. Process the Mochizuki sources

> Use NAH Audit in CHECKPOINT MODE.
>
> Process `MOC02`, `MOC03`, `MOC04`, and `MOC09` from their locally stored
> primary PDFs, one source at a time. Apply the complete one-source checkpoint
> protocol to each paper.
>
> Pay particular attention to tame harmonic bundles; filtered and parabolic
> structures; trivial versus nontrivial parabolic weights; nilpotent Higgs
> residues; de Rham residues and local monodromy; adapted harmonic metrics;
> asymptotic estimates for flat sections; monodromy weight filtrations; and
> differences among the assumptions, categories and conventions of the four
> papers.
>
> Do not merge results from different Mochizuki papers unless their hypotheses,
> objects and conventions have been explicitly checked for compatibility.
> Update the individual source files, `THEOREM_LEDGER.md`, and
> `OPEN_QUESTIONS.md`. Do not audit or edit `main.tex`.

### E. Process Deligne

> Use NAH Audit in CHECKPOINT MODE. Process only `DEL70` from the locally stored
> primary source.
>
> Build a permanent checkpoint focused on regular-singular flat connections,
> logarithmic extensions, logarithmic residues, residue-to-monodromy formulas,
> canonical extensions and residue strips, several normal-crossing variables,
> commuting residues, choices of logarithm, and sign or `2 pi i` conventions.
>
> Record exact definitions and result numbers, pages, complete hypotheses,
> conclusions, dependencies and source notation. Keep translation into the
> manuscript convention separate. Update `THEOREM_LEDGER.md` and
> `OPEN_QUESTIONS.md`.
>
> Do not audit or edit `main.tex`, rely on physics papers, or import a
> several-variable normal-crossing conclusion into disjoint one-dimensional
> plumbing tubes without an explicit geometric comparison.

### F. Consolidate the knowledge base

> Use NAH Audit in CHECKPOINT MODE.
>
> Review the existing files in `knowledge/nah/sources/` and consolidate
> `knowledge/nah/THEOREM_LEDGER.md` without changing the source statements.
>
> Check for duplicate results; inconsistent notation translations; incompatible
> sign or `2 pi i` conventions; differences between compact and punctured
> settings; differences between trivial and nontrivial parabolic structures;
> results established in one source but only assumed in another; and entries
> marked `PARTIAL` or `NEEDS CHECK`.
>
> Do not add results from memory, audit `main.tex`, or hide unresolved
> incompatibilities. Give a short gap report in
> `knowledge/nah/OPEN_QUESTIONS.md`.

## Historical prompts used

The following prompts are preserved as supplied by the project author. Their
status terminology reflects the earlier version of the workflow.

### 1. Storing the papers

> Use NAH Audit.
>
> Do not review or edit main.tex yet.
>
> Read papers/nah/SOURCE_MANIFEST.md. Retrieve the listed primary mathematics
> papers and save each accessible PDF permanently in papers/nah/ using the
> prescribed filename. Update the manifest with the exact version, stable
> source URL, retrieval date, and status.
>
> Do not substitute physics papers, reviews, abstracts, search snippets, or
> remembered summaries for the primary mathematical sources.
>
> If a paper cannot be retrieved, mark it NEEDS USER PDF and give me an exact
> list of the files I must supply.

### 2. Building the checkpoints: initial sources

> Use NAH Audit.
>
> Do not review or edit main.tex yet. Begin building the permanent NAH knowledge
> base from the locally stored primary PDFs.
>
> Start with SIM92, COR88, and SIM90. For each paper:
>
> 1. Read the relevant definitions and results in the primary PDF.
> 2. Create knowledge/nah/sources/<source-key>.md.
> 3. Extract the relevant definitions, theorems, propositions, lemmas, and
>    corollaries.
> 4. Record exact numbers, pages, complete hypotheses, conclusions, dependencies,
>    and source notation.
> 5. Translate the results into the notation used in main.tex, but keep that
>    translation separate from the source statement.
> 6. Mark each extraction VERIFIED FROM PDF, PARTIAL, or NEEDS VERIFICATION.
> 7. Update knowledge/nah/THEOREM_LEDGER.md.
> 8. Record unresolved issues in knowledge/nah/OPEN_QUESTIONS.md.
>
> Do not use physics papers and do not make stylistic comments about the
> manuscript.

### 2a. One-source variant

> Use NAH Audit. Process only SIM92 in this run. Build a detailed permanent
> source checkpoint from the primary PDF and update the theorem ledger. Do not
> inspect main.tex except when translating notation.

### 2b. Mochizuki sources

> Use NAH Audit.
>
> Do not audit main.tex yet. Process MOC04, MOC02, MOC03, MOC09 from the primary
> PDFs, one source at a time.
>
> Pay particular attention to:
>
> - tame harmonic bundles;
> - filtered and parabolic structures;
> - trivial versus nontrivial parabolic weights;
> - nilpotent Higgs residues;
> - de Rham residues and local monodromy;
> - adapted harmonic metrics;
> - asymptotic estimates for flat sections;
> - monodromy weight filtrations;
> - assumptions that differ between MOC02, MOC03, MOC04, and MOC09.
>
> Create or update the corresponding files under knowledge/nah/sources/, update
> knowledge/nah/THEOREM_LEDGER.md, and record unresolved comparisons in
> knowledge/nah/OPEN_QUESTIONS.md.
>
> Do not merge results from different Mochizuki papers unless you explicitly
> verify that their hypotheses and conventions are compatible.

### 2c. Deligne source

> Use NAH Audit.
>
> Process DEL70 from the primary source. Build a permanent checkpoint focused
> on:
>
> - regular-singular flat connections;
> - logarithmic extensions;
> - logarithmic residues;
> - the relation between residue and local monodromy;
> - canonical extensions and residue strips;
> - several normal-crossing variables and commuting residues;
> - choices of logarithm and sign or 2 pi i conventions.
>
> Update knowledge/nah/THEOREM_LEDGER.md and
> knowledge/nah/OPEN_QUESTIONS.md.
>
> Do not audit main.tex yet and do not rely on physics papers.

### 3. Consolidating the knowledge

> Use NAH Audit.
>
> Review the existing files in knowledge/nah/sources/ and consolidate
> knowledge/nah/THEOREM_LEDGER.md.
>
> Check for:
>
> - duplicate results;
> - inconsistent notation translations;
> - incompatible sign or 2 pi i conventions;
> - differences between compact and punctured settings;
> - differences between trivial and nontrivial parabolic structures;
> - statements verified in one source but only assumed in another;
> - entries marked PARTIAL or NEEDS VERIFICATION.
>
> Do not add results from memory. Do not audit main.tex. Give me a short report
> of the remaining gaps in knowledge/nah/OPEN_QUESTIONS.md.

## Interpretation of this record

The historical prompts show that the checkpoints were designed to be built
from primary PDFs before the manuscript was audited. They also explicitly
required exact result numbers, pages, hypotheses, conclusions, dependencies,
notation translations and unresolved-question tracking. This is the correct
architecture.

For current use, the main improvements are to record PDF hashes and sections
actually read, use `AI-CHECKED FROM PDF` rather than an unqualified
`VERIFIED FROM PDF`, track human review separately, and date every substantive
checkpoint revision.
