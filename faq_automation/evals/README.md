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
| Search eval (`run_search_eval.py`) | Retrieval challenge set (minsearch index) in isolation — no LLM calls | 25 | ~2s | recall@k, MRR@k, hit_rate@k |
| RAG eval (`runner.py`) | Full pipeline (search + LLM decision + content generation) | 61 | ~2 min | action correctness, section placement, code quality, formatting |

The most recent recorded results, before cases #329, #336, and #342 were added,
are 37/58 on `gpt-5.4-nano`. All three
historical placement cases added for issues #319, #330, and #332 selected the
correct section; #332 varied between NEW and UPDATE across runs. Remaining
failures are mostly action
decisions (false DUPLICATE on genuinely new proposals), content quality (code
variables undefined, filename slug), and WRONG_COURSE recall — see below for why
that last one is deliberately allowed to fail.

The suite total is a weak signal: three candidate models scored within one case
of each other, and a single run is noisy enough that the gap means nothing. The
model was picked on failure cost instead — see [docs/model-choice.md](../../docs/model-choice.md).

## Search eval (`run_search_eval.py`)

We test retrieval without making LLM calls, so the suite runs in about two
seconds. We can change the index and immediately see how it affects recall and
ranking. On the current corpus, recall@5 is 0.840 and MRR@5 is 0.813 across 25
challenge cases.

```bash
uv run --project faq_automation python -m faq_automation.evals.run_search_eval
```

### Retrieval flow

Each eval case is a deliberately difficult query paired with the `doc_id` of the
FAQ entry it should retrieve. Ten cases come from real GitHub issues, and the
other 15 are synthetic variations. Each case names the retrieval failure it
tests.

We build the search index from the current `_questions/` directory, which already
contains the target entry. Production searches the question separately from the
full question-and-answer proposal, then combines both rankings with reciprocal
rank fusion. This keeps a vague proposed answer from burying a strong question
match. The eval uses the same retrieval path and measures whether it surfaces
the right document.

This matters for duplicate detection. When a future student asks a similar
question, search must put the existing entry in front of the model. Otherwise,
the model will probably create a redundant entry.

### Exact self-matches

An original proposal usually has the same wording as the FAQ created from it.
When we search with that wording, keyword matching makes the result trivial and
inflates the aggregate score. It doesn't test whether search can recognize a
future duplicate. We therefore include only cases with a named retrieval
challenge. The original proposals remain in `search_cases.py` as source history
but aren't included in `ALL_CASES`.

### Challenge cases

We want the query to resemble the next student's question, not the proposal that
created the FAQ. A student may remember the symptom but leave out the tool, use
different words, or mention terms that appear in several modules. We still need
search to put the right FAQ in front of the model.

The challenge set includes:

- Vague questions such as "the download just hangs". They contain few words
  that distinguish the target from other troubleshooting entries.
- Reworded and paraphrased questions. They describe the same problem without
  copying the FAQ title.
- Bare error messages. An error can be distinctive, but without the command or
  module around it, several entries may look plausible.
- Cross-module questions. Terms such as Docker, Kestra, DuckDB, and dbt appear
  throughout a course, so keyword overlap can point search to the wrong section.
- Homework questions with little context. "My counts don't match" says what the
  student sees, but not which exercise or operation produced the counts.
- Competing-document cases. More than one FAQ is a reasonable match, and the
  specific one the model needs must rank near the top.
- Regressions from earlier runs. Some now rank first because we fixed them, but
  we keep them to catch the same mistake if it returns.

Four queries currently miss the top five. For example, "It crashes when I try to
search" doesn't mention the embedding-count mismatch in its target FAQ. "Kestra
Docker volume not working" mixes two common topics. The query "homework 6 Spark
record counts don't match" leaves several Spark and homework entries in
contention. We learn more about the limits of keyword search from these misses
than from an exact proposal-to-FAQ match.

### Metrics

- recall@k: did the search surface the relevant doc in the top-k? This
  directly controls DUPLICATE detection. Low recall means genuine duplicates
  slip through as NEW.
  Baseline: recall@5 = 0.840

- MRR@k: mean reciprocal rank of the relevant doc. Higher is better — the
  relevant doc should appear early so the LLM sees it in context.
  Baseline: MRR@5 = 0.813

- hit_rate@k: fraction of cases where the relevant doc is anywhere in the
  top-k. With a single relevant doc per case, hit_rate@k = recall@k.
  Baseline: hit_rate@5 = 0.840

## RAG eval (`runner.py`)

Tests the full pipeline end-to-end: search + LLM decision + content generation.
Each case is a real issue proposal processed through the agent, then checked
against expected outcomes.

```bash
uv run --project faq_automation python -m faq_automation.evals.runner
```

