<!-- AI DEV HARNESS:BEGIN -->
## AI DEV HARNESS

For ordinary project work, follow the applicable project instructions and use the
skills and integrations relevant to the task. Consult the guides in the AI Dev
Harness source repository only when the task concerns AI Dev Harness itself.

- To install AI Dev Harness, start with [INSTALL.md](https://github.com/RedtigerAV/ai-dev-harness/blob/main/INSTALL.md).
- To update or repair AI Dev Harness, or add or remove its skills or MCP
  integrations, start with [LIFECYCLE.md](https://github.com/RedtigerAV/ai-dev-harness/blob/main/LIFECYCLE.md).
- To verify or troubleshoot an AI Dev Harness installation, start with [VERIFY.md](https://github.com/RedtigerAV/ai-dev-harness/blob/main/VERIFY.md).

Follow only the references needed for the requested operation.

Source: {{harness_source_url}} at {{harness_revision}}.
Project choices and observations: `.ai-dev-harness/installation.yaml`.

- Standard development: {{superpowers_actual_state_and_invocation}}. Superpowers
  provides the normal engineering process; matching domain skills supply expertise.
  If the expected foundation is unavailable, report it and offer restoration.
- Before relevant work, identify the target project and task, then load each
  available skill whose usage rule below matches. Select community skills and MCP
  integrations by their own task/context rules, independently of whether Superpowers
  is used. Follow each skill's own instructions and apply it only within its scope.
- Respect explicit user exclusions of Superpowers, any skill or MCP, including
  delegated work. Keep tasks proportionate where the active process permits it.
  These rules guide invocation subject to native platform behavior.

### Engineering Quality

- Write readable, maintainable code that can evolve and handle the expected workload.
- Follow established architectural boundaries and reuse patterns that fit the task.
  When conventions are missing or unclear, define the responsibilities and dependency
  direction of the affected code before implementing substantial changes.
- Use clear names, straightforward control flow, focused modules, and explicit
  dependencies. Keep business rules independent of transport and storage where
  that makes the rules easier to change and test.
- Choose the simplest design that meets current requirements. Add layers, interfaces,
  and abstractions only when they solve a concrete problem in scope.
- During review, check the diff for mixed responsibilities, duplicated business
  rules, unnecessary indirection, and changes to public contracts. Fix issues
  introduced by the change.

### Installed skills: when to use them

{{available_installed_skill_rules_with_real_names_purposes_triggers_and_project_scopes}}

### MCP integrations

{{selected_mcp_instances_with_states_purpose_and_project_scopes}}

{{pending_selected_components_and_next_actions}}

Harness lifecycle tasks check only the AI environment; project tests,
builds, scans and application startup require a separate explicit request.
Preserve surrounding project instructions. Global changes need explicit
consent. Existing team conventions and normal platform permissions still apply.
<!-- AI DEV HARNESS:END -->

---

Template rendering notes (do not copy these notes into the target):

- Replace all tokens with observations; omit inapplicable optional content.
- If using a different harness source, point the three guide links directly to its
  guide files using URLs or paths that resolve from the target instruction file.
- Include **one concise rule per available selected skill or collection member**:
  `actual-skill-name — purpose. Use when <task/context>; scope: <project paths>;
  do not use for <meaningful exclusion, if any>.` Reuse `usage.instruction`, confirm
  against that skill's own description, and adapt names/scopes without copying its
  detailed workflow. Treat custom and community skills identically here. Keep each
  community skill/MCP rule self-contained, without references to other skills or workflows.
- Apply the same rules in the effective AGENTS.md/CLAUDE.md source, considering
  imports. Do not create a second block if both clients share that source.
- Label pending skills and configured/unavailable MCPs accurately. Only available
  skills receive active usage instructions. Never advertise the entire catalog.
- The managed bytes run from the BEGIN marker through the END marker only.
