# Verify and troubleshoot an installation

Verify on the actual computer, in each requested client, from the intended project.
Do not install missing components during a read-only verification request. Report
findings and offer the documented repair route.

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
   choose a no-write discovery check appropriate to it. For tool-backed skills,
   check both skill discovery and the tool as specified by the catalog.
3. **MCP:** parse native config, connect, authenticate if required, enumerate the
   actual available capabilities, then perform the catalog's harmless probe. Record
   the tool/result summary and app path. Never make external writes just to test
   connectivity. When tools are unavailable until restart, say so and defer the probe.
4. **Routing:** compare detected project scopes with connector responses. A connector
   starting does not prove its target application is reachable. Check that every
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

Call the setup **complete** only if the required foundation and all selected
capabilities are ready in that context, and instructions/record/preservation checks
passed. Otherwise say **partially installed**. A declined optional tool is not a
failure. Distinguish a connector-only success from untested app/file access.

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
| Next.js connector has no app | Check app version, running dev command, path, port, and endpoint support. Do not silently start migrations or upgrade Next.js. |
| Browser cannot launch | Check supported browser, installation and sandbox permissions; use an isolated profile. Do not weaken system security settings. |
| Duplicate MCP/skill | Compare sources, endpoints, scopes, and plugin-provided capabilities; adopt one existing equivalent. Ask before replacing conflicts. |
| Managed block is malformed or edited | Preserve it and present a merge proposal. Never guess which duplicated block to delete. |
| Collection skill has broken references | Retrieve required upstream resources/notices at the same revision or leave it pending. |
| Update only partly succeeded | Keep actual applied and retained revisions. Retry only the failed component after resolving its cause. |
| Previous computer was ready, this one is not | Recheck runtime, local paths, authentication and trust; previous evidence is historical. |

Preserve useful error summaries with secrets, sensitive URLs, and private payloads
redacted. After a failed retry, investigate the cause or request the necessary
action; do not repeat the same failing command indefinitely.
