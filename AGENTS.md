# Working on AI Dev Harness

This is an agent-readable setup repository, not an executable installer. Product
requirements are in `docs/product-requirements.md`.

- For installation into another repository, follow `INSTALL.md` and keep source
  and target paths distinct. Developing the harness does not install it here.
- Keep repository content in English. Match the user's conversation language.
- Keep Superpowers as the required ordinary-development foundation; do not build
  a competing production workflow or harness CLI. Reuse existing Superpowers global
  enablement unchanged and still explicitly enable the same ID in the project;
  distinguish native installation, cache storage and activation scope.
- Keep custom/personal skill installation generic; each skill defines its own behavior.
- Maintain catalogs against primary upstream documentation, including selection,
  compatibility, scope, task-time usage rules, and a meaningful verification probe.
- Render a concise usage rule for every available installed skill into the managed
  project instructions. Community skills and MCP integrations are selected by their
  own task/context rules, independently of the active workflow.
- During installation/addition/update/repair/verification in a target project,
  check only the AI environment. Do not run the target's tests, builds, lint/type
  checks, scans, migrations or app startup commands without a separate explicit request.
- For maintenance of this harness repository, follow `docs/acceptance.md` for
  appropriate source checks. Never label static checks as live client verification.
- Preserve normal platform and repository permissions; no additional blanket Git
  commit or push restrictions are introduced here.
