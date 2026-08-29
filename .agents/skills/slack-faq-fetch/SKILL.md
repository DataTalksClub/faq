---
name: slack-faq-fetch
description: Pull recent Slack channel discussions for a course (e.g. LLM Zoomcamp, Data Engineering Zoomcamp) into a review export to find missing FAQ entries. Determines the lookback window from the last-fetch date or git history, runs the fetcher, updates the date, and points to the export for review. Use when the user wants to fetch Slack questions, refresh FAQ content from Slack, or check what's missing for a course.
---

# Slack FAQ Fetch

Fetch recent Slack discussions for a course so missing FAQ entries can be curated. The fetcher is an existing Python CLI (`faq_automation/slack_fetch.py`); this skill drives it end to end.

## How it works

`faq_automation.slack_fetch` calls the Slack Web API using the `SLACK_BOT_TOKEN` from `.env` (loaded automatically — **never print the token**), reads the course's `slack_channel` from `_questions/<course>/_metadata.yaml`, pulls the last `N` days of messages **plus thread replies**, and writes paired JSON + Markdown exports to `.tmp/`. The Markdown export is what you review.

The tool only takes a **relative** window (`--days N`, lookback from *now*), so each run's date must be recorded in the log so the next run can pick up exactly where the last one left off.

## Steps

### 1. Pick the course(s) and the lookback window

- Course = a directory under `_questions/` (e.g. `llm-zoomcamp`, `data-engineering-zoomcamp`). Default: `llm-zoomcamp`.
- Find the course's **last fetch date** in `.claude/slack-fetch-log.md`.
  - If the course has no row yet, fall back to git: `git log -1 --date=short --pretty=%ad -- _questions/<course>/`.
- Compute `days = today − last_run`, rounded up, **plus ~1 day** so windows overlap (overlap is harmless; a gap silently drops messages).
- Get today's date with `date -u +%F`.

### 2. Run the fetch

Run from the **repo root** (so `.env` and `_questions/` resolve):

```bash
uv run --project faq_automation python -m faq_automation.slack_fetch \
  --course <course> --days <N> [--limit <N>]
```

Flags worth knowing:
- `--days` (default 7): lookback from now.
- `--limit` (default 500): max messages. Raise to `1000` for wide windows or busy channels (if the run returns exactly the limit, it was truncated — widen the limit or narrow the window).
- `--channel <name-or-id>`: override the metadata's `slack_channel` for one run.
- `--no-threads`: skip thread replies (much faster, but loses most Q&A).
- `--include-private`: allow private-channel lookup (needs `groups:read`).
- Other defaults are fine: threads included, output to `.tmp/`.

Note the printed message count and the `.tmp/slack-<course>-...-<stamp>.md` path.

### 3. Record the fetch date

Update the course's row in `.claude/slack-fetch-log.md`:

`| <course> | <last fetch date UTC> |`

Keep one row per course and use today's UTC date. Do not record message counts,
export paths, findings, or historical runs. Committing the date keeps the next
fetch window accurate.

### 4. Review the export and find missing FAQs

Open the `.tmp/*.md` export. Most real Q&A lives in thread replies. To find candidate questions:

```bash
# root messages that look like questions
awk '/^## /{if(body ~ /\?/ && header !~ /thread=/) print header"\n"body"\n---"; header=$0; body=""; next} /^$/{next} {body=body$0" "} END{if(body ~ /\?/ && header !~ /thread=/) print header"\n"body"\n---"}' .tmp/<export>.md
```

For each candidate, check it isn't already covered:

```bash
grep -ri "<keyword>" _questions/<course>/
```

- If an existing FAQ fully covers the question, discard the candidate. Do not
  add a finding that says another entry already covers it.

Keep candidates granular:

- Extract one independently answerable question per candidate.
- Split separate dimensions into separate candidates even when they share a topic
  or appear in the same Slack thread. For example, dataset minimum size, allowed
  source type, and allowed language are three questions, not one combined
  "dataset requirements" question.
- Do not create an umbrella FAQ merely because several questions have related
  answers.
- Present and resolve candidates one at a time.

Add any question that is **real, answerable, and not already covered** by an existing FAQ — it does **not** need to recur. A single good question is worth an FAQ if the answer can be reused the next time someone asks. When adding a new FAQ, follow the repo conventions:
- File at `_questions/<course>/<section>/<NNN>_<docid>_<slug>.md` where `NNN` = next `sort_order` (highest in the section + 1) and `<docid>` is a fresh 10-char id.
- Frontmatter: `question`, `id`, `sort_order` (and any existing keys in that section's files). Section id/name/comment come from `_questions/<course>/_metadata.yaml`.

## Notes

- Exports live in `.tmp/` (gitignored) — **only the fetch dates are committed**,
  not the message dumps.
- If the token is missing the run prints `Error: SLACK_BOT_TOKEN is not set`. The bot needs `channels:read` + `channels:history` for public channels, or `groups:read` + `groups:history` (and `--include-private`) for private ones.
- This repo commits straight to `main` (no PRs).
