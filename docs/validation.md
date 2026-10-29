# Implementation validation — 2026-10-29

## Performed

- Read the original product requirements before implementation; subsequent agreed revisions are maintained in product-requirements.md.
- Reviewed primary documentation for Codex, Claude Code, Superpowers, all required
  community sources, and the six MCP options. Links and review date are in the
  platform guide and catalogs. This is source research, not installation evidence.
- Validated `learning-dev-workflow` with the available skill-creator validator:
  **passed**. Required metadata is valid and no unfinished scaffold placeholders
  remain in the skill instructions.
- Copied the complete skill into disposable `.agents/skills` and `.claude/skills`
  layouts. All files remained byte-identical and internal links resolved in both.
- Parsed the TOML and JSON MCP examples. Both retained literal environment-variable
  references rather than embedded credentials.
- Executed the two JavaScript tests printed in the learning example using Node's
  test runner. Both collected successfully and failed at the intentional
  `Not implemented: clamp` stub. No import or syntax failure was observed.
- Exercised the documented managed-block replacement protocol on disposable byte
  fixtures: empty input, repeat application, CRLF/team-content preservation,
  malformed/duplicate/reversed/nested markers, and modified managed content.
  Expected preservation and conflict outcomes passed. This was a manual protocol
  exercise using temporary code, not a test of a shipped merger or agent compliance.
- Verified that the maintainer YAML loader rejects duplicate keys.

- Initial offline repository checker: **passed** for 9 skill/catalog entries,
  6 MCP entries, record template, skill metadata, and local Markdown links.
- Confirmed the initial requirements copy matched the supplied source before the
  subsequently requested cleanup and relocation; checked changes for whitespace errors.

## Agreed documentation and routing revision — 2026-10-29

- Relocated the requirements to `docs/product-requirements.md`, removed historical
  design references, and checked every local link. The revised file is intentionally
  different from the original requirements copy.
- Rechecked the official Angular skills page before adding `angular-new-app`.
- Ran the updated repository checker: **passed** for 10 skill entries, including
  task-time usage metadata, and 6 MCP entries. The revised learning skill also
  passed the skill-creator validator.
- In a disposable source fixture, added a second custom skill with a backend context
  and a reference file. Metadata validation passed without installer changes;
  complete copies preserved its resources in both native directory layouts.
- Negative fixtures with null, missing or empty usage metadata were rejected with
  useful validation errors rather than being treated as valid routing guidance.
- Rendered a disposable selected-skill rule into both AGENTS.md and CLAUDE.md from
  the template and registry metadata. The selected rule was present; unselected
  custom and new-app skills were absent. This tests the documented rendering
  contract, not live agent invocation.
- Confirmed generic setup no longer depends on a specific custom skill name and
  learning instructions/examples contain no Angular/React/Next.js references.
  Reviewed the four assistance levels: full code is disclosed in the response and
  file edits require a separate explicit request.
- Checked whitespace and confirmed edits remain unstaged on `main`, without
  creating a worktree, commit or push.

## Final repository review — 2026-10-29

Reviewed all 22 deliverable files against the current product requirements and the
agreed catalog, routing and assistance-level rules. No unresolved contradiction was
identified in the repository instructions after the corrections below. This is a
source review; the live acceptance cases remain unverified.

Corrections made during review:

- Allowed `usage.when_not: []` when a skill has no meaningful special exclusions.
  The template already allowed this; the validator previously rejected it. Invalid
  null/non-string exclusions still fail with a clear error.
- Added the documented `usage_instruction` field to the installation record
  template, left null until the skill rule is resolved.
- Aligned verification wording with independent community skill selection and
  improved line wrapping without changing the learning or installation scope.

Final checks passed for all 10 skill entries and 6 MCP entries, local links, skill
metadata, Python syntax, YAML/JSON/TOML examples and text hygiene. All community
entries remain free of cross-skill/workflow requirements. Complete learning-skill
copies preserve their resources in both native layouts. Both published example
tests load and fail only at the intentional unimplemented stub. Empty and invalid
exclusion-list fixtures produce the expected validator results.

All review edits were made directly on `main`; HEAD remained unchanged and staging
was empty. No worktree, commit or push was created during review.

## Superpowers installation correction — 2026-10-29
+
+A real installation exposed a missing step: a local source/marketplace and an
+enabled project flag were present, while native inventory still reported
+`installed: false` and no foundation skills loaded. The instructions now require
+native installation separately from activation and loaded-skill verification.
+
+The primary route remains the native plugin distribution. Existing global
+enablement is preserved, with the same actual plugin ID explicitly enabled in
+the project. A new installation without prior user preference ends user-disabled
+and project-enabled after preview/consent for any user-config writes. Claude uses
+explicit project scope. Shared caches are distinguished from activation scope.
+
+The Codex native CLI help and official installation/configuration documentation
+were inspected. YAML, local links and the new JSON/TOML examples passed checks.
+As research for the optional skill-copy fallback, Codex 0.165.0-alpha.1.2 native
+`skills/list` discovered all 15 enabled repo-scoped Superpowers 7.0.1 skills in a
+temporary target and none of those project copies in a separate context. The
+user config hash stayed unchanged. That probe did not install a plugin or invoke
+its workflow; it is not evidence of a completed native plugin installation.
+
+No target-project or user enablement was changed during this correction. Actual
+plugin installation, final per-context activation and entry invocation still need
+their documented live checks. Manual copying is only a separately selected fallback.
+
+## Not exercised in a live target client

No real target project's settings, plugins, or credentials were changed during
implementation. Native skill discovery in a fresh Codex/Claude session, marketplace
installation, MCP authentication and capability calls, and the full conversational
acceptance matrix remain live integration checks. Claude Code was not available
on PATH in the implementation environment. Availability of a Codex executable
alone does not validate desktop plugin installation or discovery.

The recorded fixture results do not prove that another agent will follow every
instruction. The learning boundary, exclusions and preservation rules remain
behavioral instructions under the platform's permissions.

Use [acceptance.md](acceptance.md) for release trials in disposable empty, existing,
and mixed-framework repositories on both platforms. Record actual versions,
selected components, capability results, failures and manual steps. Do not check
off live acceptance based solely on this implementation report.
