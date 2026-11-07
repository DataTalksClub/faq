# Model Choice

We use `gpt-5.4-nano` as the FAQ automation's `DEFAULT_MODEL` in
`faq_automation/rag_agent.py`. Set `FAQ_MODEL` to try another model for one run.

## Current evidence

The model scored 45/74 in the latest full run on the current suite with
`gpt-5.4-nano` ([workflow run](https://github.com/DataTalksClub/faq/actions/runs/42366074324)).
It made no false `WRONG_COURSE` decisions across 67 valid proposals and correctly
identified 2 of 7 misfiled proposals. It returns NEW for #548 in
`module-6-homework`, but still chooses NEW instead of UPDATE for #509.

The 11 cases added for recent FAQ Bot corrections all failed at least one
action, placement, or answer-content check. Eight chose the wrong action. The
other three chose the expected action and section but omitted required details.
This baseline doesn't pass the full RAG evaluation. Unit and integration CI pass
separately.

We haven't compared models on the current suite. Review the failure checks and
action costs before changing the default.

## Action costs differ

The bot responds to each model action this way:

- When the bot returns `NEW`, it opens a PR that adds an entry for a maintainer to review.
- When the bot returns `UPDATE`, it opens a PR that changes an existing entry. A reviewer checks the diff for mistakes.
- When the bot returns `DUPLICATE`, it comments on the issue and closes it without review.
- When the bot returns `WRONG_COURSE`, it comments on the issue and closes it without review.

When the model misses a WRONG_COURSE label, the bot opens a PR that a maintainer
can review. If the model wrongly returns WRONG_COURSE, the bot closes a valid
proposal without review. We require evidence before the model chooses
WRONG_COURSE and tell it to prefer `NEW`, `UPDATE`, or `DUPLICATE` when unsure.

When the bot wrongly returns `NEW`, it adds an entry a reviewer can spot. When
it wrongly returns `UPDATE`, it can replace accurate guidance with plausible but
incorrect content. We choose `UPDATE` only when an existing FAQ covers the same
problem. A reviewer then compares the diff with course material.

## Re-evaluating the default

Don't compare models using full-suite results from different case sets. Before
changing `DEFAULT_MODEL`, run the full current RAG suite for each candidate and
compare the false-positive checks, action decisions, and section placement. Record
the run links and results for the current cases in the eval guide.

Run the current default with:

```bash
uv run --project faq_automation python -m faq_automation.evals.runner
```

Run another model with:

```bash
uv run --project faq_automation python -m faq_automation.evals.runner --model gpt-5-nano
```
