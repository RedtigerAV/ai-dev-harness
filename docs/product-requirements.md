# AI Dev Harness — Product Vision & Requirements

**Document type:** Product vision, user expectations, and functional requirements\
**Status:** Agreed requirements for an initial implementation\
**Primary audience:** An AI coding agent responsible for designing and building the repository\
**Language:** English\
**Project:** `ai-dev-harness` (working name)

> **Important:** This is a requirements brief, **not an implementation specification**. It describes the intended experience, capabilities, behaviors, constraints, and acceptance expectations. The implementing agent should investigate the current Codex and Claude Code capabilities, propose a proportionate design, and choose the technical implementation.

---

## 1. Project vision

**AI Dev Harness** is a lightweight, reusable, agent-installable development environment for people who work with AI coding agents.

Its primary purpose is to make the maintainer's daily software development simpler: open any existing or new repository, give Codex or Claude Code a link to AI Dev Harness, make a few selections, and have the agent configure the relevant development skills and tools with minimal manual work.

The project is intended to be **a curated personal development setup**, not a new agent framework, orchestration engine, package manager, or replacement for existing AI coding products. It should build on their native capabilities and on established community tools.

Superpowers provides the standard development methodology. A personal curated registry supplies optional custom/community skills and MCP integrations for relevant technologies and tasks. The catalog can expand into frontend, backend or other development areas without changing the installation process.

Each skill defines its own behavior. Guided programming education is one supported capability in the initial catalog, alongside domain-specific development and diagnostic guidance.

The immediate beneficiary is the maintainer, who works across repositories and development technologies. The repository will be public on GitHub, and other developers should be able to adopt, customize, or extend it if they find it useful.

### 1.1 Intended users

- **Primary:** A developer who uses Codex and maintains repositories with one or more applications, services, or libraries across different technology stacks.
- **Secondary:** The same developer using Claude Code, on a different computer or in a different repository.
- **Additional:** Other developers who want a curated, adaptable, agent-installed development environment.

The initial experience should be excellent for a single developer. Team-wide administration and enterprise infrastructure are **not** the project's primary goal.

### 1.2 Desired outcome

The desired user experience is:

> “I open a project, ask my AI coding agent to install my AI development environment from a GitHub URL, select the suggested components, and start developing or learning. I do not have to manually reconstruct my setup for every repository.”

Installation should generally be a **short, conversational process**, not a lengthy series of commands. Some integrations may require authentication, permissions, or manual steps; those should be clearly explained rather than hidden.

---

## 2. Guiding principles

The implementation must preserve these product principles.

### 2.1 Agent-native, minimal infrastructure

- The **existing Codex or Claude Code agent** acts as the installer, configurator, and verifier.
- Installation is initiated by sharing the repository URL and asking the agent to follow its documented instructions.
- Favor clear Markdown guidance and curated catalog metadata over creating a custom executable installer.
- **Do not introduce a dedicated CLI, bootstrap system, orchestration service, or large script suite for the first release.** Tiny helpers are acceptable only when there is a concrete need that the agents cannot reliably handle with their existing tools.
- Reuse first-party platform functionality and community tooling rather than reimplementing it.

### 2.2 Superpowers-first, not Superpowers-only

- **Superpowers is a required component of a complete harness installation.**
- Installing Superpowers does **not** mean it must be invoked for every task.
- The user may explicitly exclude Superpowers or any other skill/tool from a particular request.
- The harness should guide tool selection without forcing elaborate workflows onto trivial tasks.

### 2.3 The developer remains in control

- The installer presents choices and obtains the user's selection before installing optional components.
- Existing project instructions must be **preserved**, never replaced wholesale.
- Changes to global or user-level Codex/Claude settings must be explained and explicitly approved.
- The user can decide which tools to use on a given task, even after installing them.
- The harness should not make new blanket restrictions on Git commits or pushes; normal platform and repository permissions still apply.

### 2.4 Context-sensitive and reusable

- Recommendations are based on the repository actually being configured.
- Different projects can have different installed components.
- A mixed-framework repository must be supported as naturally as a single application.
- The same source repository should work as an installation reference for Codex and Claude Code.
- Tool availability, versions, and framework-specific advice must be checked rather than assumed.

### 2.5 English-first and publicly understandable

- Repository documentation, skill definitions, agent role descriptions, registries, installation instructions, and examples must be written in **English**.
- The developer may converse with the coding agent in English or Russian; the harness must not unnecessarily force a conversation language.
- The README must be sufficiently clear for someone who did not participate in the original design discussions.

---

## 3. Project scope

### 3.1 Included in the first release

The first release should provide:

1. A public, well-documented GitHub repository that can be handed directly to Codex or Claude Code as an installation source.
2. Clear instructions for **initial installation**, **adding components later**, **updating**, **verification**, and **troubleshooting**.
3. **Superpowers** as the required foundation for normal development.
4. A custom **`learning-dev-workflow`** skill with explicitly described learning-agent roles and a clear integration boundary with Superpowers.
5. A curated catalog of the maintainer's custom skills, recommended community skills, and MCP servers.
6. Project-aware recommendations and conversational component selection.
7. Safe augmentation of existing `AGENTS.md` and/or `CLAUDE.md` with an identifiable **AI DEV HARNESS** section.
8. A project-level installation record at **`.ai-harness/installation.yaml`**.
9. Installation and verification behavior that is understandable, recoverable, and transparent about failures.
10. Support for both new and existing repositories, including repositories with multiple applications, frameworks, and independent package manifests.
11. A check of relevant Codex/Claude capabilities and optional guidance for useful settings, without silently changing global configuration.

### 3.2 Explicitly out of scope for the first release

Do **not** build these solely for their own sake:

- A custom AI orchestration engine, workflow runtime, job scheduler, or durable agent-state machine.
- A bespoke installation CLI or package distribution system.
- A comprehensive custom framework for Git commit/push restrictions, hooks, or approval controllers.
- A large custom production-agent fleet that replicates existing Superpowers or native platform agents.
- Automatic modernization or upgrades of application dependencies as part of harness installation.
- A hard-coded model choice for Codex, Claude, or any subagent.
- Mandatory global user-level configuration changes.
- Guarantees that an agent can work indefinitely without interruption or that a prompt alone enforces an unbreakable permission boundary.

---

## 4. Platforms and development environments

### 4.1 Primary environment

- **Codex** is the primary target, especially its desktop application and interaction with local repositories.
- The harness is independent of operating system and IDE. Individual tools may have documented runtime requirements.
- The setup should be reusable on another computer without relying on machine-specific paths or credentials.

### 4.2 Second environment

- **Claude Code** is also a supported target.
- The user-facing workflows and available catalog should be conceptually consistent across both platforms.
- Platform-specific behavior and configuration may differ. The project should explain those differences instead of pretending the two runtimes are identical.

### 4.3 Native capabilities first

When a capability such as skills, subagents, MCP integration, or project instructions is already supported by the coding platform, the harness should use that capability rather than implementing a substitute.

The implementing agent is responsible for checking current platform behavior and avoiding obsolete or unsupported configuration instructions.

---

## 5. Fundamental requirement: installation through an AI agent

### 5.1 Primary entry point

A user should be able to open a target repository in Codex or Claude Code and send a short prompt equivalent to:

> Install my AI development environment using the instructions at:\
> `https://github.com/OWNER/ai-dev-harness`

The agent should be able to discover the appropriate installation instructions from the repository, read the relevant guidance, inspect the current project, and lead the user through installation.

**The user should not have to manually copy long setup instructions into every prompt.** The repository itself is the source of those instructions.

If access to the repository URL is unavailable, the agent must explain the limitation and offer a straightforward alternative, such as allowing the user to provide a local checkout or the necessary documentation.

### 5.2 Expected installation conversation

The desired sequence is:

1. **Read the harness instructions.** Determine whether the user is in Codex or Claude Code and identify the target repository.
2. **Inspect the existing project.** Determine whether it is empty, an existing application, or a monorepo. Identify frameworks and relevant existing AI configuration.
3. **Check Superpowers.** Install it using its supported distribution mechanism if possible; otherwise explain the exact manual steps. Superpowers is required for a complete installation.
4. **Present custom and community skills.** Show the recommended selection first, with names and concise descriptions, and let the user choose which optional skills to install. Offer the full catalog on request.
5. **Install the selected skills.** Project-local installation is preferred where supported. Report conflicts or required manual steps.
6. **Present MCP options.** Recommend the ones relevant to the detected project, provide names and descriptions, and let the user choose.
7. **Configure the selected MCP integrations.** Handle permission or authentication requirements transparently. Do not report a server as working merely because a configuration entry exists.
8. **Check optional platform capabilities.** Explain worthwhile settings for multi-agent or longer-running work. Ask before changing user/global settings.
9. **Augment project instructions.** Add or update an identifiable `AI DEV HARNESS` section in the relevant existing project instruction files, preserving other content.
10. **Record the installation.** Store the selected components and their state in `.ai-harness/installation.yaml`.
11. **Verify and report.** Confirm what is installed, what is operational, what requires a restart or manual action, and what failed.

The agent should not silently install every optional component. A project-aware recommendation is a starting point for user choice, not a command to install everything.

### 5.3 Empty and existing repositories

- For an **empty/new project**, show the full set of available skill and MCP options, since there may be no reliable framework to infer yet. The user can select a future intended stack or defer tools.
- For an **existing single-framework project**, surface the most relevant tools first.
- For an **existing mixed-framework repository**, recommend tools for each detected application or framework.
- Users must always be able to ask: **“Show me all available skills and MCP servers.”**
- Existing tools, plugins, MCP servers, and project instructions must be recognized to avoid duplicate installation and conflicting definitions.

### 5.4 Installation is a guided task, not a black box

Before making a substantial set of changes, the agent should present a concise summary of what it intends to add or adjust and obtain user confirmation of the selections. The agent may need additional platform-native permission prompts.

If the installation only partially succeeds, the final result must say **partially installed**, not “done.”

---

