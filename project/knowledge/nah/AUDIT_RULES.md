# NAH audit rules

This file records established cross-source convention translations, source
hierarchies, scope boundaries, and manuscript-audit rules. These are not
individual source theorems and are not open questions.

## Development history

These instructions were developed iteratively through a human-directed,
AI-assisted process. An initial ruleset was refined after an earlier audit to 
improve physics-facing reporting, while retaining optional formal details 
and harmless differences in sign conventions in the full mathematical assessment.
 The rules define the audit procedure; verification of individual claims is recorded separately in the
checkpoints and ledgers.

## Evidence terminology

- `AI-CHECKED FROM PDF`: the primary result and its surrounding definitions
  were read directly in the identified PDF.
- `PARTIAL`: only part of the result, hypotheses, or dependency chain was
  checked.
- `NEEDS CHECK`: the source result has not yet been checked sufficiently for
  manuscript support.
- `HUMAN-REVIEWED`: a human reviewer explicitly confirmed the extraction.
- `HUMAN-REVIEW NOT RECORDED`: no human-review status is known.

An AI source check is not independent human certification.

## Claim types and required support

| Claim type | Required support |
| --- | --- |
| `THEOREM CONSEQUENCE` | A checked checkpoint plus verification of all essential hypotheses and conventions |
| `MODEL CALCULATION` | A reproducible derivation from explicitly stated model data |
| `MODEL ASSUMPTION` | Clear statement of the assumption and the conclusions that depend on it |
| `STANDARD BACKGROUND` | A direct calculation or an appropriate external subject reference when nontrivial |
| `PHYSICAL PROPOSAL` | Clear proposal/interpretation language and separation from mathematical theorems |
| `PHYSICAL ANSATZ` | Explicit ansatz status and no claim of derivation from NAH alone |

## Source hierarchy

1. Use `COR88` and `SIM92` for compact harmonic metrics and compact NAH.
   Neither supplies punctured tame filtrations, logarithmic residues, or
   parabolic weights.
2. Use `SIM90` for the punctured-curve vector-bundle correspondence.
3. Use `MOC04` for the higher-dimensional Higgs-side filtered
   Kobayashi--Hitchin theorem at `lambda=0`.
4. Use `MOC09` for the nonzero-`lambda` de Rham and filtered-local-system side.
5. Use `MOC02` only for the nilpotent, unipotent, trivial-parabolic special
   case.
6. Use `MOC03` for general KMS and sectorial local asymptotic estimates.
7. Use `DEL70` for regular singularity, logarithmic extensions, residues,
   canonical residue strips, and the residue-to-monodromy formula.

Do not use a compact theorem to justify puncture behavior or a special
nilpotent theorem to justify general nontrivial KMS asymptotics.

## Residue and monodromy conventions

In the Deligne, Simpson, and Mochizuki source convention, an ordinary flat
connection with logarithmic residue `A` has positive-loop monodromy
`exp(-2 pi i A)`. A nonzero `lambda`-connection residue must first be converted
to the ordinary flat residue by the relevant `lambda^{-1}` scaling.

The manuscript convention

`nabla = d - R dz/z`, `M = exp(+2 pi i R)`

is consistent because the connection-matrix residue is `-R`.
Translate source and manuscript conventions internally before assessing
a claim. If the statements agree after translation, classify the
difference as `INTERNAL ONLY` and propose no manuscript edit.

A physics-facing convention finding must identify the specific manuscript
claim that remains false, materially ambiguous, or unsupported after
translation, and explain the effect of the mismatch.

## Filtered and parabolic terminology

- MOC02 trivial parabolic structure is the special KMS case
  `KMS(E^0;n)=Z^n x {0}`.
- MOC04/MOC09 trivial characteristic numbers mean vanishing parabolic degree
  and second parabolic characteristic number.
- MOC09 canonical/Deligne parabolic structure is the condition
  `a+Re(alpha)=0` in the relevant convention.
