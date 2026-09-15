# NAH re-audit of the imported manuscript -- 2026-09-15

## Manuscript and scope

- Audit date: 2026-09-15 (UTC).
- Audited source: source/main.tex (Class_S - 2026-09-15T131046.747.zip).
- Original ZIP: Class_S - 2026-09-15T131046.747.zip.
- Import time: 2026-09-15T11:31:30+00:00.
- Source root, relative to `project/`: `source/`.
- TeX entrypoint and bibliography within that root: `main.tex`, `references.bib`.
- Claims assessed: `NAH-C001` through `NAH-C009`. `NAH-C007` is recorded
  only as outside NAH scope; `NAH-C008` and `NAH-C009` are assessed only at
  their interface with NAH.
- Manuscript changes made during this run: none.

This re-audit reread the active manuscript selected in `SOURCE.md`, not a
compiled PDF and not an archived source. The assessed manuscript portions were
the NAH foundations, logarithmic singularity model, local and multi-tube
asymptotics, ordered transport, class-S monodromy framework, centralizer and
weak-gauging interface, decorated cusp label, observables discussion,
conclusion, associated-vector-bundle appendix, and `references.bib`.

The re-audit reuses the permanent checkpoints in `knowledge/nah/sources/` and
the source hierarchy in `knowledge/nah/AUDIT_RULES.md`. Relevant entries from
SIM92, COR88, SIM90, DEL70, MOC02, MOC03, MOC04, and MOC09 were reread from the
checkpoint files for this re-audit. Human review of this re-audit has not been
recorded.

## Mathematical assessment

### NAH-C001 -- Associated vector bundles and the flat connection

**Status: SUPPORTED.** Anchors: `SEC: NAH intro`, "associated vector-bundle
form," and `subsec:physical-interpretation-cusp-label`.

Support: `SIM92-THM-1`, `SIM92-COR-1.3`, `SIM92-METRIC-CONSTRUCTIONS`,
`SIM90-MAIN-THM`, `MOC04-THM-1.4`, `MOC04-PROP-5.2`, and `MOC09-THM-1.1`.

The manuscript restricts its punctured non-Abelian Hodge use to the associated
vector-bundle framework and states that the tame filtered/parabolic
correspondence requires the appropriate stability, degree, and regularity
conditions. This remains within the checked vector-bundle sources and does not
require the unresolved full punctured filtered principal-`G` category recorded
in `NAH-Q001`.

The statement that fixed global Higgs-bundle data, including puncture
structure, determine the associated flat connection up to gauge is supported
under the correspondence hypotheses. The manuscript also says the local tube
exponents are additional asymptotic flat-connection data and are not determined
by the complex-structure degeneration alone, so it does not overstate the NAH
input.

### NAH-C002 -- Logarithmic exponent and monodromy

**Status: SUPPORTED WITH CONVENTION.** Anchors: "Logarithmic singularities,"
`M_p=\exp(2\pi iR_p)`, `eq:monodromy`, and the tube formulas.

Support: direct horizontal-section calculation; `DEL70-DEF-1.14-1.17`,
`DEL70-PROP-3.11`, `SIM90-LEM-3.2`, and `SIM90-RESIDUE-TABLE`.

For the manuscript model `nabla=d-R dz/z`, the flat-section equation is
`ds/dz = R s/z`, so `s=z^R s_0` and positive continuation gives
`M=exp(2 pi i R)`. The manuscript fixes a logarithmic model and branch and
explicitly distinguishes this flat-connection exponent from the Higgs residue
alone.

**INTERNAL ONLY:** in Deligne's source convention the connection-matrix
residue `A` gives positive-loop monodromy `exp(-2 pi i A)`. The manuscript's
`R` is `-A`, so the formula agrees after translation. This is internal
bookkeeping and does not require a manuscript correction.

### NAH-C003 -- Growth and tube transfer

