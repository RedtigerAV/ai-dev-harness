# Verify and troubleshoot an installation

Verify on the actual computer, in each requested client, from the intended project.
Do not install missing components during a read-only verification request. Report
findings and offer the documented repair route.

## Installation-only boundary

Apply this boundary to installation, component addition, update, repair and
verification of AI Dev Harness:

- Check the installed AI tools: native receipts/discovery, configuration, scopes,
  resources, tool runtimes, MCP startup/authentication and harmless connector calls.
  Also check managed instruction preservation and record accuracy.
- Read target manifests, lockfiles and declared scripts for context. Do not execute
  product tests, builds, lint/type checks, repository quality/security scans,
  benchmarks, migrations, dependency restore/repair or application startup commands.
  For example, `npm test`, `npm run build`, `dotnet test` and `dotnet build` are not
  installation checks. A non-mutating scan is still an application check.
- Start selected MCP processes as needed, but do not start an application or its
  supporting services to make a connector probe pass. If the app is already running,
  a minimal metadata read may confirm connector routing. Do not assess or repair
  application errors, execute browser test scenarios or run performance traces.
- Skill probes are discovery/proposal-only: explicitly pass this boundary so an
  invoked workflow does not continue into application testing or implementation.
  Installing a learning or diagnostic skill does not authorize using it on product code.
- Application validation is separate work, permitted only when the user explicitly
  requests it. A generic verification checklist does not authorize that expansion.

## Connector readiness versus application use

Scope `ready` to the AI capability actually checked. A connector that starts,
exposes the expected tools and responds to a harmless connector call can be ready
for installation even when no application is running. Record runtime/app-specific
operations as **not checked during installation**, not as a failed installation.
Do not claim the unperformed diagnostics worked. Missing connector runtime, failed
startup, required authentication or broken tool calls still require attention.

Target-project test/build results are not installation acceptance gates. A stopped
app or unrequested app diagnostics do not block completion once the selected AI
environment checks pass. Use the component's documented connector-level probe.

## Evidence and states

Use these states in [the installation record](docs/record-format.md):

| State | What it means |
| --- | --- |
| `requested` | Selected; no successful setup evidence yet |
| `configured` | Native configuration is present and parseable; connection unproven |
| `installed` | Skill files are copied or native package installation is confirmed; client loading/use unproven |
| `ready` | Required capability succeeded in the named client/context during this check |
| `requires_manual_action` | Known login, trust, restart, prerequisite, or user action remains |
| `failed` | An attempted operation/check failed; include stage and redacted summary |

States are observations, not a mandatory linear sequence. Keep `last_successful_stage`
and evidence so a pending login does not lose the fact that configuration succeeded.
Mark an old observation as historical when changing machines; never invent a fresh
success. `ready` is scoped to the verified capability, client, and app, not forever.

## Checks

1. **Foundation:** follow [installation and activation checks](docs/superpowers.md).
   Require an actual native receipt, exact plugin ID, effective project enablement
   and loaded skills/entry. Preserve pre-existing global enablement; new project-only
   activations must remain disabled outside the project. Verify any manual skill-copy
   fallback according to its distinct distribution; never call it an installed plugin.
   Source copies, marketplace availability and enabled flags alone are insufficient.
2. **Selected skills:** verify name/description and the complete resource directory;
   use native discovery and a no-write invocation where possible. Verify collection
   members individually. Use the skill's own instructions and catalog probe to
   choose a discovery/proposal-only check. For tool-backed skills, check executable
   availability with a supported help/version command and native discovery; do not
   scan, test or build the target project to verify the installation.
3. **MCP:** parse native config, connect, authenticate if required, enumerate the
   actual available capabilities, then perform the catalog's connector-level probe
   within the installation-only boundary. Record the result and any relevant routing
   path. Do not run application diagnostics or external writes to prove connectivity.
   When tools are unavailable until restart, say so and defer the probe.
