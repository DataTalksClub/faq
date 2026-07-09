# FAQ Automation Evals

Two eval suites for the FAQ merge agent, each testing a different layer:

## 1. Search retrieval eval (`run_search_eval.py`)

Tests the **retrieval layer** (minsearch index) in isolation — no LLM calls.

For each case (a real issue question paired with the doc_id of the FAQ it became),
it runs two measurements:

- **FIND eval**: with the target doc in the index, can the search find it?
  Reports hit@k and MRR@k. Low scores mean the agent would fail to detect
  DUPLICATEs.
- **NOISE eval**: with the target doc removed, what comes back instead?
  If the top results are strong matches from the same topic, the agent would
  wrongly call DUPLICATE on a genuinely NEW question.

```bash
uv run --project faq_automation python -m faq_automation.evals.run_search_eval
```

Cases live in `search_cases.py` — real issue questions + synthetic edge cases
(vague queries, cross-module confusion, exact error strings, paraphrases).

## 2. Merge agent eval (`runner.py`)

Tests the **full pipeline** (search + LLM decision + content generation).

Each case is a real issue proposal. The agent processes it end-to-end and the
output is checked against expected outcomes: correct action (NEW/UPDATE/DUPLICATE),
correct section placement, no sort_order collisions, runnable code, no structural
headers, etc.

```bash
uv run --project faq_automation python -m faq_automation.evals.runner
```

Uses the current `_questions/` state — no historical snapshots. If an entry
already exists, the correct agent behavior is DUPLICATE.

Cases live in `cases.py`. Each case has tags for failure analysis
(`section-misplacement`, `code-quality`, `content-formatting`, etc.).

## Adding cases

### Search cases
Add a tuple to `search_cases.py`:
```python
("course", "query text", "relevant_doc_id", issue_number, "optional note")
```
Use doc_id `"NONE"` for negative cases (should return no strong match).

### Merge agent cases
Add an `EvalCase` to `cases.py`:
```python
EvalCase(
    course="llm-zoomcamp",
    issue_number=123,
    question="...",
    answer="...",
    expected_action="NEW",
    expected_section="module-3",
    checks=[action_is("NEW"), section_is("module-3")],
    tags=["section-placement"],
)
```