**Status: SUPPORTED.** Anchors: `eq:leading-flat-section-growth`,
`eq:generic-tube-transfer`, `eq:single-tube-factor-multivariable`, and their
class-S restatements.

Support: direct solution of the constant logarithmic model;
`SIM90-WEIGHT-NORM`, `MOC02-THM-9.3`, `MOC03-THM-13.1`, and
`MOC03-THM-13.2`.

For `R=alpha+e` with `[alpha,e]=0`, the local logarithmic model gives
`q^R=q^alpha exp(e log q)`, and nilpotence of `e` makes the logarithmic factor
a finite polynomial. The manuscript identifies this as the leading
logarithmic model and separately says rigorous flat-section growth for tame
harmonic bundles requires the standard hypotheses and Mochizuki/Simpson
asymptotic estimates.

The general tame estimates in the checkpoints are sectorial and require
compatible KMS/parabolic and monodromy-weight data, especially for fixed
nonzero `lambda`. The manuscript does not turn those estimates into an
unqualified exact global formula.

### NAH-C004 -- Filtered/parabolic growth data

**Status: SUPPORTED.** Anchor: "is encoded by a parabolic, or filtered,
extension."

Support: `SIM90-DEF-FILTERED-HIGGS`, `SIM90-DEF-FILTERED-LOCAL`,
`MOC03-DEF-2.1-2.3`, and `MOC09-LEM-6.1-6.4-COR-6.5`.

The manuscript correctly treats controlled tame growth as encoded by
filtered/parabolic extension data. It does not collapse the filtered object to
a single logarithmic exponent. This is consistent with the KMS comparisons,
where parabolic weights, residue eigenvalues, and monodromy eigenvalues remain
separate until translated by the source conventions.

### NAH-C005 -- Fiberwise tubes and normal-crossing residues

**Status: SUPPORTED.** Anchors: `sec:nah-asymptotics`, "base-coordinate loops
and the corresponding Dehn twists," and the paragraph following
`eq:ordered-multitube-singular`.

Support: the manuscript's fiberwise construction; `DEL70-DEF-3.8-PROP-3.10`,
`DEL70-THM-4.1-DEF-4.2`, and the contrasting compatibility results in
`MOC03-THM-12.2-COR-12.5-12.7-THM-12.3`.

The manuscript distinguishes commuting coordinate loops and commuting Dehn
twists in the degeneration base from non-Abelian matrices obtained by
evaluating the fiberwise representation on disjoint tube loops. Deligne's
commuting-residue theorem concerns one integrable logarithmic connection along
intersecting components of an SNC divisor; the manuscript explicitly contrasts
that geometry with disjoint fiberwise plumbing tubes. It does not assert a
noncommuting multivariable SNC residue system.

### NAH-C006 -- Regular matching between tubes

**Status: ASSUMPTION EXPLICIT.** Anchors: "We assume that the off-tube matching
matrices" and `eq:ordered-multitube-singular`.

Support boundary: `DEL70-THM-1.19-COR-1.20` and `MOC03-THM-13.2` provide local
regular-singular and sectorial information, not the global family regularity
of the off-tube matching matrices.

The manuscript explicitly assumes that the off-tube matrices `C_a(q)` remain
regular and invertible as `q -> 0`. The algebraic identity
`C q^R = q^{C R C^{-1}} C` correctly records the resulting conjugations. The
schematic singular product remains conditional on the stated assumption and
does not prove it for the class-S family.

### NAH-C007 -- External centralizer calculation

**Status: OUTSIDE NAH SCOPE.** Anchor: `eq:indexed-jordan-centralizer`.

The Jordan-centralizer formula and example tables require Lie-theory support
external to the NAH checkpoint corpus. This re-audit records that boundary and
does not independently certify the Lie-theory formula, nilpotent-orbit
classification, or centralizer tables.

### NAH-C008 -- Compatibility with independently specified weak gauging

