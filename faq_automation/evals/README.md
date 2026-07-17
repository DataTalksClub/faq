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
| RAG eval (`runner.py`) | Full pipeline (search + LLM decision + content generation) | 51 | ~2 min | action correctness, section placement, code quality, formatting |

Current results on `gpt-5.4-nano`: 36/51. Remaining failures are mostly action
decisions (false DUPLICATE on genuinely new proposals), content quality (code
variables undefined, filename slug), and WRONG_COURSE recall — see below for why
that last one is deliberately allowed to fail.

The suite total is a weak signal: three candidate models scored within one case
of each other, and a single run is noisy enough that the gap means nothing. The
model was picked on failure cost instead — see [docs/model-choice.md](../../docs/model-choice.md).

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

### Flex and Batch

Evals are the ideal shape for OpenAI's discounted tiers: many independent
requests, and nobody waiting on any single one. Both tiers below bill at the same
rate, roughly half of standard, so the choice is purely about latency.

Cases run on the **flex tier** by default (`flex.py`). Flex answers in real time
but individual requests are slower and can be refused with a 429 when capacity is
tight, so requests retry with backoff and run 8 at a time to win the wall-clock
back. The last attempt falls back to the standard tier rather than lose the case:
one case at full price beats a hole in the results.

`--batch` submits the whole suite as a single Batch API job instead (`batch.py`).
Same price, but the job is queued and OpenAI promises only "within 24h" — a run
during this feature's development sat at 0/51 completed for over two hours. Use
it when nothing is waiting on the result; use flex when you are iterating.

Either way, retrieval and prompt assembly happen locally, so the requests are
byte-for-byte what `process_proposal` would have sent.

Submitting a batch is the part you pay for, so if a run dies while polling, score
the finished job instead of resubmitting:

```bash
uv run --project faq_automation python -m faq_automation.evals.runner --batch-id batch_abc123
```

The batch id is printed right after submission. In both modes, a case whose
request failed is scored as a failure rather than skipped, so a partial run can
never look like a clean one.

### How it works

Each case is a real issue with known ground truth (the action, section, and
content quality expected). The runner:

1. For NEW cases: hides the target doc from a temporary copy of the course
   directory, so the agent can't trivially find it as a duplicate. This
   simulates the state the agent was in when the proposal was first processed.
2. For DUPLICATE cases: runs against the full index (doc is present).
3. Runs the agent end-to-end and checks the decision against expected outcomes.

### What it checks

- Action correctness: NEW, UPDATE, DUPLICATE, or WRONG_COURSE — does the agent
  make the right call?
- Section placement: does the entry land in the right section?
- Content quality: is the code runnable (all variables defined)? Are there
  structural headers? Is the answer concise? Is the filename slug present?
- Sort order: the collision-safe `_shift_section_files` logic should prevent
  any sort_order collision.

### The historical-data problem

Entries we merged already exist in the FAQ. For DUPLICATE cases this is correct
— the agent should find and cite the existing entry. For NEW cases, we hide the
target doc so the agent sees the "before" state.

### WRONG_COURSE and its false-positive budget

Students pick the course from a dropdown when filing a proposal, and sometimes
pick the wrong one — issues #97, #109, #148, #287, and #311 are all questions
about one course filed against another. The agent only ever sees the selected
course's entries and sections, so a misfiled proposal gets forced into whichever
section fits least badly. WRONG_COURSE closes the issue instead.

The two failure modes are not equal, and only one of them is expensive.

A missed WRONG_COURSE costs a maintainer one PR close — the same review that
already happens for every proposal, and the reviewer is looking at the course
anyway. A false WRONG_COURSE closes a student's valid contribution and tells
them, wrongly, that they filed against the wrong course. Nobody reviews a closed
issue, so the mistake is invisible until the student complains or walks away.

So the two rates get treated differently: false positives are a release gate,
recall is a nice-to-have. The eval is deliberately lopsided about this:

- The `wrong-course` tag holds the positive cases (5 real, 2 synthetic).
- The `wrong-course-guard` tag holds deliberate near misses that must come back
  NEW: a shared tool used by the course that was selected (Docker in ML zoomcamp,
  Kestra in LLM zoomcamp), course-agnostic tooling (uv), and a topic the FAQ
  doesn't cover yet. Absence of coverage must never read as the wrong course.
- Every case outside the `wrong-course` tag is an implicit guard too — the runner
  injects a `not_wrong_course` check into each one, so any case that unexpectedly
  comes back WRONG_COURSE fails. That makes the whole suite the false-positive
  budget, not just the cases written for it.

