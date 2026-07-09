# FAQ Automation Evals

Two eval suites for the FAQ merge agent, each testing a different layer.

## Overview

| Eval | What it tests | Cases | Runtime | Metrics |
|------|--------------|-------|---------|---------|
| **Search eval** (`run_search_eval.py`) | Retrieval layer (minsearch index) in isolation — no LLM calls | 67 | ~4s | recall@k, MRR@k, simulated action accuracy |
| **RAG eval** (`runner.py`) | Full pipeline (search + LLM decision + content generation) | 39 | ~70s | action correctness, section placement, code quality, formatting |

## Search eval (`run_search_eval.py`)

Tests retrieval in isolation — no LLM calls, runs in ~4 seconds. Lets us
iterate on index configuration (text fields, boosts) and immediately see the
impact on recall and simulated action accuracy.

```bash
uv run --project faq_automation python -m faq_automation.evals.run_search_eval
```

### How it works

Each eval case is a real GitHub issue (the question a student asked) paired with
the `doc_id` of the FAQ entry that was eventually created from it. For example,
issue #289 ("Why do I get IndexError: list index out of range?") became FAQ entry
`1a7b27c4df` in `module-2-vector-search`.

The search index is the current `_questions/` directory, which already contains
that entry (we merged it). This creates a problem: if we just search the index,
the query will trivially match the entry's own question text. To get meaningful
results, we run two passes:

**FIND pass** — the target doc stays in the index.

This simulates a future student asking a similar question. If a student asks
"Why do I get IndexError when accessing chunks?", the search should surface
the existing FAQ entry `1a7b27c4df` so the agent can mark it as DUPLICATE
instead of creating a redundant new entry. We measure whether the target
doc appears in the top-k results (recall@k) and how high it ranks (MRR@k).

If the FIND pass fails (recall miss), it means the search can't find an
existing entry even when it's there — genuine duplicates would slip through
as NEW.

**NOISE pass** — the target doc is removed from the index.

This simulates the state the agent was in when the proposal was first
processed: the entry didn't exist yet. The question is: what does the search
return instead? If the top results are strong matches from the same topic
(e.g. other vector-search entries about embeddings or chunking), the LLM
might look at them and decide "this is already covered" — calling DUPLICATE
on a genuinely NEW question. That's a false positive.

We don't have a single-number metric for the NOISE pass. Instead we show what
the top-5 results are when the target is removed, so we can spot cases where
topical keyword overlap creates false confidence. This is the more important
pass for improving NEW/DUPLICATE discrimination.

### Metrics

- **recall@k** (same as hit rate with one relevant doc): did the search surface
  the relevant doc in the top-k? This directly controls DUPLICATE detection.
  Low recall means genuine duplicates slip through as NEW.
  Baseline: recall@5 = 0.830

- **MRR@k**: mean reciprocal rank of the relevant doc. Higher is better — the
  relevant doc should appear early so the LLM sees it in context.
  Baseline: MRR@5 = 0.777

- **Simulated action accuracy**: if the relevant doc is in top-5 -> FOUND
  (should be DUPLICATE/UPDATE), otherwise -> NEW. Cheap proxy without needing
  the LLM.
  Baseline: 0.830 (39/47)

Note: with a single relevant doc per case, precision@k would just be recall/k,
which is not informative. The NOISE eval (doc removed) covers the false-positive
side by showing what the search returns when nothing relevant exists.

### The historical-data problem

Our eval cases come from real GitHub issues — proposals that students submitted
through the FAQ form. We merged the resulting FAQ entries after processing them,
so the answer already exists in the current index.

We handle this with the two-pass design above: FIND (doc in index) tests whether
the search can find an entry that exists, and NOISE (doc removed) simulates the
"before" state to test false-positive risk for genuinely new proposals.

### Tuning harness (`tune_search.py`)

Sweeps boost configurations and text-field selections against the same cases.
No LLM calls, runs all configs in seconds.

```bash
uv run --project faq_automation python -m faq_automation.evals.tune_search
```

