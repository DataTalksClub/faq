# FAQ Automation Evals

Two eval suites for the FAQ merge agent, each testing a different layer.

## The feedback loop

The evals are part of a continuous improvement loop:

1. New FAQ proposals arrive as GitHub issues. The bot processes them
   automatically (search + LLM decision + PR creation).
2. A human reviews the PRs using the `pr` skill (`.claude/skills/pr/SKILL.md`),
   which checks section placement, duplicates, sort order collisions, content
   quality, and code correctness. Problems are fixed before merging.
3. The fixes reveal patterns the bot gets wrong. These become new eval cases:
   the issue question/answer becomes the input, the corrected outcome becomes
   the expected result, and the failure pattern becomes a tag.
4. The search eval and RAG eval are run to measure the bot's performance on
   the accumulated cases. The search eval (fast, no LLM) tunes the index.
   The RAG eval (slow, full pipeline) validates end-to-end.
5. Based on eval results, the agent prompt, search index config, or section
   metadata comments are adjusted. The evals are re-run to confirm the fix
   worked without regressing other cases.

This loop means PR reviews directly improve the bot — human corrections that
represent recurring patterns become permanent regression tests.

We don't add every correction as a test case. We select cases that:

- Represent a recurring pattern (not a one-off mistake), so fixing it helps
  broadly. For example, the bot repeatedly placed dlt questions in module-3
  instead of the workshop — one representative case covers the pattern.
- Cover diverse scenarios: different courses, different sections, different
  action types (NEW vs DUPLICATE vs UPDATE), different failure modes
  (section placement, code quality, false duplicates, content formatting).
- Have a clear, unambiguous expected outcome that can be checked
  programmatically (correct section, correct action, runnable code).

## Overview

| Eval | What it tests | Cases | Runtime | Metrics |
|------|--------------|-------|---------|---------|
| Search eval (`run_search_eval.py`) | Retrieval layer (minsearch index) in isolation — no LLM calls | 67 | ~4s | recall@k, MRR@k, hit_rate@k |
| RAG eval (`runner.py`) | Full pipeline (search + LLM decision + content generation) | 39 | ~70s | action correctness, section placement, code quality, formatting |

Current results: 29/39 pass (74%). Remaining failures are mostly action
decisions (false DUPLICATE on genuinely new proposals) and content quality
(code variables undefined, filename slug).

## Search eval (`run_search_eval.py`)

Tests retrieval in isolation — no LLM calls, runs in ~4 seconds. Lets us
iterate on index configuration (text fields, boosts) and immediately see the
impact on recall and hit rate.

```bash
uv run --project faq_automation python -m faq_automation.evals.run_search_eval
```

### How it works

Each eval case is a real GitHub issue (the question a student asked) paired with
the `doc_id` of the FAQ entry that was eventually created from it. For example,
issue #289 ("Why do I get IndexError: list index out of range?") became FAQ entry
`1a7b27c4df` in `module-2-vector-search`.

The search index is the current `_questions/` directory, which already contains
that entry (we merged it). We search the index with the issue's question and
answer (matching production behavior, where the agent searches with both) and
measure whether the search surfaces the right doc.

This tests the DUPLICATE detection scenario: if a future student asks a similar
question, will the search find the existing entry so the agent can mark it as
DUPLICATE instead of creating a redundant new one? If recall is low, genuine
duplicates slip through as NEW.

### The self-match problem

Many eval cases use the same (or very similar) question text as the FAQ entry
they became. This makes the search trivially easy — keyword search finds a doc
with the same keywords. To make the eval meaningful, some cases were reworded to
sound like how a student would phrase the question in Slack (marked `"reworded"`
in the note field), rather than copying the FAQ question verbatim.

### Metrics

- recall@k: did the search surface the relevant doc in the top-k? This
  directly controls DUPLICATE detection. Low recall means genuine duplicates
  slip through as NEW.
  Baseline: recall@5 = 0.830

- MRR@k: mean reciprocal rank of the relevant doc. Higher is better — the
  relevant doc should appear early so the LLM sees it in context.
  Baseline: MRR@5 = 0.777

- hit_rate@k: fraction of cases where the relevant doc is anywhere in the
  top-k. With a single relevant doc per case, hit_rate@k = recall@k.
  Baseline: hit_rate@5 = 0.830

## RAG eval (`runner.py`)

