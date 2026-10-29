# Scope and boundary examples

These examples calibrate preparation, not fixed templates for every framework.

## Trivial utility

Learner: “Help me practice a function that clamps a number to an inclusive range.”

A short proposal can agree `clamp(value, min, max)`, finite numeric inputs,
`min <= max`, and tests for values inside/below/above the range and equal boundaries.
Ask about invalid inputs only if they are part of the objective. Do not silently
add exceptions, coercion, or a particular internal algorithm. Ask to prepare this
scope if not already approved. Skip brainstorming and subagent ceremony.

After approval, a suitable JavaScript scaffold is:

```js
export function clamp(value, min, max) {
  // TODO: Return a value within the agreed inclusive bounds.
  // Preserve inputs that already satisfy the range.
  throw new Error('Not implemented: clamp');
}
```

In a project already using `node:test`, behavior checks can include:

```js
import test from 'node:test';
import assert from 'node:assert/strict';
import { clamp } from './clamp.mjs';

test('preserves an in-range value', () => {
  assert.equal(clamp(3, 1, 5), 3);
});

test('returns the lower bound below the range', () => {
  assert.equal(clamp(-2, 1, 5), 1);
});
```

Complete the agreed case coverage, run the project's actual test command, and report
the deliberate “Not implemented” failures. Do not insert a solved clamp into a
fixture or change tests to accept the exception. Do not add this runner to a project
already using another one simply to match the example.

## Paginated data reader

Determine the language, runtime, data source and existing test tooling. Clarify
whether the objective is iteration, asynchronous behavior, error handling or several
of these. Discuss useful architectural trade-offs without choosing the learner's
internal algorithm.

Agree the public contract: page size, ordering, empty/end-of-data behavior, and any
required handling of failed reads. Do not invent retry counts, concurrency rules
or a dependency solely to demonstrate a pattern.

Prepare approved interfaces/stubs and tests against public behavior. Fixtures can
contain fixed pages; they must not implement the reader. Behavioral TODOs describe
what to achieve without revealing the algorithm. Do not invoke an execution workflow
to make intentionally failing exercise tests pass.

## A task inside a mixed repository

If the exercise targets `services/catalog`, inspect that service's language and
dependency versions, build/test tools and applicable instructions. Guidance for
another application is relevant only when the exercise spans it. Use the target's
existing testing conventions and avoid dependency migrations during preparation.

## Choosing assistance from requests

- “Let me solve it without hints”: prepare the agreed exercise and stop; do not add
  unsolicited questions that reveal a solution direction.
- “Give me a small hint about the last page”: offer one focused concept or question.
- “Show pseudocode for the termination condition”: provide pseudocode for that part,
  not a complete implementation of the reader.
- “Show the full solution”: provide complete code for the requested scope in the
  response, leaving files unchanged. “Now apply that solution to the reader file”
  separately authorizes those specific file edits.
- “Review my solution”: inspect/test and explain findings at the current assistance
  level; do not treat review as a request for a full solution or automatic fixes.

If the learner explicitly switches to ordinary implementation, acknowledge the
mode change and clarify remaining scope ambiguity rather than imposing an exercise.