Run only the case or cases with a given `case_id` (see [Case ids](#case-ids)):

```bash
uv run --project faq_automation python -m faq_automation.evals.runner --case 303
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
decide as if those sections did not exist. See
[the catch-all section](#catch-all-sections) for what that trap turned out not to be.

### Tags

Each case is tagged for failure analysis:

| Tag | Cases | What it tests |
|-----|-------|---------------|
| correct-new | 14 | Valid NEW proposals — agent should create them |
| section-misplacement | 12 | Bot historically placed in wrong section |
| duplicate-verify | 6 | Doc in index — agent should find it as DUPLICATE |
| false-duplicate | 4 | Genuine NEW that agent wrongly calls DUPLICATE |
| dlt | 6 | dlt-specific placement (workshop vs module-3) |
| content-formatting | 4 | No structural headers, proper formatting |
| duplicate-detection | 3 | Agent should correctly identify duplicates |
| bruin | 2 | Bruin-specific placement (module-5) |
| code-quality | 2 | Generated code must be runnable |
| section-placement | 7 | Tests correct section selection |
| relevance | 2 | Agent should reject irrelevant proposals |
| wrong-course | 7 | Student picked the wrong course — agent should close the issue |
| wrong-course-guard | 4 | Near misses that must NOT be rejected as wrong course |
| catch-all | 3 | `misc`/`general` must not swallow placeable entries, but must still take genuinely cross-cutting ones |
| synthetic | 6 | Written by hand rather than taken from a real issue (negative `case_id`) |
| update-quality | 2 | UPDATE should not degrade existing content or target a lexical match from the wrong section |
| retrieval-bias | 2 | Lexical similarity must not outweigh course and section context |
| homework-placement | 4 | Homework-only material must not land in a lesson or another module |
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
    case_id=123,
    note="reworded",
)
```

The `note` must name the retrieval challenge. Cases without a note are retained
only as historical source data and are not run. Do not add an unchanged proposal
solely because it has a known target document; reword it into a realistic future
duplicate or capture a specific retrieval regression.

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
`relevant_doc_id` so the runner can hide the entry. A case can also list
`hidden_doc_ids` to hide later related entries and recreate the corpus that
existed when the historical placement error occurred. Cases were tagged based
on the failure pattern they represent.

Add an `EvalCase` to `cases.py`:

```python
EvalCase(
    course="llm-zoomcamp",
    case_id=123,
    question="...",
    answer="...",
    expected_action="NEW",
    expected_section="module-3",
    checks=[action_is("NEW"), section_is("module-3")],
    tags=["section-placement"],
    relevant_doc_id="abc1234567",  # hidden from index for NEW cases
    hidden_doc_ids=["laterdoc01"],  # optional historical-corpus isolation
)
```

Available check predicates: `action_is`, `section_is`, `suggested_course_is`,
`no_structural_headers`, `content_is_runnable_python`, `content_is_concise`,
`has_filename_slug`, `has_trailing_newline`, `content_has_no_bold_headers`,
`no_sort_order_collision`, `not_wrong_course` (injected automatically).

### Catch-all sections

ML Zoomcamp has a `misc` section ("Miscellaneous") and every course has
`general`. Both can plausibly hold anything, which makes them worth a specific
set of cases — tagged `catch-all`.

The obvious worry is that a catch-all becomes a dumping ground the agent drifts
into. That worry turned out to be **wrong**, and it is worth recording why so
nobody re-derives it. With `misc` carrying no `comment` at all, the agent still
placed course logistics in `general` (5/5) and a Waitress/Docker serving error in
`module-5` (5/5). It was not reaching for `misc` when something else fit. What it
could not do was use `misc` when `misc` was correct: a "Python 3.13 breaks sklearn"
question — cross-cutting, owned by no module — went to `module-5` 5 times out of
5. Adding a comment that scopes `misc` and states plainly that it is not a
fallback took those three cases from 10/15 to 15/15.

Two things follow:

- **The 40 entries in ML Zoomcamp's `misc` are not evidence of agent drift.** All
  40 were added by a human in bulk imports; the bot has never filed anything
  there. Their placement is a content-curation question, not a bug.
- **The real catch-all failure is the reverse of the intuitive one.** A section
  with no `comment` is invisible to the agent as a *destination*, because the
  prompt weights `comment` above retrieval. An undescribed section does not
  attract entries — it repels them.

The separate trap is `WRONG_COURSE`: a catch-all silently satisfies "no section
fits", so a misfiled proposal lands there instead of being caught. That one is
real — the first version of the prompt dropped the #311 RAG question into `misc` —
and it is handled by telling the model to decide the course question as if
catch-all sections did not exist. Section placement and the course check ask
different questions of the same section list.

### Case ids

`case_id` says where a case came from, and its sign says what kind it is:

- **Positive** — the GitHub issue number the proposal was taken from. Several
  cases may share one number when a single issue tests more than one thing (issue
  #287 is both a wrong-course case and a transient-content case).
- **Negative** — synthetic, written by hand, each with its own id. Also tagged
  `synthetic`.

Both suites use the same convention. Run one case with `--case`, which takes
either sign — use `=` for negatives so it isn't parsed as a flag:

```bash
uv run --project faq_automation python -m faq_automation.evals.runner --case 303
uv run --project faq_automation python -m faq_automation.evals.runner --case=-3
```