Key finding: removing `section` from text_fields (keeping only `question` and
`answer`) improved recall from 0.745 to 0.830. The section name was adding noise
— queries mentioning "Docker" would match the section name "Module 1: Docker"
even for unrelated entries.

## RAG eval (`runner.py`)

Tests the full pipeline end-to-end: search + LLM decision + content generation.
Each case is a real issue proposal processed through the agent, then checked
against expected outcomes.

```bash
uv run --project faq_automation python -m faq_automation.evals.runner
```

### How it works

Each case is a real issue with known ground truth (the action, section, and
content quality expected). The runner:

1. For NEW cases: **hides the target doc** from a temporary copy of the course
   directory, so the agent can't trivially find it as a duplicate. This
   simulates the state the agent was in when the proposal was first processed.
2. For DUPLICATE cases: runs against the full index (doc is present).
3. Runs the agent end-to-end and checks the decision against expected outcomes.

### What it checks

- **Action correctness**: NEW, UPDATE, or DUPLICATE — does the agent make the
  right call?
- **Section placement**: does the entry land in the right section? The agent
  uses the SECTIONS metadata (with comment fields describing what belongs
  where), not the search results, for this decision.
- **Content quality**: is the code runnable (all variables defined)? Are there
  structural headers? Is the answer concise? Is the filename slug present?
- **Sort order**: the collision-safe `_shift_section_files` logic should prevent
  any sort_order collision.

### The historical-data problem

Same as the search eval: entries we merged already exist in the FAQ. For DUPLICATE
cases this is correct — the agent should find and cite the existing entry. For NEW
cases, we hide the target doc (see above) so the agent sees the "before" state.

What we can and can't test:
- **Can test**: section placement (always testable regardless of whether the
  entry exists), content quality (code, headers, formatting), sort order
  handling, rejection of irrelevant proposals.
- **Can't test**: whether the agent would correctly choose NEW for a question
  whose answer is already in the FAQ (it should say DUPLICATE, and it does).
  The doc-hiding trick handles most of these cases.

### Tags

Each case has tags for failure analysis:
`duplicate-detection`, `section-misplacement`, `code-quality`,
`content-formatting`, `correct-new`, `false-duplicate`, `relevance`,
`duplicate-verify`, `dlt`, `bruin`, `verbosity`, `filename-slug`.

## Adding cases

### Search cases

Add a tuple to `search_cases.py`:

```python
("course", "query text", "relevant_doc_id", issue_number, "optional note")
```

Use doc_id `"NONE"` for negative cases. To find the doc_id for a merged entry:
`grep -r '<question text>' _questions/` or check the file's frontmatter `id`.

### RAG cases

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
    relevant_doc_id="abc1234567",  # hidden from index for NEW cases
)
```

Available check predicates: `action_is`, `section_is`, `no_structural_headers`,
`content_is_runnable_python`, `content_is_concise`, `has_filename_slug`,
`has_trailing_newline`, `content_has_no_bold_headers`, `no_sort_order_collision`.

## Changes made during this session

- **Removed `section` from search text_fields**: the section name ("Module 1:
  Docker") was being tokenized and matched against queries, causing false matches.
  Keeping only `question` and `answer` as text fields improved recall 0.745 -> 0.830.
- **Improved agent prompt**: explicit tool-to-section mapping (dlt -> workshop,
  Bruin -> module-5, DuckDB -> module-4), section placement based on SECTIONS
  metadata not search results, content quality rules (define all code variables,
  no structural headers, concise answers), rejection of transient questions.
- **Collision-safe sort order**: `_shift_section_files` bumps existing entries
  when a new entry collides, so the agent can freely place entries by logical
  position without manual renumbering.
- **Removed 4 real duplicate FAQ entries**: ML Zoomcamp HPA (module-6 copy),
  ML Zoomcamp deployment (module-6 copy), MLOps MLflow exception (duplicate),
  MLOps cohort diff (outdated 2022/2023 entry).
