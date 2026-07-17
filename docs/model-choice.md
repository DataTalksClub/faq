# Model Choice

The FAQ bot runs on **`gpt-5.4-nano`**, set once in `faq_automation/rag_agent.py`
as `DEFAULT_MODEL` and overridable per run with the `FAQ_MODEL` environment
variable. This document records what we measured, why we chose it, and what the
choice gives up — so the next person to touch it can disagree with evidence
rather than start over.

## The decision in one paragraph

Three models score within one case of each other on the eval suite, so the suite
total was useless as a tiebreaker. We picked on failure *cost* instead. The bot
can fail in two ways that are not equally expensive: it can open a bad pull
request, which a maintainer reviews and closes, or it can close a student's valid
proposal with a wrong explanation, which nobody reviews. `gpt-5.4-nano` is the
best model we measured at not rewriting existing published entries, and it never
once wrongly rejected a proposal as filed against the wrong course. It pays for
that by catching only 1 in 5 genuinely misfiled proposals — the cheapest failure
on the list, and no worse than the status quo before that check existed.

## Why failure cost, not accuracy

The four actions split into two paths with very different blast radii:

| Action | Effect | Reviewed by a human? |
|---|---|---|
| `NEW` | Opens a PR adding a file | Yes |
| `UPDATE` | Opens a PR **rewriting an existing entry** | Yes, but the diff is easy to wave through |
| `DUPLICATE` | Comments and closes the issue | **No** |
| `WRONG_COURSE` | Comments and closes the issue | **No** |

Two consequences drive everything below:

1. **`DUPLICATE` and `WRONG_COURSE` are the same harm class.** Both close a
   student's contribution unreviewed. It does not matter which one is wrong; what
   matters is how often a proposal that should have become a PR gets closed
   instead. That is the metric, and it is broader than any single tag in the eval.
2. **`UPDATE` is not free either.** A wrong `NEW` is additive and obvious in
   review. A wrong `UPDATE` silently degrades an entry that was already correct,
   and a reviewer skimming a plausible diff can miss it. Published content is
   harder to un-break than an unmerged PR.

## What we measured

All numbers on the flex tier, prompt held constant, `_questions/` at the time of
writing. Reproduce with the commands at the bottom.

### Wrongly closing a valid proposal

Every eval case whose ground truth is `NEW`, run 3x each (84 observations). Counts
how often the model answered `DUPLICATE` or `WRONG_COURSE` — i.e. closed a
proposal that should have become a PR.

| Model | Wrongly closed |
|---|---|
| `gpt-5-nano` | 15/84 (18%) |
| **`gpt-5.4-nano`** | **12/84 (14%)** |
| `gpt-5.6-luna` | 9/84 (11%) |

### Wrong-course recall and false positives

Wrong-course and guard cases, 5x each. Recall is out of 35, false positives out
of 20. See [the eval README](../faq_automation/evals/README.md) for why these two
numbers are weighted so unequally.

| Model | Recall | False positives | Cases that flip |
|---|---|---|---|
| `gpt-5-nano` | 13/35 (37%) | 0/20 | 5 of 7 |
| **`gpt-5.4-nano`** | **7/35 (20%)** | **0/20** | — |
| `gpt-5.6-luna` | 27/35 (77%) | 0/20 | 1 of 7 |

### Suite and composition

Single run of all 51 cases.

| Model | Suite | correct-new failed | false-duplicate failed | wrong-course |
|---|---|---|---|---|
| `gpt-5-nano` | 36/51 | 4/13 | 2/4 | 3/7 |
| **`gpt-5.4-nano`** | **36/51** | **3/13** | **1/4** | 1/7 |
| `gpt-5.6-luna` | 35/51 | 7/13 | 3/4 | 6/7 |

### Price

Per million tokens. In production this is one call per issue on a ~14k-token
prompt, so the difference is ~$0.005 vs ~$0.03 per issue — a few dollars a year
at current issue volume. Price only bites on eval runs (~$0.27 vs ~$1.30 per
suite).