## 6. Superpowers: required foundation and usage rules

### 6.1 Installation requirement

Superpowers must be installed or its absence must be clearly reported as blocking a **complete** harness installation.

The agent should prefer the currently supported, official installation route for the active platform. If installation cannot be completed automatically, it should provide clear, up-to-date manual instructions and verify afterward where possible.

### 6.2 Ordinary software development

Superpowers is responsible for the standard development methodology: clarifying and designing work, planning, implementation, testing, debugging, review, and other phases supported by its current version.

AI Dev Harness should **not** implement a parallel production workflow that competes with Superpowers.

Installed domain skills and MCP integrations apply according to their own task/context rules. Their use does not require Superpowers. Keep community skill and MCP descriptions self-contained, without references to other skills or workflows.

### 6.3 Selective use; explicit exclusions

Installation and use are separate decisions:

- Superpowers is installed as the default development foundation.
- The user can explicitly request **not** to use Superpowers on a particular task.
- The user can similarly exclude any installed skill or MCP tool in the task prompt.
- A trivial task should not automatically become a complex planning exercise if the active process permits a lighter approach.
- Explicit exclusions should be respected across delegated work as far as the platform makes that possible.

The repository should explain that such instructions guide agent behavior; they are not a runtime guarantee that an installed plugin can never activate independently. The project should not build a custom enforcement mechanism just to suppress excluded skills in the first release.

### 6.4 Missing Superpowers at task time

If Superpowers was expected but is no longer installed or available:

- Inform the user and offer to restore/install it.
- Do not pretend that the complete Superpowers workflow ran.
- For ordinary development, explain that the recommended foundation is unavailable.
- For Learning Mode, permit a clearly identified **simplified standalone learning fallback only when the user explicitly chooses to proceed without Superpowers**.

A small learning task may skip Superpowers brainstorming even when Superpowers is installed; this does not make the installation incomplete.

---

## 7. Custom learning workflow: purpose and boundaries

### 7.1 Skill identity

One initial custom skill is named **`learning-dev-workflow`**. Its own definition specifies its educational behavior; it uses the same installation and discovery procedure as every other custom/personal skill.

The user should be able to invoke it explicitly, alongside a natural-language description of an exercise or feature they want to build. No repeated boilerplate instructions should be necessary.

Example intent:

> Use `learning-dev-workflow`. Help me practice implementing a paginated data reader.

### 7.2 Educational purpose

The goal is **to teach by preparing a structured exercise, not to complete the exercise for the learner**.

The learner writes the core functionality. AI agents provide the architectural context, initial structure, behavior requirements, test cases, and progressively more helpful guidance when requested.

This applies across programming languages and technology stacks. A full solution is disclosed only at the explicitly requested assistance level and is not written to files without a separate explicit request.

### 7.3 Complexity-aware behavior

The skill must consider the **actual complexity and educational objective** before choosing its process.

- **Trivial exercises:** Avoid unnecessary Superpowers brainstorming/planning. A brief task explanation, small scaffold, and suitable tests may suffice.
- **Small exercises:** Clarify public behavior and the relevant concepts; perform only lightweight planning.
- **Medium exercises:** Use relevant Superpowers brainstorming and planning capabilities when they meaningfully improve the architecture and learning plan.
- **Complex exercises:** Conduct more thorough requirements discovery, architectural discussion, trade-off evaluation, and planning before preparing the exercise.

Complexity must not be judged solely by the number of files. Consider ambiguity, dependencies, risk, architectural choices, the developer's stated goals, and whether the task introduces new concepts.

Do not launch every learning agent or every planning phase for every exercise. Use the relevant roles without unnecessary ceremony.

### 7.4 Superpowers integration boundary

For medium and complex learning tasks, the learning workflow should benefit from Superpowers' **brainstorming and design/planning** strengths.

However, the **plan must be an educational preparation plan**, not an instruction to have Superpowers automatically implement the feature.

For learning tasks:

- Superpowers may help clarify requirements, explore approaches, design the public contract, and organize the exercise.
- After planning, the user approves the learning direction and appropriate scaffold scope.
- **Superpowers must not proceed to its normal autonomous feature-implementation process on the learner's behalf.**
- Specialized learning roles then prepare the exercise; the user retains responsibility for writing the application logic.
- The harness must explicitly describe and verify this boundary, while acknowledging that interacting skills remain subject to the underlying agent platform's behavior.

### 7.5 Explicit approval before preparation

For tasks involving meaningful changes to project files, the learner should have a chance to review the proposed scope and public contracts before the agents prepare the scaffold and tests.

For truly trivial exercises, the plan can be very short. Approval must not become an unnecessarily bureaucratic multi-document exercise.

---

## 8. Required learning-agent responsibilities

The first release must include clear, reusable role definitions or equivalent agent instructions for the following responsibilities. The implementing agent may decide how best to map them to native Codex and Claude Code agents; their duties must not be omitted.

### 8.1 Learning Architect / Tutor

**Purpose:** Help the learner understand and agree on the problem before code preparation.

Expected behavior:

- Clarify goals, unknowns, and acceptance criteria.
- Explain viable architectural approaches and meaningful trade-offs.
- Identify which concepts the exercise is intended to teach.
- Agree on public-facing interfaces and contracts where appropriate.
- Avoid prematurely designing internal implementation details the learner should discover.
- Request approval before significant preparation work.

### 8.2 Scaffolder

**Purpose:** Create the initial structure the learner will implement.

Expected behavior:

- Prepare only the relevant folders, files, component/function shells, public interfaces, and minimal dependencies.
- Use placeholders or intentional unimplemented stubs for behavior the learner must write.
- Maintain compatibility with the project's existing architecture and framework version.
- Avoid building unnecessary architecture merely to demonstrate a pattern.
- **Do not implement business logic or provide a copy-paste-ready solution.**

### 8.3 Task Annotator

**Purpose:** Add concise, high-level behavioral guidance at the places the learner needs to work.

Expected behavior:

- Add TODO-style descriptions of the intended behavior and constraints.
- Mention important edge cases or expected outcomes when helpful.
- Avoid revealing the exact algorithm, detailed control flow, private method names, additional fields, or the full solution design.
- Keep instructions clear enough that the learner knows what to achieve without being told precisely how to code it.

### 8.4 QA / Test Designer

**Purpose:** Provide meaningful tests that establish the desired behavior independently of implementation.

Expected behavior:

- Base tests on approved requirements and public contracts, not on an invented implementation.
- Cover relevant normal, edge, and error behavior without overspecifying internal design.
- Ensure the test setup itself is usable.
- Make expected failures due to intentionally missing implementation distinguishable from broken test infrastructure.
- Prefer focused, educationally useful tests to an excessive test suite.
- Do not expose a full implementation through test helpers or fixtures.

### 8.5 Tutor / Reviewer

**Purpose:** Support learning during implementation and provide constructive evaluation afterward.

Expected behavior:

- Support four assistance levels selected from the request: **No hints**, **Small hints**, **Pseudocode**, and **Full solution**.
- No hints permits the agreed exercise and evaluation without solution guidance; Small hints provides focused conceptual nudges; Pseudocode provides non-executable steps.
- Full solution provides complete code for the requested scope in the response. Writing that code into files requires a separate explicit request.
- Do not escalate the level without a user request. When unspecified, prepare without hints and use small hints for a generic request for help.
- Do not silently modify or repair learner-owned implementation files.
- On request, review the learner's code for correctness, edge cases, architecture, framework best practices, maintainability, and test coverage.
- Explain the *reason* for issues and possible directions for improvement; the learner ordinarily makes the fixes.

The exact number of runtime subagents may vary by platform and task. **All five responsibilities must exist even if an exceptionally small exercise is handled by fewer actual agents.**

---

## 9. Learning workflow: expected end-to-end journey

### Phase A — Understand the exercise

The learner submits a task. The workflow examines the relevant project context, recognizes the framework and versions, identifies learning objectives, and classifies complexity.

When beneficial, it uses Superpowers brainstorming and planning to discuss architectural options and expected behavior. The conversation focuses on choices the learner should understand, not on generating a full implementation.

### Phase B — Agree on the exercise

The agent presents a clear, appropriately sized learning plan:

- What feature or behavior will be implemented.
- What the learner is expected to write.
- What the AI agents will prepare.
- Which interfaces, if any, must be fixed so tests can be written.
- What success looks like and what edge cases matter.
- Which concepts or patterns are being practiced.

The learner can request changes before authorizing preparation.

### Phase C — Prepare the project

Depending on the exercise, the learning roles:

1. Create the minimum useful scaffold.
2. Insert high-level TODO annotations and unimplemented behavior.
3. Add behavior-oriented tests tied to the agreed contracts.
4. Provide a concise learning guide or task description where useful.
5. Explain what remains for the learner to build.

**They stop before implementing the core functionality.**

### Phase D — The learner implements the solution

The learner edits the project in their preferred editor.

When the learner asks for help, the Tutor provides guidance proportional to the request. It should not turn a request for a hint into an unsolicited completed feature.

### Phase E — Review on request

When invited, the Reviewer checks the learner's work against the acceptance criteria, relevant tests, and the framework's current supported practices.

It reports findings with understandable explanations and prioritization. It should not automatically replace the learner's code with its preferred implementation.

### Phase F — Consolidate learning

The workflow may summarize the concepts practiced, decisions made, and remaining areas for improvement. The final response should help the learner transfer the knowledge to a similar future task.

### 9.1 Learning documentation is different from Superpowers documentation

The normal development documentation generated by Superpowers is **not** the template for this workflow.

Learning documentation should be concise, learner-oriented, and avoid giving away the solution. It may include:

- A task brief and acceptance criteria.
- A conceptual learning guide with architecture, patterns, and useful documentation links.
- A review summary after the learner requests a review.

The amount of documentation must scale with task complexity. For tiny exercises, a short explanation in chat may suffice. Use a suitable existing location for larger learning materials.

---

## 10. Curated skill catalog

