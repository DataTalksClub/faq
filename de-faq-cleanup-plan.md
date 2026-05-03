# DE Zoomcamp FAQ — Cleanup Plan

Working document for the FAQ audit performed against `_questions/data-engineering-zoomcamp/`. Items are checked off as they are completed.

Course repo (canonical source for cohort dates / current syllabus): https://github.com/DataTalksClub/data-engineering-zoomcamp

For all date-bound questions ("when does the cohort start", "what are the deadlines", etc.), the answer should redirect readers to the course repo rather than hardcode a year.

---

## Stage 1 — Fix sort_order conflicts

Many entries within the same section share `sort_order`, making rendered ordering non-deterministic. Renumber sequentially per section.

- [x] `general/` — duplicate `20` (partitioning vs leaderboard); also gaps and out-of-order
- [x] `module-1/` — duplicates at `12, 25, 27, 40, 60, 76, 127`
- [x] `module-2/` — duplicate `1` (5x), `9` (2x), `11` (4x), `19` (3x), `24` (2x), `60` (2x)
- [x] `module-3/` — duplicates at `25, 26, 40, 45`
- [x] `module-4/` — duplicates at `1, 10, 60`
- [x] `module-6/` — no conflict, but verify
- [x] `module-7/` — duplicate `29`
- [x] `project/` — verify
- [x] `workshop-1-dlthub/` — verify

After renumbering, also fix files with non-standard ID format / filename:
- [x] `m1/015_docker-docker-wont-start-or.md` (id: '3549528659')
- [x] `m1/044_docker-compose-persist-pgadm.md` (id: '4146155608')
- [x] `m1/074_postgres-operationalerror.md` (id: '3459487271')
- [x] `general/057_27a95dd_homework-and-leaderboard-wha.md` (id: '05727a95dd')
- [x] `workshop/018_9950018686_dlt-column-names-snake-case.md` (id: '9950018686')

---

## Stage 2 — Move misplaced files

| File | From | To | Reason |
|---|---|---|---|
| [x] `general/020_46d95787b3_partitioning-vs-clustering` | general | module-3 | BigQuery topic |
| [x] `general/058_4f69163546_monitor-ram-local-pipelines-wsl` | general | module-5 | About local Bruin pipelines |
| [x] `m1/012_91a298833a_codespaces-kestra-forwarded-port` | module-1 | module-2 | Kestra is M2 |
| [x] `m1/023_5b4fb0c0a8_environment-is-github-codespaces-an-alternative-to` | module-1 | general | Environment topic |
| [x] `m3/001_c717810bc6_kestra-backfill-showing` | module-3 | module-2 | Pure Kestra |
| [x] `m3/002_687d54c6ba_docker-docker-compose-takes-infinitely-long-to-ins` | module-3 | module-1 | General Docker |
| [x] `m3/031_a32ed35da6_dim_zonessql-dataset-was-not-found-in-location-us` | module-3 | module-4 | dbt syntax |
| [x] `m3/033_dcb8885c9b_vms-what-do-i-do-if-my-vm-runs-out-of-space` | module-3 | general | Plus mentions Prefect (also outdated, see Stage 4) |
| [x] `m4/001_b72ed00c7b_warning-when-run-load_yellow_data-python-script` | module-4 | module-3 | GCS upload |
| [x] `m4/016_cdbabdd71a_gcp-vm-all-of-sudden-ssh-stopped-working-for-my-vm` | module-4 | module-1 | Setup, also outdated Prefect |
| [x] `m4/017_6022cc0440_gcp-free-trial-account-error` | module-4 | general | Setup |
| [x] `m4/018_c01d835b44_gcp-vm-if-you-have-lost-ssh-access-to-your-machine` | module-4 | module-1 | Setup |
| [x] `m4/089_d07a9a8ff9_duckdb-io-lock-suspend` | module-4 | module-5 | Bruin uses DuckDB |
| [x] `m4/091_f1e752882b_libduckdb-lib-missing-wsl-windows` | module-4 | module-5 | Bruin |
| [x] `m6/001_98b6a15ece_documentation-or-book-sign-not-shown-even-after-do` | module-6 | module-4 | Pure dbt |
| [x] `m7/001_5b1d465332_spark-is-working-however-nothing-appears-in-the-sp` | module-7 | module-6 | Pure Spark |
| [x] `m7/029_8fe89183d7_how-to-fix-connection-failed-connection-to-server` | module-7 | module-1 | Postgres setup |
| [x] `project/001_56d8f7ae9a_why-is-my-table-not-being-created-in-postgresql-wh` | project | module-1 | Generic |
| [x] `project/006_a3776dc060_how-to-run-python-as-a-startup-script` | project | general | Too generic |
| [x] `project/007_ce77e05d24_spark-streaming-how-do-i-read-from-multiple-topics` | project | module-7 | Streaming |
| [x] `project/013_b3bb998ae2_how-to-connect-pyspark-with-bigquery` | project | module-6 | Spark+BQ |
| [x] `project/016_7ece5b3182_is-it-possible-to-create-external-tables-in-bigque` | project | module-3 | BQ topic |
| [x] `workshop/001_70072fcf7a_solving-dbt-athena-library-conflicts` | workshop-1 | module-4 | Not dlt content |

