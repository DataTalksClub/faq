# FAQ Automation Evals

Two eval suites for the FAQ merge agent, each testing a different layer of the
pipeline.

## The historical-data problem

Our eval cases come from real GitHub issues — proposals that students submitted
through the FAQ form. For each issue we know the ground truth: which FAQ entry
it became (for NEW/UPDATE) or which existing entry it duplicated (for DUPLICATE).

The challenge is that we merged those entries into the FAQ after processing them.
So when we run the eval against the current `_questions/` directory, the answer
already exists in the index. This creates two problems depending on what we're
measuring:

1. **For the RAG/merge agent eval**: the agent sees the entry and correctly calls
   DUPLICATE — but the original issue was supposed to create a NEW entry. We can't
   evaluate whether the agent would have made the right NEW decision if the entry
   didn't exist yet, because it does.

2. **For the search retrieval eval**: if the target doc is in the index, the search
   trivially finds it by keyword overlap with its own question text. That measures
   self-match, not retrieval quality.

### Our solution

We handle this differently per eval suite:

**Search eval** — run each query twice:

- **FIND**: keep the target doc *in* the index. This tests whether the search would
  surface the right entry if a student asks a similar question later (the DUPLICATE
  detection use case). Metric: hit@k, MRR@k.
- **NOISE**: *remove* the target doc from the index, then search. This tests what
  the agent saw when the proposal was first processed (the doc didn't exist yet).
  If the top results are strong same-topic matches, the agent would have been
  tempted to call DUPLICATE on a genuinely NEW question — a false positive.

This two-pass approach lets us evaluate both DUPLICATE detection (FIND) and
NEW discrimination (NOISE) using the current FAQ corpus without needing historical
git snapshots.

**RAG/merge agent eval** — run against the current FAQ state and accept the
tradeoff that entries which already exist will be marked DUPLICATE by the agent.

What we measure vs what we skip:

- **Action decision (NEW vs DUPLICATE)**: for cases where the answer is already
  in the FAQ, a DUPLICATE response is correct — we can't test whether the agent
  would have correctly chosen NEW in the original "before" state. For cases where
  the answer should NOT be an FAQ entry (irrelevant proposals, transient questions),
  we still test that the agent rejects them.
- **Section placement**: always testable. If the agent returns NEW or UPDATE, the
  section it picks must be correct regardless of whether the entry exists.
- **Content quality**: always testable. When the agent generates content, we check
  that code is runnable, headers are absent, answers are concise, and the filename
  slug is present.
- **Sort order collision**: always testable via the collision-safe
  `_shift_section_files` logic — the agent should never produce a duplicate
  sort_order.

In the future we could snapshot `_questions/` at per-case base commits to recreate
the exact "before" state, but the current approach is simpler and still surfaces
the dominant failure patterns (section misplacement, code quality, formatting).

## Metrics and what to optimize

The search layer feeds the LLM the top-k results. The LLM then decides the action
(NEW/UPDATE/DUPLICATE) and the section placement. We measure three things:

### recall@k — can the search find the right doc? (DUPLICATE detection)

For positive cases (the relevant doc IS in the index): did the search surface it
in the top-k? This directly controls DUPLICATE detection. Low recall means genuine
duplicates slip through as NEW.

Baseline: recall@5 = 0.745

### section_acc@k — do the results point to the right section? (section placement)

For each result in the top-k, is it from the same section as the target doc?
This is the metric that predicts RAG pipeline section-misplacement failures.
The LLM picks its section based on where the retrieved results live — if the
search returns results from the wrong section, the LLM follows. We found that
13 of 19 RAG eval failures were section misplacement caused by the search
returning wrong-section results.

**This is the primary metric to optimize.** Even if the exact doc isn't in the
top-k (recall miss), if the top results are from the right section, the LLM is
likely to place the new entry correctly.

Baseline: section_acc@5 = 0.477, top1_section_hit = 0.745

### top1_section_hit — does the single strongest result point the right way?

The top-1 result dominates the LLM's context window. If it's from the wrong
section, it anchors the LLM toward a wrong placement even when lower-ranked
results are correct.

Baseline: top1_section_hit = 0.745 (llm-zoomcamp 0.947, data-engineering 0.667)

### The combined metric: simulated action accuracy

We simulate the action decision from search results alone (no LLM): if the
relevant doc is in top-5 -> FOUND (should be DUPLICATE/UPDATE), otherwise -> NEW.
This is a cheap proxy for the full RAG pipeline's action accuracy.

Baseline: 0.745 (35/47 positive cases correctly FOUND)

### The evaluation challenge: most queries are NEW

Most proposals the bot processes are NEW — the relevant doc doesn't exist yet.
For those, the search is NOT expected to return a relevant doc. Traditional IR
metrics (precision/recall) assume every query has at least one relevant doc.

We handle this with the two-pass design:
- FIND eval (positive cases): doc IS in the index. We measure recall and section accuracy.
- NOISE eval (doc removed): simulates the NEW state. We measure false-positive risk:
  does the search return same-section matches that would trick the LLM into DUPLICATE?

The NOISE eval doesn't have a single number metric yet — it reports the rate at
which the top-1 result comes from the same section as the (removed) target, which
indicates false-positive risk.

## 1. Search retrieval eval (`run_search_eval.py`)

Tests the **retrieval layer** (minsearch index) in isolation — no LLM calls, runs
in seconds.

```bash
uv run --project faq_automation python -m faq_automation.evals.run_search_eval
```

Cases live in `search_cases.py` — real issue questions paired with ground-truth
doc_ids, plus synthetic edge cases (vague queries, cross-module confusion, exact
error strings, paraphrases, negative cases).

## 2. Merge agent eval (`runner.py`)

Tests the **full pipeline** (search + LLM decision + content generation). Each
case is a real issue proposal processed end-to-end.

```bash
uv run --project faq_automation python -m faq_automation.evals.runner
```

Cases live in `cases.py`. Each case has tags for failure analysis
(`section-misplacement`, `code-quality`, `content-formatting`, etc.).

## Adding cases

### Search cases

Add a tuple to `search_cases.py`:

```python
("course", "query text", "relevant_doc_id", issue_number, "optional note")
```

Use doc_id `"NONE"` for negative cases (query that should return no strong match).
To find the doc_id for a merged entry: `grep -r '<question text>' _questions/` or
search the file's frontmatter `id` field.

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

Available check predicates: `action_is`, `section_is`, `no_structural_headers`,
`content_is_runnable_python`, `content_is_concise`, `has_filename_slug`,
`has_trailing_newline`, `content_has_no_bold_headers`, `no_sort_order_collision`.
