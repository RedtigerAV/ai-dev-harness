# Install and activate Superpowers for a project

Use the native plugin distribution. Registering a marketplace, copying its source
or setting `enabled = true` does not establish that the package was installed.
Check the install receipt and native skill loading separately from enablement.
Use [installation-only verification](../VERIFY.md): entry probes must not continue
into the target project's tests, builds, diagnostic scans or implementation.

Project setup must preserve existing user choices. **An already installed and
globally enabled Superpowers plugin stays globally enabled.** Reuse its actual
plugin ID and explicitly enable that same ID for the target project. Do not disable
it for other repositories, create a duplicate marketplace/plugin identity, or
reinstall it just to add a project setting.

## Codex

Codex supports project overrides for local-marketplace plugins in trusted projects;
see [plugin installation and configuration](https://developers.openai.com/plugins/build/plugins).
Its native package cache is shared. Cache storage and activation scope are distinct:
the requested project setup does not require placing every package file in the repo.
Workspace-managed plugins can have different enforced rules; do not claim local
overrides control those plugins without checking the active client's policy.

### 1. Inspect and preview

Inspect native plugin inventory, effective configuration and its user/project
sources before changing anything. Check source identity, installation state,
version, actual `pluginId`, and pre-existing global enablement. Distinguish a
user-level value from one inherited from the target's project override.

If Superpowers is already installed from a matching source, adopt it and preserve
its user setting. Otherwise use a supported official marketplace route and preview
the native install and intended user/project values. Do not create a new repository
marketplace just to make an existing official plugin appear project-local.

Use this decision table for the **same actual plugin ID**:

| Before setup | Native package operation | User enablement | Project enablement |
| --- | --- | --- | --- |
| Already installed and globally enabled | Reuse | Preserve enabled | Explicitly set true |
| Already installed with a user setting of false | Reuse | Preserve false | Explicitly set true |
| Already installed; another user/default policy applies | Reuse | Preserve the existing effective choice | Explicitly set true where supported |
| Not installed; no pre-existing user choice | Perform native install | Default false after installation, with explicit consent for this user-config change | Explicitly set true |
| Not installed; a user setting already exists | Repair/install as previewed | Preserve that setting; ask about conflicts | Explicitly set true |

A new project-only installation must not leave a new user-wide `enabled = true`
behind. Existing global enablement is a deliberate exception to project-only
activation and must be reported as inherited, not as newly introduced by the harness.

### 2. Perform actual native installation when needed

Check the installed client's help, then use its plugin installer. Where supported:

```text
codex plugin add <plugin-name>@<marketplace-name> --json
```

Alternatively use the client's Plugins install flow. Obtain the exact installed ID
from the returned receipt/inventory; never guess it from the repository title or
invent a Codex `--scope project` flag. The current CLI does not expose that flag.
An `AVAILABLE` marketplace entry with `installed: false` is still pending.

The installer/UI can write user-level enablement. Preview this fact and obtain
explicit consent before running a flow that changes user configuration. Apply the
agreed final user value immediately after the native install, before invoking the
plugin. For a new install with no previous user choice, merge `enabled = false`
for that ID in the effective user config; preserve all unrelated bytes/settings.
**Never replace a pre-existing global true with false as a setup shortcut.**
Do not promise an atomic install with no transient user-state writes when the
native client cannot provide one. If the user prohibits all user-config writes,
do not silently use this flow; leave installation pending or offer the separately
chosen alternative below.

### 3. Explicitly enable the project

Merge this into the target `.codex/config.toml`, substituting the **exact same ID**
used by the native installation and any user setting:

```toml
[plugins."<actual-plugin-id>"]
enabled = true
```

When an existing global true is being reused, this project entry is still required
for explicit project intent. Never use a second ID merely to distinguish scope.
Project trust is required for its configuration to load. Report trust/policy blockers.

### 4. Verify final state

- Native inventory reports the package installed for that exact ID, with a version
  or installation path; a source directory is insufficient.
- Effective target-project configuration enables that ID. The user choice matches
  the before/after plan: pre-existing true or false is preserved; a new install with
  no earlier choice ends user-disabled and project-enabled.
- After reload/new session, native skill discovery and a no-write entry probe show
  Superpowers is loaded. Use actual discovered names and namespace.
- For a new project-only install, inspect an unrelated trusted project/context:
  the newly installed ID must not be enabled or expose its skills there. For a
  reused global plugin, expect continued availability elsewhere and report it.

Record install receipt/version, plugin ID, `install_method: native-plugin`, native
install/cache scope, `project_enabled: true`, `user_enabled_before`,
`user_enabled_after`, and actual `activation_scope`. Use `project` for a new
project-only activation and `inherited-user` when retaining prior global activation.
Do not mark ready until installation, effective configuration and entry loading
have all been verified. Native package files may remain in the normal shared cache.

## Claude Code

Use the native plugin installer from the target repository root with an explicit
[project scope](https://code.claude.com/docs/en/discover-plugins):

```sh
claude plugin install superpowers@claude-plugins-official --scope project
```

Check current help and source identity first. The default without `--scope` is
user-wide. A deliberately chosen `--scope local` instead records this user's
repo-only choice in `.claude/settings.local.json`; shared project scope uses
`.claude/settings.json`. Native caches/installation registries may be client-wide.

If an existing installed/global copy is reused, preserve it and explicitly merge
the same ID in project `enabledPlugins`; do not disable the user's existing entry:

```json
{
  "enabledPlugins": {
    "superpowers@claude-plugins-official": true
  }
}
```

If the marketplace is unavailable, use a project/local
[extraKnownMarketplaces declaration](https://code.claude.com/docs/en/settings-reference)
and let the trusted project load it; do not silently add a user-level marketplace
as a prerequisite. Recheck actual source/ID rather than assuming an alternative
marketplace shares the same identity.

Verify the scoped native receipt (or an existing package receipt when adopted),
effective project enablement and actual loaded skills after reload. An enabled
settings entry copied to another computer does not prove the plugin is installed
there. Preserve pre-existing global activation and report it as inherited.

## Repair and optional alternative

For the observed source-only failure, inventory the current source, marketplace,
config, record and hashes. Complete the actual native install for the intended ID,
then apply the decision table and verify loading. Preview removal of redundant
harness-owned marketplace/config entries or source copies; preserve user changes
and other plugins. Do not delete shared caches to repair one project.

Copying the complete upstream skill collection into the native project skill
directory is an **explicitly selected fallback**, not the default plugin install.
Inspect the chosen revision's resources and plugin-only features first. Preserve
the complete collection, notices, relative paths and actual native names. Record
`install_method: project-native-skills` and verify repo-scoped discovery/entry
loading; do not call it an installed plugin or promise plugin-equivalent hooks.
If required capabilities cannot be preserved, keep the foundation incomplete.
