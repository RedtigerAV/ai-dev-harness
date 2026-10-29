<!-- AI DEV HARNESS:BEGIN -->
## AI DEV HARNESS

Source: {{harness_source_url}} at {{harness_revision}}.
Project choices and observations: `.ai-harness/installation.yaml`.

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

### Installed skills: when to use them

{{available_installed_skill_rules_with_real_names_purposes_triggers_and_project_scopes}}

### MCP integrations

{{selected_mcp_instances_with_states_purpose_and_project_scopes}}

{{pending_selected_components_and_next_actions}}
{{project_paths_technologies_and_version_sources}}

Install/add/update guidance: {{harness_source_url}} (INSTALL.md, LIFECYCLE.md,
VERIFY.md). Preserve surrounding project instructions. Global changes need explicit
consent. Existing team conventions and normal platform permissions still apply.
<!-- AI DEV HARNESS:END -->

---

Template rendering notes (do not copy these notes into the target):

- Replace all tokens with observations; omit inapplicable optional content.
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
- Keep the project map brief; detailed version/evidence data belongs in the record.
- The managed bytes run from the BEGIN marker through the END marker only.
