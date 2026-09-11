# Running the evals

Two independent eval suites live under `faq_automation/evals/` — see
[`faq_automation/evals/README.md`](../faq_automation/evals/README.md) for the
full methodology (how cases are picked, check predicates, failure analysis).
This doc is just the terminal commands. All commands run from the repo root.

## 1. Search eval (retrieval only, no LLM calls, ~2s)

```bash
uv run --project faq_automation python -m faq_automation.evals.run_search_eval
```

No API key needed. Prints recall@k / MRR@k / hit_rate@k over the 25 retrieval
challenge cases.

## 2. RAG eval (full pipeline: search + LLM decision + content generation, ~2min)

**Plain version** — runs all 61 cases on the flex tier, prints PASS/FAIL per
case plus a pattern/tag failure breakdown, exits nonzero on any failure:

```bash
uv run --project faq_automation python -m faq_automation.evals.runner
uv run --project faq_automation python -m faq_automation.evals.runner --case 289   # one case only
uv run --project faq_automation python -m faq_automation.evals.runner --batch      # Batch API, same price, hours not minutes
```

Needs `OPENAI_API_KEY`.

**Opik-tracked version** — a smaller, cheap "Friday-demo" subset (6 of the 61
cases, deterministic `action_match` + `placement_match` scoring, no judge-model
cost) run through `opik.evaluate()` so before/after comparisons (e.g. changing
`num_results`) land as comparable Experiments on Comet Opik Cloud instead of
only a terminal report. This does **not** run the full 61-case suite or the
per-case content-quality checks (code correctness, formatting, etc.) that
`runner.py` enforces — it's a fast, deterministic sanity check for prompt/
retrieval changes, not a replacement for the full suite.

```bash
source .env   # OPENAI_API_KEY, OPIK_API_KEY

# one-time: push the demo cases to the Opik dataset (skips insert if already there)
OPIK_URL_OVERRIDE=https://www.comet.com/opik/api OPIK_WORKSPACE=default \
  OPIK_PROJECT_NAME=faq-automation-ci \
  uv run --project faq_automation python -m faq_automation.evals.opik_eval --push-dataset

# before/after
uv run --project faq_automation python -m faq_automation.evals.opik_eval \
  --experiment friday-before --num-results 1
uv run --project faq_automation python -m faq_automation.evals.opik_eval \
  --experiment friday-after --num-results 5
```

(`OPIK_URL_OVERRIDE` / `OPIK_WORKSPACE` / `OPIK_PROJECT_NAME` only need setting
once per shell — put them in `.env` if you run this often. See
[docs/opik.md](opik.md) for the full platform/workspace table and the rest of
the Opik integration — tracing, prompt library, history backfill.)

### Where to see the results

- **Terminal**: `runner.py` prints a `PASS`/`FAIL` line per case, a summary
  count, and pattern/tag failure breakdowns. `opik_eval.py` prints a metrics
  table and, at the very end, `experiment '<name>' done: ...` with an
  `experiment_url` you can open directly.
- **Comet Opik Cloud**: https://www.comet.com/opik → workspace → project
  `faq-automation-ci` → **Datasets** tab (`faq-triage-friday`) for the raw
  cases, or **Experiments** tab to select multiple runs (e.g. `friday-before`
  vs `friday-after`) and diff their `action_match` / `placement_match` scores
  side by side.