**Status: PROPOSAL CLEARLY LABELED.** Anchors:
`eq:monodromy-gauge-full-stabilizer` and the paragraph beginning "We motivate
compatibility."

The NAH input is the associated flat connection and its tube monodromy. If a
generator is required to be a single-valued flat endomorphism of the tube local
system, it must satisfy `M_i X M_i^{-1}=X`. The manuscript presents the step
identifying weak-gauge generators with such monodromy-preserving symmetries as
a compatibility proposal, while stating that `h_i` is supplied independently
by fixture and gluing data.

NAH does not determine the weak gauge algebra, matter content, conformality
condition, or Lie-theory reductive quotient. The manuscript keeps these as
external physics/Lie-theory inputs.

### NAH-C009 -- Observables and future monodromy sensitivity

**Status: PROPOSAL CLEARLY LABELED at the NAH interface.** Anchors:
`subsec:physical-interpretation-cusp-label`, `eq:schematic-localization-cusp`,
"Monodromy-sensitive observables," and the matching conclusion/outlook item.

The leading localization estimate is presented under an explicit regular,
nonzero gluing-factor assumption and uses an independently specified weak
gauge algebra. The manuscript says the leading cusp metric only sees the
monodromy decoration through compatibility with this weak gauging, and it
leaves finer monodromy-sensitive observables to future investigation.

No NAH checkpoint certifies the localization calculation, sewing/AGT
interpretation, or metric normalization. The registered status only records
that the NAH contribution is not overstated.

## Physics-facing action list

No manuscript corrections are required within the assessed NAH scope.

## Supported claims and recorded boundaries

| Assessment | Claim IDs |
| --- | --- |
| Supported | `NAH-C001`, `NAH-C003`, `NAH-C004`, `NAH-C005` |
| Supported with internally matched convention | `NAH-C002` |
| Explicit model assumption | `NAH-C006` |
| Physical proposal clearly separated from NAH theorems | `NAH-C008`, `NAH-C009` |
| Outside NAH scope | `NAH-C007` |

All nine registered claim IDs are retained. The imported
`Class_S - 2026-09-15T131046.747.zip` source does not require new claim IDs for
the assessed NAH content. Existing `AI-PROPOSED` claim relationships remain
provisional; this re-audit does not promote any relationship.

## Technical validation

The active source recorded in `SOURCE.md` is `source/main.tex` from
`Class_S - 2026-09-15T131046.747.zip`, imported at
`2026-09-15T11:31:30+00:00`. The active `source/` directory contains six
files: `JHEP.bst`, `jheppub.sty`, `main.tex`, `references.bib`,
`sepnonsep.png`, and `torus.jpeg`.

During the import preceding the September 15 audit sequence, the selected ZIP
was checked for unsafe paths and symlinks, then the active `source/` tree was
verified byte-for-byte against the ZIP for all six files. The temporary import
extraction and backup folder was then removed.

For this re-audit, all nine ledger anchors were found in the active manuscript.
The cited checkpoint IDs resolve in `knowledge/nah/THEOREM_LEDGER.md` and the
corresponding source checkpoint files. `source/main.tex` declares
`\bibliographystyle{jhep}` and `\bibliography{references}`. No LaTeX build was
run as part of this re-audit.

The claim ledger already recorded all nine assessed claims with last audit date
`2026-09-15` and audited source `source/main.tex (Class_S -
2026-09-15T131046.747.zip)`. The claim network was regenerated with
`python3 ../nah-audit/scripts/generate_claim_network.py --project .`. The
script wrote `reports/CLAIM_NETWORK.svg` with all 9 registered claims and all
7 registered relationships. The two `AI-PROPOSED` relationships remain
provisional dashed edges.

## Scope limits

This re-audit evaluates the registered NAH claims against the existing
primary-source checkpoints, with explicit model calculations and assumptions
distinguished from theorem consequences. It is not a full verification of the
paper's physics, originality, Lie-theory calculations, geometric examples,
localization results, or every statement in the manuscript.
