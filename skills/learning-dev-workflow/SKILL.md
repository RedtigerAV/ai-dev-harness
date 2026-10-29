---
name: learning-dev-workflow
description: Prepare guided programming exercises with agreed contracts, minimal scaffolds, behavioral tests, progressive hints, and review while the learner writes the implementation. Use when the user requests learning mode or an exercise to implement personally, in any programming language or technology stack.
---

# Learning development workflow

The learner normally writes the core functionality. Prepare an understandable
exercise and provide support at the user's chosen assistance level. A requested
full solution is shown in the response; editing implementation files requires a
separate explicit request.
Use the user's conversation language. Keep repository materials in English unless
the repository or user requests otherwise.

## Choose the current phase

For a new exercise, follow understand → agree → prepare → stop. For assistance or
review of an existing exercise, go directly to that phase; do not regenerate the
scaffold or overwrite learner work. Read [the role definitions](references/roles.md) for the
responsibility being performed. All five responsibilities are covered even when
one agent performs them sequentially.

1. **Understand.** Inspect the relevant application, framework version, conventions,
   existing code/tests, and learner goals. Identify ambiguity, dependencies, risks,
   architecture choices, and unfamiliar concepts. Explain complexity briefly:

   | Complexity | Preparation effort |
   | --- | --- |
   | Trivial | A short contract and small scaffold/test; no elaborate planning or agents |
   | Small | Brief behavior/edge-case agreement and a lightweight learning plan |
   | Medium | Discuss meaningful architecture choices and use relevant design/planning help |
   | Complex | Resolve requirements, dependencies, risks and trade-offs before preparation |

   File count alone is not complexity. Ask only questions needed to establish the
   exercise and public contract. Match guidance to the actual language/tool versions.
   Determine the assistance level from the user's request using the table below;
   carry it forward without silently escalating it.

2. **Check the foundation and exclusions.** Inspect available Superpowers skills,
   not merely installation records. If unavailable, explain the limitation and
   offer restoration or a simplified standalone learning fallback. Proceed with
   that fallback **only when explicitly chosen**; do not install global tooling
   on the strength of an exercise request. A prompt explicitly saying to proceed
   without Superpowers is already that choice. If installed but excluded for this
   task, honor the exclusion and identify the standalone approach.

   For medium/complex tasks, use Superpowers brainstorming/design/planning when it
   materially helps and is available and allowed. Before invocation, constrain its
   output to an **educational preparation plan**. Do not accept an automatic handoff
   to feature implementation, executing implementation plans, or implementation
   subagents. If the installed workflow cannot respect this boundary, explain the
   conflict and use an explicitly chosen standalone approach. Small tasks can skip
   brainstorming without making an otherwise complete installation incomplete.

3. **Agree.** Present the behavior to build, concepts practiced, learner-owned work,
   AI-prepared files, necessary public interfaces, acceptance criteria and edge
   cases. Leave internal design decisions to the learner. Show enough scope to
   obtain informed approval before meaningful file changes. A trivial exercise
   needs only a sentence or two. Existing explicit approval of this exact contract
   and scaffold is sufficient; a generic “help me learn” is not scope approval.

4. **Prepare only the approved scope.** Create minimal shells/interfaces, behavioral
   TODOs, and tests using the existing project architecture and runner. Stubs may
   throw a clear “Not implemented” error where appropriate. Keep scaffold files,
   tests and preparation notes free of business logic, solution algorithms, hidden
   solved examples and solution-bearing fixtures. A requested full solution belongs
   separately in the response, as defined below. Explain a new test dependency before
   changing the approved scope. Do not create production architecture for ceremony.

   Tests assert approved public behavior, never guessed private methods, fields,
   internal control flow, or framework-version assumptions. Run them: test files
   must load and collect, with intentional failures attributable to missing behavior.
   Missing imports, invalid syntax, or broken fixtures are preparation defects to
   fix; pre-existing unrelated failures should be reported separately. Do not
   implement the exercise to turn its expected failures green. Do not skip tests
   or mark them expected failures merely to present a green result.

5. **Audit and stop.** Inspect all changes for accidental solution leakage, including
   comments, helpers, fixtures and planning notes. Confirm the public contract and
   learner ownership remain intact. Hand off files, the exact test command, actual
   expected failures, acceptance criteria and where to start. State that preparation
   is complete and file implementation belongs to the learner. **Stop preparation
   here**, even if a general workflow would continue until tests pass. Provide any
   explicitly requested assistance separately in the response at the chosen level.

Use [the exercise examples](references/examples.md) when calibrating scope or test
boundaries. A tiny exercise can live entirely in chat plus its scaffold/tests.
Larger tasks may use a concise task brief and conceptual guide in the project's
existing documentation location. Do not generate a normal Superpowers implementation
plan or detailed solution algorithm as part of preparation.

## Four assistance levels

Choose the level from the request, including natural-language instructions. A later
explicit request can change it. Keep the level within the requested portion of the
exercise; assistance never authorizes file edits by itself.

| Level | What to provide | Example request |
| --- | --- | --- |
| No hints | Agreed brief, public contracts, scaffold/tests and requested evaluation; no solution guidance | “Let me solve it myself; no hints.” |
| Small hints | A focused question or conceptual nudge, without an algorithm or solution code | “Give me a small hint.” |
| Pseudocode | Language-independent steps for the requested part, without a copy-paste implementation | “Show pseudocode for the boundary cases.” |
| Full solution | Complete working code and explanation for the requested scope **in the response** | “Show me the full solution.” |

If no level has been established for the exercise, use **No hints** during
preparation and **Small hints** for a generic request for help. Do not ask for a choice when the
request already establishes it. Clarify genuinely ambiguous requests to disclose a
solution rather than escalating from a smaller hint automatically.

No hints does not remove agreed TODOs, contracts or test feedback. Preparation
still stops at the scaffold at every level: even a Full solution preference does
not put solved logic into scaffold files, fixtures, comments or planning artifacts.
When a full solution is requested, present it separately in the response. Do not
write it to files unless the user separately and explicitly requests those edits;
once requested, limit changes to that scope. Do not use that request to solve
unrelated parts of the exercise or to trigger autonomous workflow execution.

## Review and consolidation

- **Review on request:** read the agreed contract and learner's changes; run relevant
  existing tests. Explain prioritized findings with locations, observed behavior,
  reasons, and directions for improvement. Check correctness, edge cases,
  architecture, supported framework practices, maintainability, and coverage.
  Review is not authorization to repair or replace learner code. Separate real
  defects from stylistic preferences or unapproved requirements.
- **Consolidate:** briefly connect what the learner practiced with future uses,
  including remaining gaps. Respect the current assistance level; a review request
  alone does not request a full solution.

## Native roles and continuity

Use the five roles as responsibilities, not a requirement to spawn five agents.
For larger approved preparation tasks, native delegation may help if available and
authorized by the active environment. Do not create a new runtime or persist custom
platform agent definitions just for this skill. In every delegated instruction pass
the contract, allowed files, learner-owned implementation, exclusions, requested
hint level, and the stop-before-implementation boundary. Sequence work that shares
files; inspect outputs before handoff. Inherit the user's model settings.

When resuming, reconstruct the agreed contract, current phase, approved changes,
learner progress, and hint level from available context. If an essential approval
cannot be established, ask; do not treat elapsed time as consent. These instructions
guide behavior under native platform permissions and cannot enforce an unbreakable
boundary against other plugins.
