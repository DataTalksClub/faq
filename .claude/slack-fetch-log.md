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
| 2026-07-30  | llm-zoomcamp              | 16   | 1000  | 383      | `.tmp/slack-llm-zoomcamp-course-llm-zoomcamp-20260730T154645Z.md`                       | Three granular project-dataset FAQ candidates found.              |
| 2026-07-15  | llm-zoomcamp              | 7    | 1000  | 168      | `.tmp/slack-llm-zoomcamp-course-llm-zoomcamp-20260715T095558Z.md`                       | One clarification: homework is optional; the capstone and required peer reviews determine certificate eligibility. |
| 2026-07-15  | data-engineering-zoomcamp | 7    | 1000  | 17       | `.tmp/slack-data-engineering-zoomcamp-course-data-engineering-20260715T095544Z.md`      | No new reusable FAQ gap found.                                    |
| 2026-07-15  | machine-learning-zoomcamp | 7    | 1000  | 5        | `.tmp/slack-machine-learning-zoomcamp-course-ml-zoomcamp-20260715T095541Z.md`           | July 9 certificate clarification was already inside the previous fetch window. |
| 2026-07-15  | mlops-zoomcamp            | 7    | 1000  | 0        | `.tmp/slack-mlops-zoomcamp-course-mlops-zoomcamp-20260715T095541Z.md`                   | No channel activity in the window.                                |
| 2026-07-15  | ai-dev-tools-zoomcamp     | 7    | 1000  | 1        | `.tmp/slack-ai-dev-tools-zoomcamp-C09HWT76L95-20260715T100219Z.md`                      | Fetched by channel ID; only an automated Telegram link, no question. |
| 2026-07-15  | stock-markets-analytics-zoomcamp | 7 | 1000 | 0      | `.tmp/slack-stock-markets-analytics-zoomcamp-C06L1RTF10F-20260715T100219Z.md`           | Fetched by channel ID; no channel activity in the window.         |
| 2026-07-09  | machine-learning-zoomcamp | 24   | 1000  | 22       | `.tmp/slack-machine-learning-zoomcamp-course-ml-zoomcamp-20260709T150147Z.md`           | First tool-based fetch. Covered 06-15→07-09 (baseline from git 06-16). |
| 2026-07-09  | llm-zoomcamp              | 10   | 1000  | 213      | `.tmp/slack-llm-zoomcamp-course-llm-zoomcamp-20260709T145556Z.md`                       | Covered 06-29→07-09 (overlaps last fetch at 06-30).               |
| 2026-07-09  | data-engineering-zoomcamp | 22   | 1000  | 62       | `.tmp/slack-data-engineering-zoomcamp-course-data-engineering-20260709T145543Z.md`      | Covered 06-17→07-09 (overlaps last fetch at 06-18).               |
| 2026-06-30  | llm-zoomcamp              | 13   | 1000  | 476      | `.tmp/slack-llm-zoomcamp-course-llm-zoomcamp-20260630T093805Z.md`                       | Covered 06-17→06-30 (overlaps last fetch at 06-18).               |
| 2026-06-18  | llm-zoomcamp              | 3    | 500   | 89       | `.tmp/slack-llm-zoomcamp-course-llm-zoomcamp-20260618T152321Z.md`                       | Covered 06-15→06-18 (overlaps last fetch at 06-16).               |
| 2026-06-18  | data-engineering-zoomcamp | 40   | 1000  | 164      | `.tmp/slack-data-engineering-zoomcamp-course-data-engineering-20260618T152346Z.md`      | First tool-based fetch. Covered 05-10→06-17. Recurring certificate/self-paced questions flagged. |

## Findings / follow-ups

- **LLM Zoomcamp — minimum project dataset size (2026-07-17):** the rubric sets no
  minimum size. This is a granular FAQ candidate.
- **LLM Zoomcamp — static or self-created project data (2026-07-16→07-17):** a
  project dataset does not need to come from a live API; a static file or self-created
  dataset is allowed when the ingestion is reproducible. This is a separate granular
  FAQ candidate.
- **LLM Zoomcamp — non-English project data (2026-07-24):** non-English data and
  responses are allowed when the README and documentation are in English. This is a
  separate granular FAQ candidate.
- **LLM Zoomcamp — already covered or resolved (2026-07-30 review):** repeated project
  attempt and peer-review questions match existing project FAQs; differing module-4
  retrieval metrics match the FAQ explaining that the live dataset changes over time;
  and the module-5 feedback-button bug was fixed in the course repository.
- **LLM Zoomcamp — certificate requirement (clarified, 2026-07-14):** students do
  not need to complete homework, but they must finish a capstone project and its
  required peer reviews to receive a certificate. Clarified the self-paced
  certificate FAQ.
- **Channel metadata (2026-07-15):** the Slack token could not resolve the names
  `course-ai-dev-tools` or `course-stock-markets-analytics`, so those exports were
  fetched successfully with their configured channel IDs instead. Updated both
  course metadata files to their current `*-zoomcamp` channel names.
- **Data Engineering — certificate for self-paced learners (recurring):** 5+ messages
  from self-paced learners who submitted the project before the deadline but see
  "Certificate Not available" / leaderboard score still zero after peer review. Likely a
  gap vs. the existing `general/025_how-do-i-get-my-certificate` and
  `general/015_certificate-can-i-follow-the-course-in-a-self-pace` entries — worth a
  dedicated "certificate not available after self-paced submission" FAQ.
- **Data Engineering — dbt `analyses` subfolder (single report):** a learner couldn't find
  the `analyses`/deduplication for `fct_trips` committed to the repo. Not matched by
  existing `module-4` entries (closest: `035` inconsistent rows on re-run).
- **Data Engineering — self-paced eligibility (recurring, 2026-07-09):** four+ messages
  asking whether the course can still be done self-paced after the 2026 cohort closed,
  whether materials stay relevant, and whether a project done now counts toward a future
  cohort. Already partly covered by `general/015_certificate-can-i-follow-the-course-in-a-self-pace`,
  `general/006_course-how-many-zoomcamps-in-a-year`, `general/009_course-can-i-get-support-…`;
  no new FAQ needed unless a "can a self-paced project count for a future cohort?" entry
  is wanted (that specific angle isn't covered).
- **Data Engineering — module-4 playlist confusion (single report, 2026-06-26):** learner
  unsure whether to follow Juan's 8-video dbt set or Victoria's 69-video playlist.
  Closest existing entry is `general/010_…-which-playlist-on-youtube-…`; low priority.
- **LLM Zoomcamp — HW4 hybrid_search `k` values (single report, 2026-07-01):** question
  about what "evaluate hybrid_search for k = 1,50,100,200" means given per-doc RRF.
  Homework-specific; better suited to the module-4 homework thread than an FAQ unless it
  recurs. ONNX/MRR divergence (07-08) is also single-report.
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
