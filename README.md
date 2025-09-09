# Average Refactor Demo

This tiny project lets you practice refactoring using two near-duplicate functions:
- `average_age(ages: list[float]) -> float`
- `average_score(scores: list[float]) -> float`

You'll start from the **function stubs** (raise `NotImplementedError`), write the simplest implementation (Green), then **refactor** by extracting shared logic and eventually using a better built-in (`sum`).

## Install & Test (Poetry)

```bash
poetry install
poetry run pytest -q
```

To run only the performance demo (prints timing info):
```bash
poetry run pytest -q -k perf
```

> The perf test is for demonstration; it does not assert a strict speed ratio to avoid flakiness across machines.