Where it stands on `gpt-5.4-nano`, the production model:

| | Result |
|---|---|
| False positives | 0 of 44 non-wrong-course cases (single suite run) |
| Recall | 1 of 7 wrong-course cases (single suite run) |

Every model measured holds the false-positive count at zero; they differ only in
recall and in what they do on the other 44 cases. `gpt-5.4-nano` sits at the low
end of recall on purpose — [docs/model-choice.md](../../docs/model-choice.md) has
the comparison and the reasoning.

That recall is low on purpose and is fine to ship. The rules demand positive
evidence of another course and tell the model to prefer NEW/UPDATE/DUPLICATE when
unsure, so a borderline call lands on "file it" rather than "close it". The misses
become PRs that a human closes, which is exactly what happened before this action
existed — the bot is no worse than the status quo on them. The zero is the number
that has to hold.

Do not chase recall by softening the "when unsure, prefer NEW" hedge or by
dropping the demand for positive evidence. Those are what buy the zero. If recall
ever needs to be better, a stronger model for this decision is the safer lever
than a more aggressive prompt.

#### The decision is not stable

A single run understates how much this moves. Re-running the wrong-course and
guard cases 5x each against an identical prompt on `gpt-5-nano` — the model this
project used before `gpt-5.4-nano`, kept here because it is the clearest
illustration of the instability, which has not gone away:

| Case | Fires | |
|---|---|---|
| #148 BigQuery query costs | 4/5 | flips |
| MLflow model registry (synthetic) | 4/5 | flips |
| #97 Spark global temp views | 3/5 | flips |
| #311 RAGWithMetrics | 1/5 | flips |
| Terraform GCS bucket (synthetic) | 1/5 | flips |
| #287 FAQ dataset doc counts | 0/5 | never fires |
| #109 pgAdmin in Codespaces | 0/5 | never fires |
| **Recall** | **13/35** | |
| **False positives** | **0/20** | |

Five of seven wrong-course cases flip between NEW and WRONG_COURSE on identical
input, so any single case's result is a coin toss, not a fact. The guards flip
too — the `uv` case returned DUPLICATE twice, NEW twice, and UPDATE once — but
never into WRONG_COURSE. Across the suite run and this probe the false-positive
count is 0/64 observations, which is the evidence the release gate rests on. It
is still a bounded sample, not a proof: re-run after any prompt change rather
than trusting a previous green, and treat a single passing run of a wrong-course
case as noise.

What predicts recall is whether the entry names a tool owned by exactly one
course. BigQuery, MLflow, and Spark fire reliably. #311 is mostly generic OpenAI
API mechanics (`chat.completions` vs `responses`) with RAG incidental to it, and
#287 names no tool at all — both read as "unfamiliar", which the rules correctly
send to NEW. #109 never fires because the rules explicitly forbid firing on
Docker and Codespaces, which is most of that entry; the pgAdmin signal that would
identify it never gets weighed. That is the "prefer NEW when unsure" hedge doing
its job, and the cost of the zero.

Reproduce with the probe used to produce this table, on any model:

```bash
uv run --project faq_automation python -m faq_automation.evals.probe_wrong_course gpt-5.4-nano 5
```

Model choice moves these numbers more than prompt tuning has: `gpt-5.6-luna`
reaches 27/35 recall with 5 of 7 cases fully deterministic, still at 0/20 false
positives, but was not adopted for reasons that have nothing to do with this
table. See [docs/model-choice.md](../../docs/model-choice.md).

Catch-all sections are a trap worth knowing about: ML Zoomcamp has a `misc`
section and every course has `general`. A catch-all can plausibly hold anything,
which silently satisfies "no section fits" and lets a misfiled proposal land there
instead of being caught — the first version of this prompt dropped the #311 RAG
question into `misc` for exactly that reason. The rules now tell the model to
decide as if those sections did not exist.

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
| wrong-course | 7 | Student picked the wrong course — agent should close the issue |
| wrong-course-guard | 4 | Near misses that must NOT be rejected as wrong course |
| synthetic | 6 | Written by hand rather than taken from a real issue |
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

Available check predicates: `action_is`, `section_is`, `suggested_course_is`,
`no_structural_headers`, `content_is_runnable_python`, `content_is_concise`,
`has_filename_slug`, `has_trailing_newline`, `content_has_no_bold_headers`,
`no_sort_order_collision`, `not_wrong_course` (injected automatically).

Use the real issue number whenever a case comes from one, so `--issue N` reaches
it; several cases may share a number when one issue tests more than one thing.
Hand-written cases use `issue_number=0` and the `synthetic` tag.