4. **Routing:** compare detected project scopes with harmless connector metadata
   where available. Record application-specific access as untested if the app is not
   already running; do not start or validate it. Check that every
   available selected skill/member has a concise task/context rule in the effective
   project instructions, then use relevant no-write proposals to observe task-based
   skill selection, including with Superpowers excluded. Check unrelated tasks and
   explicit exclusions of the selected skill.
   Follow [skill routing](docs/skill-usage.md); record unperformed behavioral checks.
5. **Instructions:** ensure one valid managed block per effective instruction source,
   correct component names/states, and unchanged non-harness bytes compared with the
   saved before-image. Check nested overrides/imports from the actual app context.
6. **Record:** validate YAML, unique instance identities, revisions, ownership,
   selections, paths, states, and evidence. Resolve template placeholders. Check
   that no credential values or private diagnostic payloads were saved.
7. **Diff:** confirm no unexpected app dependency upgrades, source edits, or unrelated
   configuration changes. Save only accurate results, including partial failures.

Do not use the agent's ability to read `SKILL.md` directly as proof that the client
has discovered the installed skill. If a native test is unavailable, retain
`installed` or `configured` and describe the unperformed check.

## Final report

Give the overall result per platform and a concise table:

| Component / app | State | Evidence | Next action |
| --- | --- | --- | --- |
| Example selected MCP | requires_manual_action | Config parsed; no authenticated call | Log in via the client's MCP panel, then retry the catalog probe |

Call the setup **complete** only if the required foundation and selected AI
installation capabilities are ready in that context, and instructions/record/
preservation checks passed. Unrequested target-project validation is not a gate.
Otherwise say **partially installed**. A declined optional tool is not a failure. Distinguish a connector-only success from untested app/file access.

## Troubleshooting

| Symptom | Check and next step |
| --- | --- |
| Source URL unavailable | Report access failure; use a local checkout or supplied docs/catalogs at a known revision. |
| Superpowers source/config exists but no skills load | Follow `docs/superpowers.md`: check the real native install receipt, exact ID and activation scope; preserve existing global choices and keep setup partial until loading works. |
| Skill files exist but no skill appears | Check the client's effective project path, native directory, frontmatter, complete resources, same-name collisions, and reload/restart guidance. |
| MCP config exists but tools do not | Check parse errors, project trust, native enablement, runtime PATH, stderr, and restart requirements. A GUI app may inherit a different PATH. |
| Unauthorized / forbidden | Use the service's native login flow; check account/file access. Keep credentials out of diagnostics. A valid login is not file permission. |
| Node/Python/browser missing | Report the required runtime from upstream; provide the approved manual setup route. Do not upgrade app dependencies to fix tool runtime requirements. |
| Wrong Angular workspace | Check angular.json, launch directory/arguments, and returned project paths; separate instances if needed. |
| Connector has no running application | Verify connector startup, tools and harmless discovery; note app-specific operations are untested. Do not start/build the app or make its tests an installation gate. |
| Browser cannot launch | Check supported browser, installation and sandbox permissions; use an isolated profile. Do not weaken system security settings. |
| Duplicate MCP/skill | Compare sources, endpoints, scopes, and plugin-provided capabilities; adopt one existing equivalent. Ask before replacing conflicts. |
| Managed block is malformed or edited | Preserve it and present a merge proposal. Never guess which duplicated block to delete. |
| Collection skill has broken references | Retrieve required upstream resources/notices at the same revision or leave it pending. |
| Update only partly succeeded | Keep actual applied and retained revisions. Retry only the failed component after resolving its cause. |
| Previous computer was ready, this one is not | Recheck runtime, local paths, authentication and trust; previous evidence is historical. |

Preserve useful error summaries with secrets, sensitive URLs, and private payloads
redacted. After a failed retry, investigate the cause or request the necessary
action; do not repeat the same failing command indefinitely.
