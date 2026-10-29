# Design and customization

The product is the agent-readable installation contract, curated registries and
custom skills. Native platforms own execution, discovery, permissions, plugins and
MCP. The harness works across development technologies and does not depend on an
operating system or IDE; individual integrations may have runtime requirements.

## File responsibilities

- `README.md` is the public entry point; `AGENTS.md` / `CLAUDE.md` guide maintainers.
- `INSTALL.md` owns selection, installation and safe instruction merging.
- `LIFECYCLE.md` covers reconciliation/update/recovery; `VERIFY.md` owns readiness.
- `registry/*.yaml` holds curated sources, recommendations, usage rules and probes.
- `docs/skill-usage.md` explains task-time routing and concise project rules.
- `templates/` and `docs/record-format.md` define portable project handoffs.
- `skills/<name>/` holds each independently deployable custom skill and its resources.

## Extend a catalog

Add a stable kebab-case ID and concise English name/description. Include required
status, recommendation contexts, primary upstream URL, installation method and
selection boundary, scope, prerequisites, compatibility/authentication caveats,
and a non-destructive readiness probe. Check the upstream itself and date the review.

For every skill, add `usage.role`, `contexts`, `when`, `when_not` and `instruction`
as defined in [skill routing](skill-usage.md). Recommendations help choose what to
install; usage rules define when installed tools apply. New technology contexts
do not require changing the installer or adding a fixed technology allowlist.

For collections, offer individual members, resolve their own usage rules, and check
shared resources. For a tool-backed skill, distinguish tool installation from skill
discovery. Keep community skill/MCP descriptions and usage rules self-contained,
without references to other skills or workflows. Their applicability is independent
of Superpowers. Keep each skill's detailed behavior in that skill.
Preserve upstream licenses/notices when copying required resources.

## Add a custom/personal skill

Create `skills/<name>/SKILL.md` with YAML `name` and `description`, concise behavior,
and only needed supporting resources. Keep relative references inside that skill's
directory so a complete copy works on both clients. Its own definition describes
scope, modes, required approvals, dependencies and stopping behavior. Update the
registry's short usage summary to match it.

Every custom skill follows INSTALL.md's same complete-directory copy, discovery,
resource verification and update process. Avoid installer branches or template
placeholders keyed to a specific skill name. No special client metadata is required
for the portable baseline. Discovery of a skill does not itself authorize file edits.

## Validate changes

Follow [acceptance scenarios](acceptance.md). The maintainer check
`python3 scripts/check_repository.py` requires PyYAML and checks catalogs, usage
metadata, identities, local links and portable custom skill references. It does not
configure target projects. Keep development dependencies in an isolated environment.
Validate revised skills with the platform's skill validator when available.

Behavioral acceptance needs real client sessions: check that rendered project rules
select appropriate installed skills independently of the active workflow, respect
exclusions and do not copy a skill's full workflow into general instructions. Record results
and outstanding live checks in the validation report.