After each move: re-prefix the file with the next available sort_order in the destination section, update the `sort_order:` in frontmatter accordingly.

---

## Stage 3 — Merge duplicate clusters

For each cluster: pick one canonical file as the merge target, fold useful content from the rest into it (often as separate "Cause N / Solution N" subsections), then delete the others.

### Module 1
- [x] **Postgres connection failures**: merge `059, 061, 064, 065, 071, 072, 073, 074, 075` into one "Postgres / pgcli connection troubleshooting" entry.
- [x] **pgcli/psycopg/libpq install**: merge `062, 063, 066, 069, 071, 076 (52858)` (note: 071 already part of cluster above — pick one canonical home).
- [x] **Docker compose hostname does not resolve**: merge `031, 038, 039, 040 (432d3), 082`.
- [x] **Postgres data folder permissions**: merge `013, 021, 025 (4e92), 027, 028, 035, 054`.
- [x] **Windows Docker volume mount syntax**: merge `019, 022, 023, 024`.
- [x] **pgAdmin persistence**: merge `042, 044 (4146), 045, 081`.
- [x] **docker-compose binary install**: merge `046, 047, 049, 050, 052`.
- [x] **SQLAlchemy ImportErrors**: merge `089, 090, 091, 092` (and revisit `076 (52858)` overlap).

### Module 2
- [x] **Kestra GCP service account auth**: merge `008, 011 (all 4 variants), 017`.
- [x] **`host.docker.internal` on Linux**: merge `014, 015, 016`.

### Module 3
- [x] **GCS / BigQuery region mismatch**: merge `010, 011, 020`.
- [x] **External vs native tables**: merge `028, 034, 035`.
- [x] **BigQuery limits**: merge `025 (45b58), 026 (0888d), 045 (48ce1)` into a single "BQ partitioning/clustering limits".

### Module 4
- [x] **dbt + BigQuery region mismatch** (largest cluster — 11 files): merge `004, 005, 019, 028, 032, 048, 058, 066, 068, 070, 081`.
- [x] **`dbt_utils.surrogate_key` rename**: merge `020 + 027`.
- [x] **Main branch is read-only**: merge `033 + 034`.
- [x] **`bad int64 value` on green tripdata**: merge `053, 054, 055, 056`.
- [x] **Parquet column type mismatch**: merge `013, 044, 049, 062, 075, 076`.
- [x] **dbt CI with GitHub**: merge `035, 036, 067`.
- [x] **BQ permission denied for service account**: merge `021, 045, 058`.

### Module 6
- [x] **`Java gateway process exited`**: merge `011 + 022`.
- [x] **`'DataFrame' has no attribute 'iteritems'`**: merge `029 + 030 + 057`.
- [x] **`PicklingError: IndexError`**: merge `034 + 054`.
- [x] **`No module named 'py4j'`**: merge `013 + 014`.
- [x] **Spark Standalone Mode on Windows**: merge `031 + 040 + 046`.
- [x] **Hadoop winutils**: merge `018 + 043 + 044`.
- [x] **Insufficient SSD quota / Dataproc**: merge `052 + 058`.

