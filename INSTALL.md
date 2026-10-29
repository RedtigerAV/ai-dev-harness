# Install AI Dev Harness

For the existing Codex or Claude Code agent. Use native tools, ordinary file edits,
and documented upstream installers. No harness runtime is needed. For an existing
installation, use [LIFECYCLE.md](LIFECYCLE.md).

## 1. Establish source, target, and platform

Read this file, [platform guidance](docs/platforms.md), both catalogs
([skills](registry/skills.yaml), [MCP](registry/mcp.yaml)), and [verification](VERIFY.md).
Resolve relative links against the harness source, not the target project.
Use a checkout or fetch files at one resolved harness commit so the source does
not change midway. Record that commit; if unavailable, say so rather than inventing it.

Identify the active client, supported features, target repository root, and current
working directory. Ask only if the target or requested platforms cannot be inferred.
Configure the active platform by default; configuring both is a user choice. An
unavailable second client can be configured, but cannot be marked ready.

If source access is blocked, explain the failure and offer a local source checkout
or the relevant files. Do not run guessed setup commands.

## 2. Inspect before recommending

Read root and applicable nested instructions, including overrides and imports.
Inspect Git status and identify pre-existing edits so installation does not absorb
or undo them. Inspect relevant configuration without printing credential stores.

Use `rg --files --hidden` excluding `.git`, `node_modules`, generated build output,
vendored dependencies, and caches. Discover relevant manifests, workspace/build
configuration, lockfiles and tests across applications, services and libraries.
Use detected technologies and the catalog's recommendation/usage metadata to decide
which evidence to inspect; do not depend on a fixed list of manifest filenames or
assume the root manifest describes the entire repository. Include relevant ignored
projects if the layout points to them; avoid unrelated checkouts.

Produce a compact map: project path, languages/frameworks, declared/resolved versions,
dependency/build tooling, test commands and applicable instructions. Declared ranges
remain ranges; resolved versions require lockfiles or installed dependencies.
Resolve shared dependencies for consuming projects. Do not fabricate recommendations
for technologies absent from the catalog or change product dependencies during setup.

Check `.ai-harness/installation.yaml`, native skill directories, plugin inventories,
and MCP configuration/available tools. Identify components by source and capability
as well as name: an existing Figma plugin may satisfy Figma MCP. Adopt matching
components as externally owned instead of reinstalling them.

## 3. Check the required foundation

Inspect native installation, source identity and existing user/project enablement
separately. Follow [native installation and project activation](docs/superpowers.md),
including its before/after scope table. Reuse matching installed Superpowers rather
than duplicating it under another marketplace ID.

Preserve pre-existing global enablement. Even when it is already globally enabled,
explicitly enable the same plugin ID in the project config. For a new install with
no prior user choice, complete the native package installation and make its final
activation project-only. Preview and obtain consent for user-config changes made
by the native installer or the required default-false setting; never disable an
existing global installation as a shortcut. Use explicit project scope in Claude.

Copying source, declaring a marketplace and setting an enabled flag are not a native
installation. If install/reload/permission actions remain, give exact supported next
steps, record `requires_manual_action`, and continue independent selected setup.
Refusal or failure leaves the foundation incomplete; do not claim that reloading
alone installed the package or silently switch to a manually copied skill collection.

## 4. Select skills, then MCP integrations

Show the foundation separately. For each optional recommendation show name,
description, app paths, source, installation form/caveat, and observed status.
Label recommended versus optional explicitly. Offer the full catalog; in an empty
project show all entries immediately and let the user choose a future stack or
defer it. Do not create a starter app.

For collections, enumerate current member names/descriptions and ask for a subset.
A collection name is not permission to install every member. Check supporting
resources before selecting isolated collection skills.

Obtain the skill selection, then present MCP options similarly. Honor explicit
choices already made. Present one concise preview: components, target files,
scopes, prerequisites, and manual actions. If that exact scope was already approved,
proceed without another confirmation. Keep global changes separate; declining them
must not cancel unrelated local work.

## 5. Install the agreed components

- Recheck the catalog's upstream route. Prefer project-local skills and MCP config.
  Avoid whole collections, unrelated plugins, and unselected clients.