The harness must offer **custom skills** from its own repository and **community skills** from trusted upstream sources.

### 10.1 Custom skills

Include `learning-dev-workflow` in the initial catalog and make it straightforward to add more custom/personal skills.

All selected custom skills follow the same complete-directory installation, resource verification, discovery and update process. Each skill defines its own behavior, modes and dependencies. The installer must not contain special branches keyed to one custom skill. Selection remains optional for every custom skill.

### 10.2 Community skills to offer

At minimum, the catalog must include these options, with verified upstream sources and understandable descriptions:

| Skill or skill collection | What the user should understand |
|---|---|
| **Superpowers** | **Required foundation** for standard agentic development workflows; not an optional catalog item during initial installation |
| **Angular Developer** | Official Angular-specific development guidance and current best practices |
| **Angular New App** | Official guidance for creating and structuring a new Angular application |
| **React Best Practices** | React and Next.js engineering and performance guidance |
| **Vercel Composition Patterns** | Component composition and maintainable React component API patterns |
| **React Doctor** | React diagnostics and review-oriented checks; its installation form may differ from a conventional skill |
| **UI UX PRO MAX** | UI/UX design and interface-quality guidance |
| **Matt Pocock Skills** | Optional selection of focused engineering, planning, testing, review, and teaching skills |
| **Addy Osmani Agent Skills** | Optional selection of engineering, architecture, security, documentation, and quality skills |

The agent should suggest relevant items, not blindly install entire collections.

### 10.3 Information shown before selection

For each option, show:

- Name and a concise description.
- Whether it is **required**, **recommended for the current project**, or **optional**.
- The frameworks or types of tasks for which it is relevant.
- Its upstream source and any important installation or compatibility caveat.
- Whether it is already installed.

The user should be able to view the whole catalog, select several items, and decline others.

### 10.4 Skill selection during work

Every skill registry entry must distinguish installation recommendations from task-time usage rules: role, contexts, triggering tasks, meaningful exclusions and a concise instruction. For collections, resolve rules for each selected member.

The installer must place a brief purpose and **when-to-use rule for every available installed skill** in the managed AGENTS.md and/or CLAUDE.md section. During work the agent identifies the target project/task and loads matching skills according to their own usage rules, independently of the active workflow and subject to explicit exclusions. A skill's own description and instructions define its detailed behavior.

The agent should respect explicit user exclusions and each skill's own scope. Superpowers provides the default ordinary development process; individual community skills and MCP integrations remain independently applicable.

---

## 11. Curated MCP catalog

The MCP catalog must offer these integrations at minimum:

| MCP option | Expected purpose |
|---|---|
| **Context7** | Library documentation and relevant API guidance |
| **Angular CLI MCP** | Angular-specific documentation and project tooling |
| **Next.js DevTools MCP** | Next.js development/runtime diagnostics and tooling |
| **Playwright MCP** | Browser-based interaction and UI verification |
| **Chrome DevTools MCP** | Console, network, browser debugging, and performance analysis |
| **Figma MCP** | Access to design context and assets when permitted |

MCP selection should follow the same user experience as skill selection:

- Detect relevant frameworks and recommend matching tools.
- Show names, descriptions, and availability/status.
- Let the user choose from the recommended subset or request the full list.
- Explain authentication, local runtime requirements, and manual steps where needed.
- Avoid duplicating already configured integrations.
- Verify the available capability rather than assuming configuration implies connectivity.

Not every MCP must be configured globally. Use project-level integration where the active platform supports it and where it makes sense; explain exceptions.

The catalog must remain easy for the maintainer to expand or edit without introducing a bespoke management application.

---

## 12. Project detection and recommendation behavior

### 12.1 Requirements

Before recommending tools, the installer should understand the repository well enough to avoid irrelevant selections.

It should identify, when possible:

- Whether the repository is empty or already contains an application.
- Languages, frameworks and relevant development tools, based on detected project evidence and extensible catalog metadata.
- The framework and library versions relevant to each application.
- Whether there are multiple independent projects or workspaces.
- Any existing AI development configuration and installed tools.

Do not assume the root package manifest describes every application.

### 12.2 Mixed-framework monorepositories

A single repository may contain applications, backend services and libraries using different languages or frameworks, each with its own manifests, dependency versions and build tooling.

In this situation:

- **One harness installation at repository level should be sufficient** for shared workflows and project-level instructions.
- The installer should identify the relevant applications and suggest tools for each framework.
- The user should not be required to initialize the entire harness independently inside every application.
- The installed tools and future agent behavior should remain aware of which application a task concerns.
- Framework guidance should be appropriate to the target application's installed version.
- A task affecting multiple applications should be able to use relevant tools for each, without confusing their contexts.

If a desired integration cannot work reliably across independent workspaces, explain the limitation and recommend an appropriate configuration rather than silently connecting to the wrong application.

### 12.3 Avoid unexpected project changes

Installing the harness must not automatically migrate dependency versions, refactor product code, reorganize package boundaries, or install unrelated runtime dependencies.

The harness installs **AI development capabilities**, not changes to the product being developed.

---

