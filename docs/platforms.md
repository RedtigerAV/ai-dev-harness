# Platform routes and compatibility

Sources checked **2026-10-29**. Recheck the linked primary documentation and local
client help before setup. These are supported starting points, not guarantees
about an older client or a particular account. A desktop app may work even when
its CLI is absent from PATH. Inspect available app capabilities before asking the
user to install another client.

## Project integration

| Concern | Codex | Claude Code |
| --- | --- | --- |
| Local skill directory | `.agents/skills/<name>/` | `.claude/skills/<name>/` |
| Project guidance | Effective `AGENTS.md`, considering overrides | Effective `CLAUDE.md`, considering imports and nested rules |
| Project MCP config | `.codex/config.toml`, subject to project trust | `.mcp.json`, subject to project approval |
| Explicit skill invocation | `$<skill-name>` or natural-language name | `/<skill-name>` or natural-language name |

Codex skills use a `SKILL.md` with YAML name/description. Project discovery includes
the repository's `.agents/skills`. See [Codex skills](https://developers.openai.com/codex/skills).
Claude Code supports project skills under `.claude/skills` with the same basic
format; see [Claude skills](https://code.claude.com/docs/en/skills). Copy complete
folders, not just entry points. Verify the effective name in the client after loading.

Codex can prefer `AGENTS.override.md` over `AGENTS.md` at a directory level and
applies more local guidance along the working-directory path. Inspect the actual
chain before editing; see [instruction discovery](https://developers.openai.com/codex/guides/agents-md).
Claude instructions support their own hierarchy and imports; see
[Claude memory](https://code.claude.com/docs/en/memory). If `CLAUDE.md` already imports
`AGENTS.md`, do not insert the same block twice. Do not add a new cross-platform
import unless its broader effects are understood and approved.

## Superpowers

Follow [Superpowers upstream](https://github.com/obra/superpowers) and the concrete
[native install and project activation procedure](superpowers.md).

- **Codex:** use the native plugin installer when the package is missing; then
  explicitly enable the actual installed plugin ID in the trusted project's config.
  Preserve existing user enablement. A new installation with no previous user choice
  ends user-disabled/project-enabled, with consent for any user-config write.
- **Claude Code:** use
  `claude plugin install superpowers@claude-plugins-official --scope project` from
  the target root, or adopt an existing package and explicitly enable it for the
  project. Preserve any existing global choice.

Source copying, marketplace discovery and enablement are separate from actual
native installation and loading. Shared client caches are acceptable. Manual skill
copying is a separately chosen fallback, not the default plugin distribution.

## Optional community skills

Prefer documented native distributions. For selectively installed portable skills,
the [upstream skills tool](https://github.com/vercel-labs/skills) supports choosing
individual members and target agents. Check runtime requirements and current help.
Examples to adapt after selection, from the **target project root**:

```text
npx skills add <upstream-source> --list
npx skills add <upstream-source> --skill <selected-member> -a codex
npx skills add <upstream-source> --skill <selected-member> -a claude-code
```

Run only the selected platform command. Confirm actual names from the source's
frontmatter/listing. Project scope is preferred; avoid
`-g` and blanket selection flags. The current tool documents Node 22.20 or later;
check again before execution. Where permitted, complete directory copies can avoid
requiring this optional tool. Do not run a collection's setup skill until its
effects have been previewed. Follow component-specific installation routes in the catalog.

## MCP configuration

Use existing equivalent plugins first. For direct configuration, preserve unrelated
entries and select only chosen servers. The following examples show **Context7**;
they are not a full configuration to paste over an existing file.

Codex project `.codex/config.toml`:

```toml
[mcp_servers.context7]
url = "https://mcp.context7.com/mcp"
bearer_token_env_var = "CONTEXT7_API_KEY"
```

Claude project `.mcp.json`:

```json
{
  "mcpServers": {
    "context7": {
      "type": "http",
      "url": "https://mcp.context7.com/mcp",
      "headers": {"Authorization": "Bearer ${CONTEXT7_API_KEY}"}
    }
  }
}
```

These reference a user-provided environment variable; they contain no key. Confirm
the launched app inherits it. Do not ask the user to paste secrets into chat.
For Figma, use the catalog URL and native OAuth instead of this bearer example.

Translate stdio catalog entries into `command` and `args` in the native format.
Codex supports a server `cwd`. Claude's documented stdio format should not be
assumed to support the same field: use a verified upstream workspace argument or
an explicitly quoted launch command that changes to the intended app directory.
Confirm returned workspace paths. If portable routing cannot be established,
report the limitation and offer app-specific client sessions using the shared
root installation. Do not invent config keys or silently use the root workspace.

Use [Codex MCP documentation](https://developers.openai.com/codex/mcp) for project
config and authentication. `codex mcp list` shows configuration, while `/mcp` in the
TUI shows active connections. OAuth servers support `codex mcp login <name>`.
Check the scope of CLI add commands rather than assuming they write project config.

For Claude, [MCP documentation](https://code.claude.com/docs/en/mcp) describes
`claude mcp add --scope project` and `.mcp.json`; the default CLI scope is not a
substitute for choosing project scope. Use `/mcp` for connection/login checks.
Configuration, authentication, and a successful capability call are separate checks.
Apply VERIFY.md's installation-only boundary: verify connectors and their own
runtimes, not the target project's builds/tests. Do not launch the application or
its services merely to exercise runtime tools; report app-specific checks as untested.

## Optional capability check

Inspect capabilities of the current session first. Do not apply an old experimental
flag simply because a guide once recommended it.

- [Codex subagents](https://developers.openai.com/codex/multi-agent): current releases
  document native support. Delegation follows the active client's policies; it
  increases token use. Skill-defined responsibilities can also be performed sequentially.
- [Claude subagents](https://code.claude.com/docs/en/sub-agents): native subagents
  can take role instructions. No custom agent files are necessary for this release.
- [Claude agent teams](https://code.claude.com/docs/en/agent-teams) remain documented
  as experimental. They are optional, add cost/coordination, and are not a prerequisite.
- Long tasks: check native continuation, background-task support, session limits,
  and interruption behavior in the installed client. Save concise progress so work
  can resume. Do not promise indefinite execution or create a scheduler.
- Permissions: recommend only what selected tools need. Explain concrete changes,
  scope, effects, and experimental status. Ask before user/global edits; inherit
  the user's model configuration. Do not disable approvals or sandboxing for convenience.

If a setting cannot be verified, leave it unchanged and link current manual guidance.
Record declined suggestions as choices, not installation failures.
