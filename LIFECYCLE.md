# Add, update, and recover

Use the same catalogs, platform adapters, safe merge procedure, and verification
as [INSTALL.md](INSTALL.md). There is no separate migration system.

## Read the current state

Read the installation record and effective project instructions, then inspect the
actual skills, plugins, and MCP capabilities. The record is evidence of prior work,
not authority to overwrite current files. Identify the source revision, installed
versions, selection choices, ownership, and any user customizations. No record?
Inventory the existing setup, show what can be adopted, and establish a record from
observations rather than assuming a fresh installation.

## Add components

1. Consult the current catalog and re-detect relevant apps, including new manifests.
2. Show relevant absent/declined components first, with name, source, purpose,
   compatibility, scope, and current state. Offer the full catalog on request.
3. Obtain the additional selection. A named-component request may already supply it;
   clarify only its scope, ambiguous collection members, or unresolved conflicts.
4. Preview changes. Install only the selected additions and necessary approved
   prerequisites. Do not upgrade or reinstall unrelated working components.
5. Verify new capabilities and their task-time routing. Add a concise usage rule
   for every new available skill/member to the managed instruction section and merge
   records. Preserve versions and usage rules of components not changed.

If Superpowers is missing, report the incomplete foundation and offer repair. A
request to add Context7 alone does not authorize a global Superpowers installation.

## Update

1. Resolve the requested harness revision, or current upstream revision if none
   was specified. Review relevant changes since the recorded source. Compare the
   installed component versions separately; a catalog refresh is not a bulk upgrade.
2. Compare recorded file hashes and source revisions with current installed files.
   Use the original upstream version as a base where available. A hash mismatch
   means local changes need review, not automatic replacement.
3. Present the exact components, old/new revisions, instruction changes, scope,
   compatibility issues, and manual actions. Obtain approval before applying them.
   A prior approval of this exact preview remains valid.
4. Save a recoverable diff or local backup of harness-owned changes. Keep any backup
   containing private configuration out of Git and never copy credential stores.
5. Update approved components through their recorded installation route. For a
   customized skill, offer keeping the local copy, manually merging, or an explicitly
   approved replacement with recovery available. Do not use a global “update all”
   command for a subset. Preview changes to shared user-level plugins across projects.
6. Recheck usage rules against each updated skill's own description. Preview and
   merge the resulting rules with the managed instruction blocks using INSTALL.md's
   marker/conflict rules. Preserve unrelated settings, authentication references,
   and unknown record fields. If a component has disappeared upstream, report it;
   do not remove it silently.
7. Verify and save actual per-component revisions/states. A partially failed update
   must keep old versions for unchanged components and distinguish applied changes
   from the intended target revision. Report **partially installed** where appropriate.

## Repeat installation or move to another computer

Re-running installation is reconciliation: reuse equivalent components and leave
unchanged files alone. Preserve declined choices unless the user asks to reconsider
them. Do not append duplicate blocks or re-run successful setup for unrelated items.

On another computer, treat previous readiness observations as historical. Check
the current client's skill discovery, plugin inventory, runtime, credentials, and
MCP capabilities. Do not copy credentials, machine-specific absolute paths, or
trust decisions from the record. Prefer repository-relative scopes; reconstruct
necessary local paths from the current checkout. If a shared client config requires
an absolute path, explain portability limits and choose a supported local adapter
with consent. Reverify each configured platform independently.

## Recover or retry one component

Use the component's recorded next action and [VERIFY.md](VERIFY.md). Retry the
failed stage after addressing its cause. Leave working components in place. Restore
only changes from this operation if rollback is requested; never reset the entire
repository or overwrite pre-existing user edits. Verify the restored state and
record it honestly. An externally owned component is not removed by harness recovery.

If the user requests removal, preview the exact owned files/entries and any
cross-project effects. Remove only approved harness-owned material, preserve
customizations, and update instructions and choices. Shared native plugin removal
must use its own scope-aware workflow; deleting a record alone does not uninstall it.