## 13. Project instructions: AGENTS.md and CLAUDE.md

### 13.1 Required behavior

During installation, augment the relevant project instruction files for the selected platform(s): `AGENTS.md`, `CLAUDE.md`, or both.

- If a required file does not exist, create it.
- If it exists, **preserve all existing non-harness content**, including team conventions and architectural guidance.
- Add a clearly labeled **`AI DEV HARNESS`** section.
- Future harness updates should update that section without duplicating it or rewriting unrelated content.
- If a conflict or ambiguous existing configuration is found, explain it and ask the user how to proceed.

The goal is to complement project instructions, not replace them.

### 13.2 What the AI DEV HARNESS section must convey

Keep it concise and useful. It should cover:

1. The role of Superpowers in standard development.
2. The purpose and concise task-time usage rule of **every available installed custom skill**, using its actual invocation name.
3. Each **selected and confirmed available community skill/member**, with its actual name, purpose, triggering tasks/contexts and relevant project scopes.
4. Each **selected MCP integration**, with a short description and the situations in which it is useful. Clearly distinguish configured-but-not-working integrations.
5. The principle that the agent should choose only relevant tools for the task.
6. The instruction to **respect explicit user requests not to use a particular skill, MCP, or Superpowers** for a given task.
7. A reference to the harness installation/update/add-component guidance, where helpful.

Catalog descriptions should be maintained so that the installation agent can reuse concise, consistent wording in project instructions.

Do not dump the entire external documentation of a skill or MCP into `AGENTS.md` or `CLAUDE.md`.

### 13.3 Existing team instructions and platform differences

The installer must respect existing root-level and nested project instructions, especially in team repositories and monorepos. It should not assume that Codex and Claude Code load the same filenames and instruction layers identically. The resulting project documentation must make sense for the platform being configured.

---

## 14. Installation record

Maintain a lightweight project installation record at:

**`.ai-harness/installation.yaml`**

Its purpose is to make later installation, verification, addition, and update conversations aware of the project's current harness setup.

The record should identify, as applicable:

- Which harness revision/version was used.
- Which coding platforms were configured.
- Whether required Superpowers is installed, available, or still needs attention.
- Which custom and community skills were selected and installed.
- Which MCP integrations were selected and their known readiness states.
- Which project instruction files were updated.
- Information needed to avoid duplicate installation and support future updates.

**Never record tokens, credentials, API keys, or other secrets.**

The exact metadata organization may be chosen by the implementing agent. The record must remain human-readable and must not create a complex runtime dependency.

---

## 15. Global and environment-level settings

Some useful agent capabilities depend on the platform, its version, user account, or local computer settings.

The harness should check and, where appropriate, **recommend** options related to:

- Availability and use of subagents or multi-agent execution.
- Additional or experimental collaborative-agent features, if supported.
- Long-running local tasks and ways to reduce avoidable interruption.
- Tool permissions or other settings that materially affect selected skills/MCP integrations.

**Policy:**

- Prefer existing defaults and project-local configuration.
- Do not require global changes when they are not necessary.
- Explain optional settings, benefits, side effects, and any experimental status.
- **Ask for explicit consent before changing user/global Codex or Claude settings.**
- If the agent cannot safely change a setting, give accurate manual steps instead.
- Do not promise indefinite or uninterrupted autonomous execution.
- Do not hard-code a model or model family.

The first release does not need an elaborate global-settings manager.

---

## 16. Add components after initial installation

The user must be able to expand an already configured project without running a full setup from scratch.

### 16.1 Desired user journey

Example request:

> Install additional skills and MCP integrations from my AI Dev Harness. Show me what is available and what is not yet installed.

The agent should:

1. Read the project's existing installation record and relevant instructions.
2. Consult the current harness catalog.
3. Check which components are already available.
4. Recommend components relevant to the current project and show the full list on request.
5. Ask which additional components to install.
6. Install or guide installation of the chosen items.
7. Verify them.
8. Update the managed `AI DEV HARNESS` section and installation record.
9. Clearly report any required manual action or failures.

### 16.2 Expected properties

- Repeated requests should not create duplicate skills, MCP entries, or instruction sections.
- The agent should not reinstall or update unrelated components merely because the user asked to add one tool.
- A project that acquires a new framework later should be able to add the corresponding skills and MCP integrations.
- It should be possible to ask for a particular skill by name instead of going through the entire catalog.

A dedicated user-facing document such as `ADD-COMPONENTS.md` is desirable, but the implementing agent may choose the simplest clear documentation structure.

---

## 17. Update an existing harness installation

The user must be able to ask their coding agent to update a previously configured project from the public harness repository.

### Desired behavior

1. Identify the current installation and installed components.
2. Read the current harness update guidance.
3. Compare the current setup with what is available from the requested/new version.
4. Explain relevant changes, compatibility concerns, and potential conflicts.
5. Ask before changing installed components or managed project instructions.
6. Apply the agreed updates while preserving unrelated project instructions and customizations.
7. Verify the resulting setup and update the installation record.
8. Explain any incomplete steps.

