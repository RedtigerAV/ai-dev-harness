# Skill selection during work

The registry serves two decisions: `recommend_for` helps the user select components
during installation; `usage` tells the agent when an installed skill applies to a
task. Neither installs or invokes anything by itself.

## Registry fields

Each skill entry has a `usage` mapping:

| Field | Meaning |
| --- | --- |
| `role` | `workflow`, `domain`, or `diagnostic`; the kind of capability provided |
| `contexts` | Technologies or task contexts to match against the actual project/request |
| `when` | Concrete tasks or user intents that call for the skill |
| `when_not` | Meaningful exclusions; use an empty list when none apply |
| `instruction` | A short when-to-use rule suitable for project instructions |

Contexts are extensible catalog metadata, not a fixed harness technology list.
For collection entries, these fields describe the selection boundary; installation
must resolve each selected member's own triggers and real invocation name.

The installed skill's description and instructions define its detailed behavior.
Keep its registry summary aligned with them. A summary must not grant broader
permissions, silently change modes, or override the user's explicit exclusions.
Keep community skill and MCP entries self-contained: describe their own capabilities,
triggers and technical requirements without mentioning other skills or workflows.
Their applicability does not depend on whether Superpowers is installed or used.

## Render into project instructions

For each selected, confirmed available skill, place a short rule in the managed
**AI DEV HARNESS** section of the effective `AGENTS.md` for Codex and/or `CLAUDE.md`
for Claude Code. Include actual name, purpose, triggering task/context, project
scope and relevant exclusions. Use `usage.instruction`; resolve selected collection
members from their own upstream metadata. Do not list only names or describe only
installation recommendations. Use the same process for custom and community skills.

Record resolved member usage summaries in component records so later additions or
updates can compare them without guessing. On update, recheck the installed skill
and preview changes to routing rules like other managed instruction changes.

## Apply during tasks

The project block should direct the agent to identify the target path, technology,
version and task before relevant work, check exclusions and available skills, and
load matching skills. Community skills and MCP integrations apply according to
their own task/context rules, including when Superpowers is excluded or unavailable.
The harness's foundation requirement concerns installation completeness; it is not
a prerequisite for using an individual community skill or MCP integration. A
diagnostic skill applies when its checks help the requested work, not on every edit.

Pass selected skills, target context and exclusions into delegated work when used.
Keep choices proportional to the task. Missing expected skills should be reported
and offered for restoration; do not pretend their guidance ran.

## Verify routing

Check that every available selected skill/member has a rule in each effective
instruction source. Then use a no-write task proposal for a relevant project and
inspect whether the agent selects the expected skills. Repeat with Superpowers
excluded to check that relevant community skills remain applicable. Also try an
unrelated task or an explicit exclusion of the skill itself. Merely reading
registry YAML does not prove either native discovery or actual invocation.

Instructions improve the likelihood of appropriate selection; the client and agent
still execute them. Report what was observed rather than promising automatic use
on every future task.