- Graded semisimplicity concerns the nilpotent part of the residue on
  parabolic graded pieces.

These conditions are not interchangeable. A logarithm of semisimple
monodromy does not by itself determine the complete filtered/parabolic object.

## Strength of asymptotic claims

Distinguish three levels:

1. exact formulas for the chosen constant logarithmic model;
2. curve-level or nilpotent/trivial-parabolic norm estimates;
3. general KMS sectorial adapted-frame and flat-section estimates.

The factor `q^R=q^alpha exp(e log q)` is exact in the constant logarithmic
model. In the general tame setting it should be described as a leading
singular/model factor unless the complete hypotheses of the relevant
Mochizuki theorem are stated and checked.

## Associated vector bundles versus principal objects

The checkpoint base supports compact principal NAH and filtered/parabolic
vector-bundle correspondences. It does not yet contain a complete primary
checkpoint for the full parabolic/filtered principal `G` category required by
the strongest possible principal-bundle formulation. Keep manuscript claims
in the associated vector-bundle setting unless that source gap is closed.

## Multi-tube and SNC distinction

Deligne's commuting-residue statement concerns one integrable logarithmic
connection along intersecting components of a higher-dimensional SNC divisor.
The manuscript's different plumbing tubes are disjoint annular neighborhoods
inside a one-dimensional fiber. Do not import the SNC commutation conclusion
without first matching these geometries.

## NAH scope boundary

The NAH ledger certifies NAH inputs. It does not automatically certify:

- Lie-algebra Jordan-centralizer formulas;
- class-S fixture and gluing data;
- weak-gauge-algebra realization;
- localization and sewing formulas;
- Picard--Lefschetz claims beyond their stated interface with NAH.

Absence from the NAH ledger is not itself an error. Classify such statements
as standard background, model assumptions, physical proposals, or physical
ansatze and audit them in their proper subject area.

## Physics-facing reporting threshold

The underlying check must be mathematically complete, but the manuscript is a
theoretical-physics paper. Report a required correction only when an omission
affects correctness, applicability, scope, an essential convention, a later
argument, or the likelihood that a knowledgeable physics reader would be
misled. Keep purely formal refinements internal.

Use the audit statuses:

- `SUPPORTED`
- `SUPPORTED WITH CONVENTION`
- `ASSUMPTION EXPLICIT`
- `PROPOSAL CLEARLY LABELED`
- `SHOULD CLARIFY`
- `MUST CORRECT`
- `INTERNAL ONLY`
- `OUTSIDE NAH SCOPE`

## Separation of mathematical and physics-facing layers

Every audit has a `Mathematical assessment` containing the complete check of
theorems, hypotheses, conventions, applicability, and implications. It may
record `INTERNAL ONLY` observations that improve the permanent mathematical
record but do not require a change to a physics manuscript.

The separate `Physics-facing action list` contains only `MUST CORRECT` and
`SHOULD CLARIFY` findings and gives the smallest sufficient, physics-appropriate
wording that resolves each material issue. Only this action list may populate
the `Edit` queue.
Mathematical completeness must never be reduced to simplify the physics
interface, and purely formal refinements must never be promoted into edits.

## Claim-network evidence boundary

The claim network is a derived navigation view generated from
`CLAIM_LEDGER.md` and `CLAIM_RELATIONS.md`. It is not mathematical evidence and
does not replace a checkpoint, ledger entry, or audit finding. Include every
registered claim, retain isolated claims, and draw only registered relations.
Keep manuscript-explicit and author-confirmed relations visually distinct from
AI-proposed relations, and never promote an AI-proposed relation without the
author's explicit confirmation.

## Technical validation boundary

Missing figures, undefined bibliography keys, stale PDFs, hash mismatches, and
LaTeX failures belong in a separate `Technical validation` section. They are
not mathematical findings unless they prevent a source claim from being
identified or checked.