The process should not silently overwrite user-customized skills, project rules, or authentication-related configuration.

Updates should be understandable and repeatable without a bespoke migration engine for the first release.

---

## 18. Verification, failures, and recovery

The agent must validate the result of installation, component addition, or update and report problems honestly.

### 18.1 Verification expectations

Where reasonably possible, check that:

- Superpowers is installed and available to the target coding platform.
- Selected custom/community skills can be discovered and used.
- Selected MCP servers have valid configuration and can be connected to, including any required authorization.
- The `AI DEV HARNESS` section accurately represents installed/available components.
- Existing project instruction content remains intact.
- The installation record matches what was actually done.
- The setup recognizes the relevant applications in a mixed-framework repository.

Distinguish **requested**, **configured**, **installed**, **verified/ready**, **requires manual action**, and **failed**. A component that is listed in a file but cannot start must not be reported as fully working.

### 18.2 Failure handling

When an installation fails:

- State which component failed and at what point.
- Show a useful error summary and preserve relevant technical output when available.
- Offer concrete troubleshooting steps and a way to retry that component.
- Do not hide errors, invent successful checks, or mark the whole environment complete when a required component remains unavailable.
- Avoid repeating completed installation work unnecessarily.
- Do not expose secrets in displayed diagnostics or saved material.

If a tool requires a manual login, platform permission, restart, or action in the UI, explain exactly what the user needs to do and how to verify completion.

The project should include clear verification and troubleshooting documentation; **a custom diagnostics CLI is not required**.

---

## 19. Everyday usage scenarios

### Scenario A — Standard development with domain guidance

The developer opens an existing project and asks Codex to implement a feature for its technology stack.

**Expected result:** Superpowers provides the standard development approach; matching installed domain skills are loaded according to project usage rules, and irrelevant tools are not invoked. Existing conventions remain in force.

### Scenario B — Two-line fix without Superpowers

The developer asks for a tiny code fix and explicitly says not to use Superpowers or browser tools.

**Expected result:** The agent follows the explicit exclusion and solves the small task without unnecessary ceremony, subject to the platform's native behavior. No custom disabling mechanism is required.

### Scenario C — Guided programming exercise

The developer invokes `learning-dev-workflow` for a search/filtering feature.

**Expected result:** The agent discusses the task and relevant architecture at an appropriate depth, uses Superpowers for meaningful brainstorming/planning if needed, gets the learner's agreement, prepares scaffold/TODO/tests, and stops. The learner writes the implementation, requests hints as needed, and later asks for review.

### Scenario D — Very small learning task

The developer invokes `learning-dev-workflow` for a simple utility function.

**Expected result:** The agent recognizes low complexity, avoids excessive planning/subagents, creates a minimal meaningful exercise, and leaves the implementation to the learner.

### Scenario E — Missing Superpowers

The developer tries to set up the harness but Superpowers cannot be installed.

**Expected result:** The agent provides verified next steps and reports an incomplete installation. It does not falsely claim the required foundation is ready. If a learning task is later requested without Superpowers, a standalone fallback is available only by explicit choice.

### Scenario F — Mixed-technology repository

The developer installs the harness at the root of a repository with several applications and separate package manifests.

**Expected result:** The agent recognizes multiple technologies, recommends appropriate per-framework tools, configures the shared harness once, and avoids confusing one application's tools with another's.

### Scenario G — Existing AGENTS.md in a team repository

The user installs the harness where `AGENTS.md` already documents architecture and team conventions.

**Expected result:** All existing instructions remain intact; a clearly delimited `AI DEV HARNESS` section is added. Running installation/update again does not duplicate the section.

### Scenario H — Add tools later

A previously configured repository later gains a project using a different technology. The developer asks to install additional tools from the harness catalog.

**Expected result:** The agent suggests relevant missing tools from the current catalog, installs only selected additions, adds their usage rules to project instructions, and updates/verifies the record and tools.

### Scenario I — Update on another computer

The developer opens a project on a second computer and asks the coding agent to verify or update the harness.

**Expected result:** The agent can use the repository instructions and installation record to identify what is needed, including any machine-specific authorizations, without requiring a dedicated locally installed harness CLI.

### Scenario J — Optional global capability

The agent identifies a useful optional setting for longer-running tasks or collaborative agents.

**Expected result:** It explains the feature and asks before modifying global/user configuration. Declining the setting does not break unrelated installation steps.

---

## 20. Public repository documentation requirements

The repository must have a clear English README that answers, without needing this requirements document:

- What AI Dev Harness is and what it deliberately is not.
- Who it is useful for.
- How Superpowers relates to the harness.
- How installed skills are selected during tasks and where their own behavior is defined.
- How to install by sharing the GitHub URL with Codex or Claude Code.
- How component selection and project-aware recommendations work.
- How to see the full list of supported Skills/MCP integrations.
- How to add components after installation.
- How to update and verify an existing installation.
- What to do when installation fails or manual authentication is required.
- How to customize or extend the catalog and custom skills.
- How mixed-framework repositories are handled.
- What kinds of global settings might optionally be recommended.
- What limitations users should expect from agent-driven installation.