Tests the full pipeline end-to-end: search + LLM decision + content generation.
Each case is a real issue proposal processed through the agent, then checked
against expected outcomes.

```bash
uv run --project faq_automation python -m faq_automation.evals.runner
```

Run only the case or cases originating from one GitHub issue:

```bash
uv run --project faq_automation python -m faq_automation.evals.runner --issue 303
```

### How it works

Each case is a real issue with known ground truth (the action, section, and
content quality expected). The runner:

1. For NEW cases: hides the target doc from a temporary copy of the course
   directory, so the agent can't trivially find it as a duplicate. This
   simulates the state the agent was in when the proposal was first processed.
2. For DUPLICATE cases: runs against the full index (doc is present).
3. Runs the agent end-to-end and checks the decision against expected outcomes.

### What it checks

- Action correctness: NEW, UPDATE, or DUPLICATE — does the agent make the
  right call?
- Section placement: does the entry land in the right section?
- Content quality: is the code runnable (all variables defined)? Are there
  structural headers? Is the answer concise? Is the filename slug present?
- Sort order: the collision-safe `_shift_section_files` logic should prevent
  any sort_order collision.

### The historical-data problem

Entries we merged already exist in the FAQ. For DUPLICATE cases this is correct
— the agent should find and cite the existing entry. For NEW cases, we hide the
target doc so the agent sees the "before" state.

### Tags

Each case is tagged for failure analysis:

| Tag | Cases | What it tests |
|-----|-------|---------------|
| correct-new | 13 | Valid NEW proposals — agent should create them |
| section-misplacement | 7 | Bot historically placed in wrong section |
| duplicate-verify | 5 | Doc in index — agent should find it as DUPLICATE |
| false-duplicate | 4 | Genuine NEW that agent wrongly calls DUPLICATE |
| dlt | 4 | dlt-specific placement (workshop vs module-3) |
| content-formatting | 4 | No structural headers, proper formatting |
| duplicate-detection | 3 | Agent should correctly identify duplicates |
| bruin | 2 | Bruin-specific placement (module-5) |
| code-quality | 2 | Generated code must be runnable |
| section-placement | 2 | Tests correct section selection |
| relevance | 2 | Agent should reject irrelevant proposals |
| update-quality | 1 | UPDATE should not degrade existing content |
| verbosity | 1 | Answer should be concise |
| filename-slug | 1 | Filename slug should not be None |

## Adding cases

### Search cases

Add a `SearchCase` to `search_cases.py`:

```python
SearchCase(
    course="llm-zoomcamp",
    question="...",
    answer="...",
    doc_id="abc1234567",
    issue_number=123,
    note="reworded",
)
```

To find the doc_id for a merged entry: `grep -r '<question text>' _questions/`
or check the file's frontmatter `id`. To fetch the answer from GitHub:
`gh issue view <N> --json body` then parse the `### Answer` section.

### RAG cases

How the eval data was created:

The eval cases come from two sources:

1. GitHub issues: listed all faq-proposal issues with
   `gh issue list --state all --label faq-proposal --limit 200`, then fetched
   each issue body with `gh issue view <N> --json body` to get the question and
   answer. Traced each issue to its PR to find the outcome (NEW/UPDATE/DUPLICATE)
   and the `doc_id` of the created file.

2. Git log corrections: the most valuable test cases come from commits where a
   human had to fix the bot's output after merging. We traced these by finding
   all commits by `github-actions[bot]` and `FAQ Bot` that created `_questions/`
   files, then searching for subsequent commits touching the same file:

   ```bash
   # Find bot commits
   git log --all --format="%H|%an|%s" | grep "github-actions\|FAQ Bot"
   # Find corrections to a bot-created file
   git log --oneline --all <bot_commit>..HEAD -- <file>
   ```

   These correction commits reveal the patterns the bot gets wrong: section
   misplacements (e.g. "Move dlt schema evolution FAQ from module-3 to
   workshop-1-dlthub"), sort order collisions ("Renumber to avoid collision"),
   content fixes ("strip headers"), etc. Each correction became a test case with
   the expected outcome set to what the bot should have done.

For each case, the expected_action and expected_section were determined from the
issue content and the course's `_metadata.yaml` section comments. NEW cases got a
`relevant_doc_id` so the runner can hide the entry. Cases were tagged based on the
failure pattern they represent.

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
