# Class S non-Abelian Hodge audit companion

Author: Amineh Mohseni

This companion uses AI to check mathematical claims involving non-Abelian
Hodge (NAH) theory in the accompanying draft against the mathematics papers
used as sources.

- **Permanent checkpoints.** Definitions and results are recorded from primary
  PDFs with exact references, full hypotheses, conclusions, conventions,
  dependencies, and limitations. Audits reuse these checkpoints across draft
  revisions; substantive checkpoint updates are dated and explained.
- **Mathematical completeness and physics-facing reporting.** The full
  mathematical assessment checks hypotheses, conventions, applicability, and
  implications. A separate physics-facing action list gives only material
  corrections, preserving the manuscript's physical motivation, notation, and
  style. Simplifying the presentation never weakens the mathematical
  assessment; harmless convention differences and optional formal refinements
  remain internal.
- **Complete claim map.** Every registered claim appears with its type,
  status, audit date, and audited source. Solid arrows record manuscript-explicit
  or author-confirmed relationships; dashed arrows remain AI-proposed. The map
  is a navigation aid, not mathematical evidence.
- **Approval for each repair.** `Edit` presents one smallest sufficient
  correction at a time and applies it only after human approval.

## Use

In terminal Codex, use this companion’s `project/` directory as the working folder.
 Send `Import source …`, `Audit`, and `Map` as messages inside the Codex 
 conversation, not at the shell prompt.


In chat, attach the manuscript ZIP and send:

```text
Import source relevant_NAH_manuscript.zip
```

In terminal Codex, open this companion's `project/` directory and use a local
path:

```text
Import source ".../relevant_NAH_manuscript.zip"
```
Replace the example filename or path with your own, and send the command 
as a message to the assistant, not at the shell prompt.

 Only `Import source` imports a manuscript:
it unpacks into `project/source/` and updates `project/SOURCE.md`. Later
imports replace only `source/`, preserving checkpoints and audit history.

Importing does not run an audit. Send `Audit` to check the draft's registered
NAH claims without editing, then `Map` to generate the network. Use `Edit`
for proposed corrections.

After Audit and Map finish, their outputs and updated claim records are saved in project/.
No further command is needed.

## Contents and requirements

- `project/`: manuscript, source references, checkpoints, claim records, and audits.
- `nah-audit/`: reusable workflow instructions and the map generator.

See `project/PROJECT_GUIDE.md` for the file tour and full command list.
The source papers, authors, and versions are listed in
`project/papers/nah/SOURCE_MANIFEST.md`.

The companion produces dated audit reports and a visual claim map. 
Reports include the full mathematical assessment, concise physics-facing findings, 
and a record of the checks performed. The manuscript can also be compiled into a PDF.