### General
- [x] **Troubleshoot + how to ask**: merge `040 + 041`.
- [x] **Cloud trial / sandbox / payment**: merge `028 + 030`.
- [x] **Environment choice cluster**: consolidate `022, 023 (after move from m1), 024, 025, 027, 029, 030, 031, 036` into 2-3 well-structured entries (local vs Codespaces vs GCP vs AWS, OS friendliness, do I need to pay).

---

## Stage 4 — Outdated / broken content

- [x] `workshop/005` — body is truncated ("…with:" then nothing). Either fix or delete.
- [x] `workshop/013` — Frankenstein file mixing 4 unrelated topics. Split into separate FAQs (most belong in other sections).
- [x] `general/037` — references "module-05 & RisingWave workshop" — RisingWave not in current syllabus; remove or update.
- [x] `m1/121` — pins Terraform 1.1.3; either delete or note it's archival.
- [x] `m4/045, 080` — Mage references; rewrite for Kestra or delete.
- [x] `m4/011, project/011` — Mage orchestration recipes; delete or rewrite for Kestra.
- [x] `m4/013` — references "Modify Airflow DAG"; clean up.
- [x] `m4/071` — uses `execution_date.strftime` (Airflow); update or delete.
- [x] `m4/064` — Python 3.9.9-slim Dockerfile reference; verify still relevant.
- [x] `m6/all spark-3.0.3 / Python 3.11 incompatibility entries` — verify against current course Spark version; update or delete.
- [x] `m7/006` — `pip install kafka-python==1.4.6` (very old pin); update to current.
- [x] `m7/022` — explicitly says Faust unmaintained. Move to a "legacy" callout or delete.
- [x] `m3/030, m3/032` — BQ ML model export recipes; verify still in syllabus.

---

## Stage 5 — Refresh date-bound content (point at course repo)

Decision: Instead of hardcoding cohort years, redirect to the course repo for current dates.

- [x] `general/001` "When does the course start?" → "Cohorts run roughly January–April each year. See the course repo for the current cohort start date and registration link."
- [x] `general/006` "How many Zoomcamps in a year?" — keep general info, remove year-pinned schedule, link to https://datatalks.club/blog/guide-to-free-online-courses-at-datatalks-club.html.
- [x] `general/007` "Is the current cohort going to be different?" — generalize to "each cohort may use updated tooling; check the course repo's `cohorts/` folder".
- [x] `general/010` YouTube playlists — keep main playlist link, drop year-by-year breakdown (or move to course repo reference).
- [x] `general/016` "Homework and project deadlines" → "Deadlines for the active cohort are published on the course website and in the cohort folder of the repo."
- [x] `general/020 (leaderboard, 7255a)` — remove hardcoded 2024/2025 enrollment URLs; use a placeholder pattern.
- [x] `general/021` "Is Python 3.9 still recommended in 2024?" — drop the year, just describe current recommendation.
- [x] `general/046` "How do I get my certificate?" — drop hardcoded `de-zoomcamp-2025` URL; use placeholder pattern.

---

## Stage 6 — Re-sectioning proposals

Larger structural changes; do these last after content is cleaned.

- [x] **Split `general` into two**:
  - `general` keeps course logistics (cohort, certificate, homework, project rules, leaderboard, contributing).
  - New `environment` (or `setup`) section for: GCP vs Codespaces, Python version, Windows/WSL/Mac, Git, troubleshooting workflow, books.
- [x] **Module 7 scope**: renamed to just "Streaming" in `_metadata.yaml`.
- [x] **Project section**: keep procedural items only (peer review, datasets, deadlines, attempts). Move integration recipes (`009, 010, 011, 014, 015, 018`) either back to relevant module sections or to a new `integrations` appendix.
- [x] (Optional) Add subsection ordering hints inside large sections (module-1 has 145 entries → split into Taxi data / Docker / WSL / Postgres / pgAdmin / Python+SQLAlchemy / GCP setup / Terraform / Misc).

---

## Notes on execution

- After every merge, verify no other files reference the deleted file's `id:` via `#hashlink`. If they do, update those links to point to the merged target.
- After every move, run a quick scan to catch broken cross-references.
- Update each file's `sort_order:` in frontmatter after each section is renumbered (don't only rely on filename prefix).
- The `_metadata.yaml` for the course doesn't need changes unless we add/rename sections (Stage 6).
