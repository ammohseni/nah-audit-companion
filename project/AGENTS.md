# Class S manuscript project

This file provides project-specific instructions to an AI agent working with
the manuscript; it does not create, launch, or connect to additional agents.

Read `SOURCE.md` for the active manuscript source root, TeX entrypoint,
and bibliography.

Import a manuscript source ZIP only when the user sends
`Import source <ZIP filename or path>` as a message to the assistant.
Use the attached ZIP in chat or the ZIP at the supplied local path in a
Codex terminal session. Extract it into `source/` and update `SOURCE.md`
with the original ZIP filename,
import time, source root, TeX entrypoint, and bibliography files. A later
import replaces only `source/`. Preserve the imported manuscript contents
and the permanent checkpoints and audit records.

For every `Import source`, including the first import:

1. Use a fresh, uniquely named temporary folder inside this project. Inspect
   the ZIP before extraction; reject escaping paths and symlinks. Do not delete
   an existing folder merely to reuse its name. Keep the original ZIP and retain
   the previous `source/` and `SOURCE.md` until the replacement is verified.
2. Identify the TeX entrypoint, install the new source, and update `SOURCE.md`.
   Verify the imported file list and contents against the selected ZIP, allowing
   only the deliberate removal of operating-system metadata or a wrapper
   directory. Check that the recorded source root, entrypoint, and bibliography
   point to the imported files. If verification fails, retain the recovery
   copies and restore the previous source and source note when safe.
3. Treat the import request as authorization for routine cleanup after these
   checks pass. Before deleting anything, resolve the exact paths and inspect
   their contents. Remove only temporary folders created for this import,
   including its backup of the previous source. Preserve the original ZIP,
   active source, and permanent project records. Leave unrelated or uncertain
   folders intact; do not ask the user to decide whether their contents are
   safe to delete. Perform verified cleanup automatically when the existing
   execution permissions allow it.
4. If execution permission is required, explain the proposed deletion in plain
   language immediately before requesting approval. Include the explanation in
   the tool's approval justification when that field is available. State:
   - the exact folder paths, what each contains, and why it is no longer needed;
   - the ZIP filename, active source location, and verification actually
     completed, with file counts where useful;
   - that approval permanently removes those temporary copies, including any
     backup of the previous draft, while keeping the verified new manuscript,
     original ZIP, checkpoints, and audit records;
   - that declining this cleanup leaves the completed import usable and keeps
     the temporary copies;
   - whether an offered approval applies only to this operation or creates a
     reusable permission rule. Explain its actual scope; do not imply that a
     rule for one timestamped path covers future paths.
   Ask the user to authorize the explained action, not to perform or judge
   the technical checks. Do not change permission settings or use another
   deletion method to bypass a required approval.
5. If cleanup is declined or blocked, retain the temporary folders and finish
   reporting the verified import; cleanup is not required to run `Audit` or
   `Map`. Briefly report the import result, checks performed, and whether
   cleanup was completed or left pending. Claim only checks actually performed.

Uploading a ZIP, placing it in a folder, or pasting manuscript text does
not trigger an import.
Importing selects the source and does not run an audit. `Audit` rereads
the source selected in `SOURCE.md`; it does not import files.

Do not treat a compiled PDF or a file under `archive/` as current unless
the user explicitly selects it.

Use the `nah-audit` skill. In this companion package its instructions are at
`../nah-audit/SKILL.md`, and its interface metadata is at
`../nah-audit/agents/openai.yaml`.

Treat bare `Audit`, `Edit`, `Claim`, `Map`, and `Re-audit` requests according to
the skill's default command routing. Do not ask the user to restate that
workflow. `Map` must include every registered claim, retain isolated claims,
and never promote an AI-proposed relationship to a confirmed dependency.
For `Edit`, approval one finding at a time is mandatory; never batch changes or
apply a second change before the first is approved, rejected, or deferred.

For an NAH audit, read the project in this order:

1. `knowledge/nah/AUDIT_RULES.md`
2. `papers/nah/SOURCE_MANIFEST.md`
3. `knowledge/nah/THEOREM_LEDGER.md`
4. relevant files under `knowledge/nah/sources/`
5. `knowledge/nah/OPEN_QUESTIONS.md`
6. `knowledge/nah/CLAIM_LEDGER.md`
7. `knowledge/nah/CLAIM_RELATIONS.md`
8. the selected portions of the manuscript identified in `SOURCE.md`

Every audit must reread the active manuscript selected in `SOURCE.md`
and record the audit date, manuscript source, and audited sections
or claim IDs.

After saving a new report for `Audit` or `Re-audit`, automatically update
the history table in `audits/ABOUT_AUDITS.md` with its filename and audit
date. Before reporting completion, check that every saved audit report
appears exactly once with the correct date, and add any missing entries.
Keep completed reports unchanged. No separate user command is required.

For review-only requests, do not edit the selected manuscript. For repair requests, make
only approved claim-level changes, preserve unrelated text and labels, update
the claim ledger and any affected claim relationships, regenerate the claim
network, and validate the manuscript afterward.

For every manuscript compilation and its cleanup:

1. Before compiling, record the files already present. Afterwards, identify
   exactly which files this run created; file extensions alone do not establish
   that a file is disposable. Preserve imported and pre-existing files, any PDF
   requested as an output, and logs still needed to diagnose a failed build.
2. Treat an authorized compilation as authorization for routine cleanup of its
   verified temporary files. Before deleting, resolve the exact paths and
   inspect the files. Save the compilation result and relevant diagnostics
   before cleanup; record checks actually performed under `Technical validation`
   in the next new audit report when applicable. Remove only confirmed temporary
   files created by this run, using explicit paths, automatically when the
   existing execution permissions allow it. If the build tool's cleanup fails,
   any fallback must meet the same verification and permission requirements.
3. If execution permission is required, explain the deletion in plain language
   immediately before the prompt and in the tool's approval justification when
   available. State the exact file paths, what the files contain, and how they
   were identified as temporary files from this run. Explicitly name any PDF
   that would be deleted and say that this removes the generated PDF, while
   keeping the manuscript source, bibliography, figures, style files, original
   ZIP, checkpoints, and audit records. Explain that declining keeps the
   generated files and does not undo the completed checks or prevent `Audit`
   or `Map`. Do not describe the deletion only as removing "build products."
   Explain the actual scope of one-time or reusable approval as for import
   cleanup; do not ask the user to perform or judge the technical checks.
4. If cleanup is declined or blocked, leave the files and finish reporting the
   work, including the actual compilation result and cleanup left pending.
   Cleanup is optional; its failure is not a mathematical finding. Do not
   change permission settings or switch deletion methods to bypass approval.

Keep the complete `Mathematical assessment` separate from the
`Physics-facing action list`. The latter contains only the smallest sufficient
changes for `MUST CORRECT` and `SHOULD CLARIFY` findings. Record `INTERNAL ONLY`
issues in the former and never use them to request a manuscript edit.

Do not repeat or summarize `INTERNAL ONLY` observations in the
`Physics-facing action list`, even to explain that they require no
correction. If there are no `MUST CORRECT` or `SHOULD CLARIFY` findings,
write only: "No manuscript corrections are required within the assessed
NAH scope."

Before saving a new report, check that this section contains only
actionable findings or the sentence above. Preserve all useful internal
observations in the `Mathematical assessment`.

Keep source theorems, cross-source audit rules, unresolved questions,
manuscript claims, and dated audit reports in their designated files. Do not
use one file as a substitute for another.
