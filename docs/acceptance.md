# Acceptance and validation

These are repeatable acceptance cases for maintainers. Use disposable target
repositories and the actual requested client. Preserve the initial file bytes and
Git status. Do not install optional/global components without the test user's
selection. Never use a production service write as a connectivity probe.

## Static checks

Run `python3 scripts/check_repository.py` with PyYAML available. It checks metadata,
unique catalog IDs/YAML keys, the uninstalled record template, local links and
self-contained skill references. Use the platform's skill validator if available.
Parse JSON/TOML configuration examples and inspect rendered templates without
secrets. These checks do not prove agent behavior or service readiness.

## Installation and lifecycle cases

| Case | Fixture and request | Observable acceptance |
| --- | --- | --- |
| Empty project | Git repo containing only README; install from URL | Reads INSTALL.md; shows full catalogs; asks selections/future stack; creates no app; no optional installs before selection. |
| Existing project | Technology manifest, resolved-version evidence, team AGENTS.md | Recommends matching catalog entries; preserves instructions; checks compatibility without upgrades. |
| Mixed independent projects | A UI, service and library using different technologies; separate manifests/lockfiles and sparse root metadata | Finds all projects; one root harness; per-project versions/paths; guidance and connections stay scoped correctly. |
| Existing tools | Figma plugin and same-named community skill present | Checks identity/capability, adopts equivalent tools as external; asks about source conflict; avoids duplicates. |
| Repeat | Install twice with unchanged selections | No duplicate blocks/skills/MCP entries; no unrelated changes or reinstall; respects declined choices. |
| Instruction conflicts | CRLF file, team text, malformed/duplicate markers, locally edited managed block | Non-harness bytes preserved; ambiguous markers and local modifications cause a merge proposal, not deletion. |
| Both clients | Existing CLAUDE.md imports AGENTS.md; select both clients | Avoids duplicate effective block; copies skill to native directories; separate readiness observations. |
| Optional selection | Decline design/browser tools; choose one collection member | Installs only selection/resources; no full collection, deployment workflow or runtime dependency upgrade. |
| Add later | A new technology/project and previously declined matching tools; request one member | Installs only the requested addition, renders its usage rule, and preserves other versions/choices. |
| Update | Old source revisions, locally edited skill, native plugin updates | Compares actual versions; preview and approval; preserves customizations; records applied/retained revisions if partial. |
| Second computer | Copy repo/record but no auth, runtime or user plugin | Treats old evidence as historical; explains exact local steps; no secret/path copying or false readiness. |
| Missing Superpowers | Native install unavailable or agreed scope not achieved | Other selected work may proceed; overall result partial; no ready claim from source/marketplace/config alone. |
| MCP failure | Configured but unauthorized server or failed connector startup | Distinguishes config/auth/connector health; redacted useful error; exact retry; no ready claim from config alone. |
| Stopped application | Connector initializes and responds, but no target app is running | Records verified AI connector capability and untested app diagnostics; does not start/build/test the application or block setup on unrequested product checks. |
| Installation boundary | Target has test/build scripts and a diagnostic skill is selected | Reads configuration and verifies installed tools without running product tests, builds, scans or startup commands; generic workflow checklists do not expand setup scope. |
| Global suggestion | Optional setting offered then declined | Leaves user config unchanged; explains side effects/experimental status; unrelated work continues. |
| Restricted access | Harness URL inaccessible or client unavailable | Offers local source fallback; accurately reports unperformed client checks. |

For live MCP cases use the corresponding catalog probe and verify its target
project/file, runtime and authentication scope. Use an approved test resource or
isolated browser where needed. Record actual versions and results. Check only the
AI environment; do not run the target's tests, builds, scans, migrations or application
startup commands. A stopped app leaves app diagnostics untested, not an otherwise
healthy connector's installation failed.

## Development and learning cases

| Case | Request | Observable acceptance |
| --- | --- | --- |
| Standard work | Feature in a project with a matching installed domain skill | Agent selects the domain skill from its own task/context rule, including when Superpowers is excluded; conventions preserved. |
| Explicit exclusion | Two-line fix without Superpowers/browser tools | Exclusions passed through any delegation; no harness enforcement engine; proportionate work. |
| Trivial learning | Clamp utility; approve finite input contract and minimal scaffold | Brief agreement; no agent fleet; runnable tests fail because stub is unimplemented, not broken imports. |
| Meaningful learning | Paginated data reader exercise in the target language | Complexity discussion; allowed Superpowers design/planning only; public contract and preparation approval; scaffold/TODO/tests then stop. |
| Standalone fallback | Missing Superpowers | Offers restore/fallback; waits for explicit fallback choice; small-task exemption does not imply consent. |
| Boundary audit | Inspect all exercise output | No core logic in sources, comments, fixtures, helpers or plan; no private internals imposed by tests. |
| Assistance levels | Request no hints, a small hint, pseudocode, then full solution | Honors each requested level; full code appears in the response only; file edits require a separate explicit request. |
| Review | Ask to review learner implementation | Tests and prioritized explanations; no auto-fix; no invented requirements; conceptual consolidation. |
| Resume | Reopen an exercise after learner edits | Reconstructs phase/contract/approval; preserves work; does not reset scaffold or restart implementation. |

## Routing and extensibility cases

- For an available installed domain skill, inspect its `usage` mapping and rendered
  AGENTS.md/CLAUDE.md rule. Request a relevant no-write task proposal through
  Superpowers and observe that the domain skill is selected too. Repeat with
  Superpowers excluded: the domain skill should still apply. Try an unrelated task
  and exclusion of the domain skill itself; do not force irrelevant activation.
- In a disposable source fixture, add a second custom skill with a different name
  and a supporting resource, plus its catalog path/usage. Confirm the generic setup
  instructions cover copying, resource checks, discovery and rendering a rule
  without installer/template edits for that name.
- Reuse an existing globally enabled Superpowers plugin: user enablement stays true,
  while the same actual plugin ID gets explicit project enablement. Repeat for an
  existing user-disabled copy and verify that its user setting stays false.
- For a new plugin with no prior user choice, require an actual native receipt,
  final user-disabled/project-enabled state and native entry loading; an unrelated
  project must not gain activation. Preview all user-config writes before installing.
- A source-only marketplace with `installed: false` stays pending even if its
  project flag is true. Manual skill copying is offered only as a distinct chosen
  fallback, not silently substituted for the native plugin.
- For the catalog's new-app skill, verify discovery/proposal only during setup;
  scaffolding is triggered by a separate user request to create an application.

## Requirements coverage

| Product requirements | Implementation |
| --- | --- |
| Sections 1–5: vision, platforms, agent installation | README, INSTALL, docs/platforms |
| Section 6: foundation and exclusions | Catalog foundation, INSTALL, instruction template, learning boundary |
| Sections 7–9: learning and all five roles | Portable skill and its role/example references |
| Sections 10–12: catalogs, project detection and usage | Both registries, INSTALL, docs/skill-usage |
| Sections 13–15: safe instructions, record, settings | INSTALL merge procedure, templates, record format, platform guide |
| Sections 16–18: lifecycle and verification | LIFECYCLE, VERIFY |
| Sections 19–24: scenarios and public acceptance | README, this acceptance matrix, validation report |

Implementation coverage is not a claim that every case has been exercised in a
real client. Record performed checks and limitations in [validation.md](validation.md).
