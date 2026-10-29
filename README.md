# AI Dev Harness

A personal development setup that your coding agent installs into your projects.
Built for Codex and Claude Code, with an extensible, curated catalog of skills and
MCP integrations for the technologies and tasks you work with.

**Superpowers provides the standard development workflow.** Choose custom/personal
and community skills plus MCP tools for each repository. The registry is your
curated list: extend it for frontend, backend, or other development work.

This repository contains instructions, catalogs, and custom skills. There is no
harness CLI, service, agent runtime, or application dependency to install.

## Start in your project

Open the repository you want to configure in Codex or Claude Code and send:

```text
Install my AI development environment from https://github.com/RedtigerAV/ai-dev-harness.
Follow INSTALL.md and help me choose the components for this repository.
```

**Installing agent: start at [INSTALL.md](INSTALL.md).** Identify the target project
before changing files. Resolve source links against this repository. If the URL
cannot be read, use a local checkout or request the installation documents/catalogs.

The conversation is short: inspect the project, check Superpowers, choose skills,
choose MCP tools, preview changes, install, and verify. Already approved choices
do not need repeated confirmation. Global settings need separate explicit consent.
Some plugin installs, authentication, or restarts require action in the client.
Setup checks only the AI environment. It does not run your project's tests, builds,
code scans or application startup commands; those require a separate explicit request.
Superpowers uses its native plugin installer plus explicit project activation; an
existing globally enabled copy stays enabled. See the
[foundation setup guide](docs/superpowers.md) for new-install scope and verification.

Every project gets the full skills catalog, including all custom/personal skills,
then the full MCP catalog: individual bullets with names, useful descriptions and
`(recommended)` beside matching options. Choose several items in separate native
multi-select panels for skills and MCP. Recommendations never hide other options.
An empty project can defer technology choices. In a mixed repository, the agent
inspects relevant applications, services, libraries and their versions, configures
shared guidance once, and associates tools with their scopes.
Installing the harness does not upgrade dependencies or reorganize the project.

## Choose your tools

These are catalog entries, **not a claim that they are installed**. All except
Superpowers are optional. Collections are selected one skill at a time.

| Skill or collection | Use it for |
| --- | --- |
| Superpowers — required | Standard engineering process, from design to verification |
| learning-dev-workflow — custom | Guided programming exercises, requested help, and review |
| Angular Developer | Development and review in Angular projects |
| Angular New App | Creating a new Angular application |
| React Best Practices | React and Next.js engineering and performance |
| Vercel Composition Patterns | Reusable React component APIs |
| React Doctor | React diagnostics, with a separate tool/skill installation |
| UI UX PRO MAX | Visual design and interface quality |
| Matt Pocock Skills | Selected engineering, testing, planning, and teaching guidance |
| Addy Osmani Agent Skills | Selected architecture, review, security, and quality guidance |

| MCP integration | Use it for |
| --- | --- |
| Context7 | Library documentation |
| Angular CLI MCP | Angular workspace information and tooling |
| Next.js DevTools MCP | Running Next.js application diagnostics |
| Playwright MCP | Browser interaction and UI verification |
| Chrome DevTools MCP | Console, network, and performance investigation |
| Figma MCP | Accessible design context and assets |

Sources, installation routes, usage rules, caveats and probes live in
[the skills catalog](registry/skills.yaml) and [the MCP catalog](registry/mcp.yaml).
Ask: **“Show me all available skills and MCP servers, including what is already installed.”**
Recommendations reflect your project; they never select optional tools for you.
The current technology-specific entries can grow without changing the harness's
installation process.

## Use installed skills

```text
Implement filtering in the target application using the project's conventions.
```

Each installed skill gets a short **when to use it** rule in the managed section of
`AGENTS.md` and/or `CLAUDE.md`. The agent should load skills relevant to the task
and project context. Community skills and MCP integrations apply independently of
whether Superpowers is used. Selection for installation (`recommend_for`) and
selection during work (`usage`) are separate; see [skill routing](docs/skill-usage.md).

```text
Fix this typo. Do not use Superpowers or browser tools for this task.
```

Explicit exclusions apply to delegated work too. Trivial tasks should stay small
where the active process permits it. Routing instructions improve tool selection;
native client behavior still determines actual invocation.

You can invoke any installed custom or community skill by its name. Its own
description and instructions define its behavior. For example:

```text
Use learning-dev-workflow. Help me practice implementing a paginated data reader.
```

## Keep a project current

```text
Add components from AI Dev Harness. Show relevant tools I have not installed.
```

```text
Update this project's AI Dev Harness from its source. Preview the changes first.
```

```text
Verify this project's AI Dev Harness on this computer. Explain what needs attention.
```

Use [LIFECYCLE.md](LIFECYCLE.md) for additions, updates and another computer;
[VERIFY.md](VERIFY.md) for checks and troubleshooting. The project record at
`.ai-harness/installation.yaml` tracks choices, origins, revisions and observations
without credentials. Recheck readiness in each environment.

Existing project instructions are preserved. Only a delimited **AI DEV HARNESS**
section is managed. Incomplete setup is reported as **partially installed**.

## Adapt and contribute

Edit the catalogs or add a custom skill under `skills/`; see
[customization](docs/maintenance.md) and [product requirements](docs/product-requirements.md).
Public documentation is English; conversation follows your preferred language.

The [platform guide](docs/platforms.md) records researched routes and optional
capability checks. Native subagents, permissions and longer-running work depend
on the client/account. No model is forced and global changes are optional.

[Acceptance scenarios](docs/acceptance.md) distinguish repository checks from live
client tests. Sources were reviewed on **2026-10-29**; recheck upstream instructions
when installing because distributions and APIs change.
