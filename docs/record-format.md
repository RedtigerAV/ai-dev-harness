# Installation record, version 1

The YAML at `.ai-harness/installation.yaml` is a small human-readable handoff, not
a runtime database. Start from [the template](../templates/installation-record.yaml).
Paths below are relative to the target repository unless a scope explicitly differs.
Quote dates and revisions. Use `null` for unknowns rather than invented values.
Preserve unrecognized fields when editing a record from another harness version.

## Identity and selections

- `harness.source`: canonical source URL or documented local source.
- `harness.revision`: revision of the harness guidance actually applied. If an update
  is incomplete, `requested_revision` identifies its target; component revisions
  still describe what is actually installed.
- `platforms`: requested `codex` and/or `claude-code`.
- `applications`: applications/services/libraries with `path`, `frameworks`
  (technology name, declared version, resolved version or null, and evidence path),
  `package_manager`, `test_command`,
  and `instruction_files`. An empty repository can have an empty list.
- `choices.selected` / `declined`: catalog IDs, or `catalog-id/member-name` for a
  collection member. A collection ID alone is not an install selection. Superpowers
  remains selected/required even if blocked; note refusal in its next action.

## Component instances

Each component entry is unique by `(id, member, platform, instance)`. Use a separate
entry for each client and each distinct workspace binding. `app_paths` lists the
applications that instance serves; one shared instance may cover several apps.

Record the source, actual member name, resolved revision/package version, install
method, scope (`project`, repository-private `local`, `user`, `account`, or `external`), and location/native
plugin identifier. Record `ownership: external` when adopting an existing tool;
this does not grant permission to update or remove it. `update_policy` describes
pinning or native automatic updates.

For a native Superpowers plugin, keep its exact plugin ID, receipt and version.
Distinguish native `install_scope`/cache location from `activation_scope`: a newly
installed plugin can live in the shared client cache while enabled only for the
project. Record `project_enabled`, `user_enabled_before` and `user_enabled_after`.
Preserve pre-existing user choices. Use `activation_scope: inherited-user` when an
existing globally enabled copy is reused, rather than falsely claiming isolation;
use `project` for a verified new project-only activation. Unset/unknown values are
null and must not be treated as evidence of false/disabled. A manually chosen
`project-native-skills` fallback has its own member/file inventory and no plugin receipt.

For skills, retain the resolved `usage_instruction` used in project instructions
and the actual member name/context, especially for collections. It summarizes when
to apply the skill; detailed behavior remains in the installed skill itself.

`state` uses the six values in [VERIFY.md](../VERIFY.md). `last_successful_stage`
retains useful progress if the latest check fails. `observation` contains an ISO
timestamp, a non-sensitive user-chosen context label (for example `computer-secondary /
Codex Desktop`), the capability tested, and concise evidence. Do not store serial
numbers, account identifiers, or raw private tool responses. On another computer,
keep old evidence as history if useful, then replace current state only with new
observations. Missing access is not permission to mark a check passed.

Scope observations to installation capabilities such as connector startup,
authentication, native discovery and harmless tool responses. If the target app is
not running, record its runtime diagnostics as untested; do not mark a healthy AI
connector failed or run product builds/tests to obtain installation evidence.

`failure` is null or a mapping with `stage`, `summary`, and `retry` (redacted).
`next_action` is a concrete instruction or null when none remains.
`files` lists owned project files and their last-applied SHA-256 hashes, for example:

```yaml
files:
  - path: .agents/skills/example-skill/SKILL.md
    sha256: '<actual SHA-256 of the installed file bytes>'
```

Record all installed custom skill resources, not just SKILL.md. Hashes support
conflict detection, not authentication. Plugin-managed files need not be hashed;
record their native identity/version instead. Do not hash or copy credential stores.

## Instruction ownership

`instruction_files` holds `path`, `platforms`, and `managed_block_sha256` for the
last applied block. Hash bytes from BEGIN through END (including the marker lines,
excluding the newline after END). Compare before replacing. Preserve line endings;
never hash a normalized representation and then claim byte preservation.

An unknown hash means inspect/reconcile rather than overwrite. For an existing
shared imported block, list the physical source file once with both platforms.
Do not claim that every `AGENTS.md` or `CLAUDE.md` in the repository is managed.

`last_operation` records install/add/update/verify/recover, time, result
(`complete` or `partially_installed`), and a concise factual summary. Completeness
is computed from verified current state and requested scope, not from template defaults.