- For every selected custom/personal skill, resolve its `install.path` from the
  catalog at the chosen harness revision. Copy the **whole skill directory**, including
  references, scripts, assets and metadata, into the platform's project skill directory.
  Inspect its own instructions for dependencies; do not execute its workflow merely
  to install it. Avoid links to temporary downloads or another computer's paths.
  For both clients, track two complete copies at the same source revision. Apply the
  same procedure to future custom skills without adding name-specific installer rules.
- Install community skills via supported upstream distributions or the skills tool
  with explicit member and agent selection. Inspect current help/scope first. When
  copying is supported, preserve required resources and notices. Missing collection
  dependencies leave a component pending, not ready.
- Reuse existing matching installs. Same name with different source, local edits,
  or a conflicting endpoint requires user resolution.
- Merge only selected MCP entries into native config. Associate processes with the
  correct app directory. Reuse an equivalent connected plugin when appropriate.
- Check prerequisites without upgrading app dependencies. Explain missing runtimes
  and record any necessary manual action.
- Use native authentication or environment references. Never put tokens in shared
  config, the record, chat, or diagnostics.

Prefer pinned compatible package versions/revisions and record the resolution.
Examples using `@latest` are discovery examples: resolve a version during setup to
avoid upgrades on every server start. Record platform-controlled update policies
where pinning is unsupported. Do not add MCP dependencies to the application.

Check optional capabilities using [the platform guide](docs/platforms.md). Recommend
useful settings; never silently enable experiments or bypass permissions.

## 6. Merge project instructions safely

Render [the instruction template](templates/project-instructions.md) from actual
observations, per platform, following [skill routing](docs/skill-usage.md). For **every
available selected skill**, custom or community, include its real invocation name,
brief purpose, when to use it, meaningful exclusions and relevant project paths.
Use the catalog's `usage.instruction` as the concise starting point and confirm it
against the installed skill's description. For collection members, derive a specific
rule from each selected member, not one vague rule for the collection.

Write these rules into the managed `AGENTS.md` section for Codex and `CLAUDE.md`
section for Claude Code. Tell the agent to load skills matching the task and context
independently of the active workflow. Community skill/MCP rules must describe their
own purpose and requirements without references to other skills or workflows.
Include every selected MCP with its state and scope. Explain pending skills
separately and state when Superpowers is missing.
Keep each skill's detailed workflow in that skill; do not duplicate it in the template.

Manage exactly this pair of whole-line markers:

```text
<!-- AI DEV HARNESS:BEGIN -->
<!-- AI DEV HARNESS:END -->
```

For each effective target instruction file:

1. Save original bytes or a recoverable local diff; note whether the file existed.
2. No markers or ambiguous old section: append a section, or create the file.
   Preserve original bytes, including line endings.
3. Exactly one correctly ordered pair: compare with the recorded baseline, then
   replace only the enclosed block. Preserve the prefix/suffix byte for byte.
4. Duplicate, nested, missing, or reversed markers, an unmarked old harness section,
   or user edits inside the managed block: show the conflict and ask how to reconcile.
   Never delete or normalize surrounding content.
5. Review the diff and verify one section and unchanged non-harness content.

Use `AGENTS.md` for Codex and `CLAUDE.md` for Claude Code as effective entry points;
inspect overrides/imports first. Do not append to an ignored file or duplicate a
section already imported from another file. Propose the smallest effective change
if layering conflicts. Nested team rules remain in force. Shared root guidance
uses app paths instead of duplicating the harness per application.

## 7. Record, verify, and hand off

Create or merge `.ai-harness/installation.yaml` using
[the record template](templates/installation-record.yaml) and
[record semantics](docs/record-format.md). Preserve unknown fields and unrelated
component records. Save partial progress and failures. Template examples are not
discoveries.

Run [VERIFY.md](VERIFY.md). Update evidence, states, and instruction descriptions
from the results, then check consistency. Report:

- **Complete** or **partially installed** for each requested platform.
- Ready, pending, and failed components, with evidence and exact next actions.
- Changed and preserved files, app associations, approved user-level changes.
- A short development prompt and invocation examples for selected skills.

Completion requires a ready foundation and selected capabilities, accurate
instructions/record, and preservation checks. Declined optional components do not
prevent completion. Never report future restarts or checks as already performed.
