# Class S NAH audit project

## Active manuscript files

The active manuscript source root, TeX entrypoint, and bibliography
are recorded in `SOURCE.md`. See the README for instructions on
importing a revised manuscript.

No compiled manuscript is designated current in this directory. Generate a
fresh PDF from the active TeX entrypoint when needed; compiled and auxiliary
files are not part of the clean companion release.

## Audit architecture

The permanent workflow is:

```text
primary PDFs
  -> source checkpoints
  -> theorem ledger and audit rules
  -> manuscript claim ledger
  -> explicit claim relationships
  -> dated audit report
  -> all-claims map
  -> approved repair
```

The supporting files are:

- `papers/nah/SOURCE_MANIFEST.md`: primary-source identities and integrity
  hashes
- `knowledge/nah/sources/`: detailed source-specific checkpoints
- `knowledge/nah/THEOREM_LEDGER.md`: index of individual source results
- `knowledge/nah/AUDIT_RULES.md`: established cross-source conventions and
  audit boundaries
- `knowledge/nah/OPEN_QUESTIONS.md`: unresolved source or applicability gaps
- `knowledge/nah/CLAIM_LEDGER.md`: stable manuscript claim IDs and support
  status
- `knowledge/nah/CLAIM_RELATIONS.md`: explicit claim groups and claim-to-claim
  relationships
- `audits/ABOUT_AUDITS.md`: audit lifecycle and status index
- `audits/`: immutable dated audit reports
- `reports/CLAIM_NETWORK.svg`: generated all-claims network
- `../nah-audit/SKILL.md`: reusable audit instructions
- `../nah-audit/agents/openai.yaml`: skill display metadata
- `../nah-audit/scripts/generate_claim_network.py`: deterministic claim-network
  generator

## Built-in commands

The following one-line messages to the assistant are complete instructions;
no workflow prompt is needed. Use them in chat or in a Codex terminal session,
not directly at the shell prompt:

- `Import source <ZIP filename or path>`: extract the attached manuscript ZIP
  or the ZIP at the supplied local path into `source/` and update `SOURCE.md`.
  Importing does not run an audit.
- `Audit`: reread the source selected in `SOURCE.md` and audit every
  registered, in-scope claim against the permanent checkpoints. Record the
  audit date and manuscript source, keep the mathematical assessment separate
  from the physics-facing action list, and do not edit the manuscript.
- `Edit`: use the latest applicable audit of the selected source, or run
  `Audit` first if necessary.
  Present one `MUST CORRECT` or `SHOULD CLARIFY` change at a time with current
  wording, proposed wording, reason, and downstream effect. Ask for approval,
  apply only an approved change, validate, and then continue to the next item.
- `Claim`: update the claim ledger for the active manuscript or requested
  section and keep every claim registered in the relationship group table.
- `Map`: regenerate the color-coded network containing every registered claim.
  Reread the selected source and run `Claim` first if the ledger needs updating.
  Solid arrows are manuscript-explicit or author-confirmed;
  dashed arrows are AI-proposed. Isolated claims remain visible.
- `Re-audit`: create a new audit of the selected source after approved edits.

Only ask which manuscript or section to use when the target is genuinely
ambiguous. `INTERNAL ONLY` mathematical observations never enter the `Edit`
queue.

## Technical validation

After an approved change, check the affected files. Record the checks
actually performed in the `Technical validation` section of the next new
audit report under `audits/`.