| Model | Input | Output |
|---|---|---|
| `gpt-5-nano` | ~$0.05 | ~$0.40 |
| **`gpt-5.4-nano`** | **$0.20** | **$1.25** |
| `gpt-5.6-luna` | $1.00 | $6.00 |

## Why `gpt-5.4-nano`

- **It holds the release gate.** 0/20 false positives on the wrong-course guards,
  same as every other model we tried. This was never the differentiator — all
  three pass — but it is the condition any candidate must meet.
- **It is the best at leaving existing entries alone.** 3/13 `correct-new`
  failures against 4/13 and 7/13. Those failures are the ones that turn into
  `UPDATE` PRs rewriting entries that were already fine, the failure a reviewer is
  least likely to catch.
- **It is the best at not closing valid work, among the models whose UPDATE
  behaviour we trust.** 14% against `gpt-5-nano`'s 18%. It strictly dominates the
  model it replaces: fewer wrongful closes *and* fewer bad rewrites, for a price
  difference that rounds to nothing in production.
- **What it costs: wrong-course recall drops to 1 in 5.** Accepted deliberately.
  A missed wrong-course is a PR a maintainer closes — the identical outcome to
  before the check existed, on a review that was going to happen anyway. We are
  trading the cheapest failure for the two most expensive ones.

## The case against, honestly

`gpt-5.6-luna` beat `gpt-5.4-nano` on both headline safety numbers: it wrongly
closed fewer valid proposals (11% vs 14%) and caught 6 of 7 misfiled proposals
against 1 of 7, nearly deterministically where the nanos flip constantly. On a
straight reading of "don't close valid issues, do catch misfiles", luna wins.

We chose `gpt-5.4-nano` anyway because luna buys that recall with a disposition
to conclude "this belongs somewhere else" — right for wrong-course, wrong for
`NEW`. Its `correct-new` failures more than double (7/13 vs 3/13), and they land
as `UPDATE`s. Luna trades a visible, reviewed failure for an invisible one that
corrupts published content, and 3 points of wrongful-close rate did not justify
that. It is a judgement call on which risk is worse, not a fact the data settles.

**Revisit this if:** the `UPDATE` path grows a guard (an eval check that an UPDATE
preserves the original entry's information would make luna's regression
measurable rather than assumed), issue volume rises enough for wrong-course
misses to cost real reviewer time, or a `5.6`-family model appears that does not
over-merge. Luna is the first place to look — the recall gain is real and stable.

## Caveats on this evidence

- **Suite totals are single runs and the decision is not stable.** On
  `gpt-5-nano`, 5 of 7 wrong-course cases flip between `NEW` and `WRONG_COURSE`
  on byte-identical input. A 36-vs-35 gap is inside that noise and was not used to
  decide anything. Only the repeat-probe numbers carry weight.
- **The samples are small.** 84 observations for wrongful closes, 4 cases behind
  the `false-duplicate` column. An earlier version of this decision rested on that
  4-case column alone and reached the opposite conclusion; the 84-observation
  probe overturned it. Treat single-digit differences as noise.
- **Prices are from OpenAI's pricing page at the time of writing** and are not
  checked by anything. Verify before quoting them.
- **The eval's guard cases assert only "not wrong course"**, not a specific
  action, because those questions legitimately overlap existing entries. Do not
  tighten them back to `action == NEW` without re-reading
  [the eval README](../faq_automation/evals/README.md).

## Reproduce

```bash
# Full suite on a given model
uv run --project faq_automation python -m faq_automation.evals.runner --model gpt-5.4-nano

# Wrong-course recall and false positives, 5 repeats
uv run --project faq_automation python -m faq_automation.evals.probe_wrong_course gpt-5.4-nano 5
```

The wrongful-close measurement was a one-off probe over every `expected_action="NEW"`
case, counting `DUPLICATE` and `WRONG_COURSE` answers. It is not committed as a
module; rebuild it from `probe_wrong_course.py` if the number needs refreshing.