Include simple example prompts that readers can copy, without requiring long, repetitive instructions.

The repository should also contain sufficient instructions for an AI coding agent to carry out installation **without needing the historical conversation that produced these requirements**.

---

## 21. Repository organization

Keep installation/lifecycle guidance, curated registries, reusable templates and independently deployable custom skills easy to discover. Link the current implementation from the README. Generic installation and project-instruction templates must work for any selected custom skill.

---

## 22. Acceptance expectations

The initial release should be considered successful when the following outcomes can be demonstrated in realistic repositories.

### 22.1 Installation and configuration

- [ ] The user can start installation by providing the public GitHub repository URL to Codex or Claude Code.
- [ ] The agent can explain and follow the repository's installation instructions without a proprietary CLI.
- [ ] Superpowers is installed or clearly identified as a blocking missing requirement.
- [ ] Custom and community skills are offered with useful descriptions and project-aware recommendations.
- [ ] The user can view all available skills, select some, and decline others.
- [ ] MCP options are presented similarly and verified honestly.
- [ ] Existing `AGENTS.md` / `CLAUDE.md` content is preserved and a concise `AI DEV HARNESS` section includes a when-to-use rule for every available installed skill/member.
- [ ] `.ai-harness/installation.yaml` reflects the actual installation and contains no secrets.
- [ ] Repeating installation does not create duplicate managed sections or component installations.
- [ ] The installation works sensibly in an empty project, a populated project, and a mixed-framework repository.

### 22.2 Standard development

- [ ] Superpowers is used as the standard development foundation rather than a duplicate custom production workflow.
- [ ] Matching skills are selected by their own project/task rules rendered into project instructions, including when Superpowers is not used.
- [ ] Explicit requests to avoid a skill/MCP are reflected in the agent's behavior to the extent supported by the platform.
- [ ] The harness does not force a large planning process on every trivial request.

### 22.3 Guided learning

- [ ] The `learning-dev-workflow` skill is discoverable and can be explicitly invoked.
- [ ] It assesses complexity and adjusts the planning effort accordingly.
- [ ] For meaningful tasks, it can leverage Superpowers brainstorming/planning without handing off core implementation to Superpowers.
- [ ] Learning Architect/Tutor, Scaffolder, Task Annotator, QA/Test Designer, and Tutor/Reviewer responsibilities are all covered.
- [ ] The scaffold provides usable starting structures without completed feature logic.
- [ ] TODO annotations describe desired behavior without revealing complete algorithms.
- [ ] Tests are grounded in agreed requirements, not invented implementation details.
- [ ] The learner retains control of implementation and receives one of the four assistance levels according to the request; full solutions stay in the response unless file edits are separately requested.
- [ ] Review explains findings without automatically replacing learner-owned code.
- [ ] Learning documentation is concise and educational, rather than a standard Superpowers implementation plan.

### 22.4 Lifecycle and reliability

- [ ] The user can add previously declined Skills/MCP integrations later.
- [ ] The user can request an update and receive a clear preview of changes.
- [ ] Optional global settings are explained and changed only after consent.
- [ ] Failures, missing permissions, and manual authorization steps are reported with useful next actions.
- [ ] Verification distinguishes configuration from actual operational readiness.
- [ ] The English README makes installation, usage, addition, updates, and troubleshooting understandable to a new user.

---

## 23. Guidance to the implementing AI agent

Use this document as a **product requirements source**, not as a ready-made implementation plan.

Before implementing:

1. Review the current documentation and actual capabilities of Codex, Claude Code, Superpowers, and the selected community tooling.
2. Identify gaps, conflicts, unsupported assumptions, and any aspects that may behave differently across platforms.
3. Propose a **minimal, maintainable solution** that fulfills the desired user experience.
4. Prefer native agent/platform features and documented installation workflows over custom code.
5. Confirm material product-level ambiguities with the project owner before making irreversible or unexpectedly broad changes.

During implementation:

- Keep all public repository content in English.
- Prioritize **end-to-end usability** over adding files or abstractions.
- Preserve existing project instructions when configuring target repositories.
- Clearly separate required components from optional recommendations.
- Avoid overstating guarantees about autonomous agents, skill invocation, or plugin precedence.
- Keep the custom Learning Mode learner-centered and prevent inadvertent AI completion of exercises as far as the supported tooling permits.
- Ensure update and add-component experiences are considered alongside first-time installation.

The owner delegates the **technical design, file organization, implementation approach, and concrete integration choices** to the implementing agent. Deliver the agreed outcomes in a simple, maintainable form.

---

## 24. Final product statement

**AI Dev Harness should make a curated personal AI development environment easy to install, understand, reuse, extend, and keep current across repositories and computers.**

Superpowers provides the default engineering methodology. The personal registry supplies optional skills and MCP integrations for relevant technologies and tasks. Each installed skill has a concise usage rule in project instructions and defines its own behavior, allowing the catalog to grow without changing generic setup procedures.

The intended product is a **small, clear, public, agent-readable GitHub repository—not another complex development platform**.
