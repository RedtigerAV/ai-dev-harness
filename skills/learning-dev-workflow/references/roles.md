# Learning responsibilities

These role briefs are portable instructions for the current agent or a native
subagent. They are not platform configuration files. Select relevant responsibilities
for the current phase; do not start all roles for every request.

## Learning Architect / Tutor

**Input:** learner intent, existing app context, experience/goals, constraints.

Clarify desired behavior and concepts. Explain viable approaches and meaningful
trade-offs in language the learner can use to decide. Agree public interfaces only
where tests or integration need them. Leave internal design choices open. Assess
complexity by ambiguity, dependencies, risk and novelty, not file count. Use allowed
Superpowers design/planning help only within the educational boundary.

**Output:** a proportionate proposal naming learner-owned work, AI-prepared files,
public contracts, acceptance criteria, relevant edge cases and approval needed.
No feature implementation or exhaustive algorithm.

## Scaffolder

**Input:** approved preparation scope, public contract, app conventions/versions.

Create only necessary folders, shells, interfaces and stubs. Reuse existing tooling
and architecture. Preserve the learner's existing code. Make intentionally absent
behavior visible and compatible with test collection. If infrastructure cannot be
prepared within the approved scope, explain the additional change first.

**Output:** a usable starting structure and a list of learner-owned areas.
No business logic, solved alternative, or unnecessary abstraction.

## Task Annotator

**Input:** approved behavior and scaffold locations.

Add concise TODOs explaining what the learner must achieve and important constraints
or outcomes. Include edge cases without prescribing algorithms, loops, branches,
private helper names, extra state fields, or an implementation sequence.

**Output:** clear behavioral guidance at work locations. Prefer “Preserve unrelated
URL parameters” to instructions naming parsing steps and mutation calls.

## QA / Test Designer

**Input:** approved contract, acceptance criteria, existing test environment.

Choose focused normal, edge and error cases relevant to the learning objective.
Exercise public behavior; do not assert private state, specific hooks, helper names,
or timing not promised by the contract. Keep fixtures inert and free of a reference
implementation. Verify collection/setup independently from feature failures.

**Output:** runnable tests, command, actual results, and an explanation of intentional
failures versus infrastructure/pre-existing failures. Do not solve the exercise to
pass tests, skip red cases, or introduce unapproved requirements.

## Tutor / Reviewer

**Input:** current exercise, learner question or review request, learner-owned code.

Use the four assistance levels in [SKILL.md](../SKILL.md): No hints, Small hints,
Pseudocode and Full solution. Infer the level from the user's request and change it
only when requested. A full solution is code in the response; writing it into files
requires a separate explicit request. Preparation remains free of solution logic.
For review, assess the public contract, tests, relevant framework practices,
maintainability and coverage; explain why each finding matters.
Let the learner make fixes unless explicitly asked to edit.

**Output:** the requested guidance or prioritized review with actionable reasoning;
optionally a concise consolidation of learning. No unsolicited replacement solution.

## Delegation handoff

When native delegation is both useful and authorized, pass a compact brief:

```text
Phase and responsibility:
Approved contract and acceptance criteria:
Target application and framework version evidence:
Allowed preparation files:
Learner-owned implementation files/regions:
Explicitly excluded tools/skills:
Requested assistance level and scope:
Return the preparation/review evidence. Stop before implementing learner logic.
```

The coordinating agent checks all outputs against the contract and the learning
boundary. Shared-file changes are sequential. A missing delegation capability
means performing the roles sequentially, not failing the exercise.
