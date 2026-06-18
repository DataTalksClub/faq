# Slack FAQ Fetch — Run Log

Operational log of Slack fetch runs for FAQ curation. Each run pulls a course's Slack
channel (the `slack_channel` in `_questions/<course>/_metadata.yaml`) over a lookback
window and writes a review export to `.tmp/`. Driven by the `/slack-faq-fetch` skill.

## How the window is chosen

The fetcher takes a **relative** window (`--days N`, lookback from now). To pick up
exactly where the last run left off:

1. Find the course's **last run date** — the most recent row for that course in the
   **Run history** table below.
2. `days = today − last_run`, rounded up, **plus ~1 day** of overlap (overlap is
   harmless; a gap silently drops messages).
3. If the course has no row yet, fall back to git:
   `git log -1 --date=short --pretty=%ad -- _questions/<course>/`

Exports live in `.tmp/` (gitignored) — only this log is committed.

## Run history

Most recent at the top. `date` is UTC run date.

| date (UTC)  | course                    | days | limit | messages | export                                                                                  | note                                                              |
| ----------- | ------------------------- | ---- | ----- | -------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| 2026-06-18  | llm-zoomcamp              | 3    | 500   | 89       | `.tmp/slack-llm-zoomcamp-course-llm-zoomcamp-20260618T152321Z.md`                       | Covered 06-15→06-18 (overlaps last fetch at 06-16).               |
| 2026-06-18  | data-engineering-zoomcamp | 40   | 1000  | 164      | `.tmp/slack-data-engineering-zoomcamp-course-data-engineering-20260618T152346Z.md`      | First tool-based fetch. Covered 05-10→06-17. Recurring certificate/self-paced questions flagged. |

## Findings / follow-ups

- **Data Engineering — certificate for self-paced learners (recurring):** 5+ messages
  from self-paced learners who submitted the project before the deadline but see
  "Certificate Not available" / leaderboard score still zero after peer review. Likely a
  gap vs. the existing `general/025_how-do-i-get-my-certificate` and
  `general/015_certificate-can-i-follow-the-course-in-a-self-pace` entries — worth a
  dedicated "certificate not available after self-paced submission" FAQ.
- **Data Engineering — dbt `analyses` subfolder (single report):** a learner couldn't find
  the `analyses`/deduplication for `fct_trips` committed to the repo. Not matched by
  existing `module-4` entries (closest: `035` inconsistent rows on re-run).
- **Data Engineering — prerequisites:** one detailed "is my SQL/Python enough, and where
  to learn Git/Linux before starting" question. Check whether an existing prerequisites
  FAQ covers it before adding.

## Pre-log baseline (inferred from git + `.tmp/`, before this log existed)

- **llm-zoomcamp** — last fetch **2026-06-16**. Export
  `.tmp/slack-llm-zoomcamp-course-llm-zoomcamp-20260616T081545Z.md` (412 messages,
  covering 06-02→06-16). Corresponding commit `42034b4` "Add Slack FAQ fetch workflow…".
- **data-engineering-zoomcamp** — **never fetched with the tool** prior to 2026-06-18.
  Last FAQ *content* commit `2026-05-12`; older manual dump
  `.tmp/de-zoomcamp-slack-faqs.md` dated 2026-05-03.
