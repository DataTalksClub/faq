# DataTalks.Club FAQ

Answers to the questions DataTalks.Club Zoomcamp students regularly ask, so they
can find them quickly. It's available at
[datatalks.club/faq](https://datatalks.club/faq).

Each course cohort brings thousands of students. They have the same problems:

- a Docker mount that fails on Windows
- an API that changed since the video was recorded
- a homework answer that doesn't match any of the options

The instructors have to answer the same question in every cohort. In this FAQ database,
we collect all these questions, so they can be used to help the students. We also
use it for the FAQ assistant in Slack to answer these questions automatically.

## The parts

The repository has several parts:

- [Content](#content) (`_questions/`): the answers, one markdown file per
  question, 1395 of them across 6 courses
- [FAQ automation](#faq-automation) (`faq_automation/`): the bot that reads a
  student's proposal issue and opens a pull request, or closes the issue if it's
  already answered
- [Evals](#evals) (`faq_automation/evals/`): test cases that measure how well the
  bot finds existing entries and picks the right action
- [Skills](#skills) (`.claude/skills/`): written procedures for the work
  maintainers do by hand, like adding an entry or reviewing open pull requests
- [The site](#the-site) (`website/`): the generator that builds datatalks.club/faq,
  plus a JSON copy of the content for other programs to read
- [The FAQ assistant](#the-faq-assistant): a Slack bot in
  [a separate repo](https://github.com/DataTalksClub/faq-assistant) that answers
  students using this FAQ as one of its sources

The rest of this README covers them in the same order.

## Content

Every FAQ record is a markdown file in `_questions/<course>/<section>/`.

In the frontmatter it contains:

- the unique id
- the question
- the sort order

The answer is in the body. 

Example for `001_74eb249bbf_i-just-discovered-the-course-can-i-still-join.md`:

```markdown
---
id: 74eb249bbf
question: I just discovered the course. Can I still join?
sort_order: 1
---

Yes, but if you want to receive a certificate, you need to submit your project
while we're still accepting submissions.
```

Each course has a `_metadata.yaml` file:

```yaml
course: llm-zoomcamp
course_name: "LLM Zoomcamp"
slack_channel: course-llm-zoomcamp
telegram_channel: llm_zoomcamp
sections:
  - id: general
    name: "General Course-Related Questions"
    comment: "Course logistics: cohort schedule, certificate, deadlines,
      leaderboard, project rules. Technical questions belong in the module
      sections."
```

Open a [FAQ proposal issue](https://github.com/DataTalksClub/faq/issues/new?template=faq-proposal.yml)
to add an answer, or send a PR to fix one that's already there. See
[CONTRIBUTING.md](CONTRIBUTING.md).

## FAQ automation

Anyone can contribute to the FAQ dataset:

- You submit an issue, specifying the question, the course and your answer.
- A GitHub Actions workflow indexes the entire dataset with minsearch.
- It searches twice - on the question alone, and on the question and answer together - and combines the two results with reciprocal rank fusion.
- It sends the results to OpenAI, which returns a structured decision: `NEW`, `UPDATE`, `DUPLICATE` or `WRONG_COURSE`.
- For `NEW` or `UPDATE`, it commits the file and opens a pull request.
- For `DUPLICATE` or `WRONG_COURSE`, it closes the issue.


The LLM then makes one structured call that returns the action, target section,
sort order, and rewritten content together as a single `FAQDecision`.

TODO include the schema here

We run `gpt-5.4-nano`. See the reasons in [docs/model-choice.md](docs/model-choice.md).

## Evals

We run two suites:

| Suite | What it tests | Cases | Runtime | Score |
|---|---|---|---|---|
| [Retrieval](#retrieval) (`run_search_eval.py`) | Retrieval | 25 | ~2s | recall@5 0.840 |
| [Generation](#generation) (`runner.py`) | Generation | 61 | ~2min | 42/61 on `gpt-5.4-nano` |

Cases come from real mistakes. If automation gets something wrong, it may become a test case for the evaluations. See the [eval guide](faq_automation/evals/README.md).

### Retrieval

In the first suite, we test retrieval. There are no calls to LLMs. 

We need it because:

- Retrieval is the ceiling. The model only sees the top 5 hits, so an entry
  search doesn't surface can't be recognized as a duplicate.
- We need a smoke test to make sure we don't accidentally break retrieval. The
  run fails if recall@5 drops below the recorded baseline.

Every case in the retrieval eval set is a hard query:

- vague symptoms: "the download just hangs"
- bare error messages: "IO Error: Could not set lock on file"
- rewordings that share no vocabulary with the entry they should find

Current performance: 

| | @1 | @3 | @5 |
|---|---|---|---|
| recall | 0.800 | 0.840 | 0.840 |
| MRR | 0.800 | 0.813 | 0.813 |



### Generation

In the second suite we test the whole flow. We check if:

- the action (`NEW`, `UPDATE`, `DUPLICATE` or `WRONG_COURSE`) is correct
- the session for the course is selected correctly 
- the code looks runnable, all the variables are defined variables
- the filename slug makes sense

Current performance:

| | Result |
|---|---|
| cases passing | 42/61 |
| valid proposals left open | 54/54 |
| wrong-course proposals closed | 0/7 |

The last row is a known limitation: the automation doesn't catch a proposal filed
under the wrong course. The student picks the course from a dropdown, and the
automation only ever sees that course's entries, so a wrong pick lands in
whichever section of that course fits least badly. Case #97 is a real one — an answer about
Spark global temporary views, submitted under ML Zoomcamp, should come back
`WRONG_COURSE` and close the issue. It comes back `NEW` in `misc` instead.

We leave it that way. The prompt demands positive evidence of another course and
files when unsure, which is what holds the row above it at 54/54. A miss costs a
wrong PR that a maintainer closes in seconds; the opposite mistake closes a valid
proposal with nobody looking. See [docs/model-choice.md](docs/model-choice.md).

We use the Flex tier for evals, so it's 50% cheaper than the usual API requests.
A batch run of this suite once sat at 0/51 completed for 2.7 hours, which is fine
for CI and useless for iterating.

## Skills

| Skill | What it does |
|-------|--------------|
| `add-faq-record` | Adds or updates a single entry from a question, a chat thread, or a screenshot. Pushes back when unclear course material caused the confusion, because fixing that material beats writing an FAQ around it. |
| `clear-backlog` | Resolves open FAQ PRs first and then issues, one item at a time. Checks placement, duplicates, and canonical sources before reviewing content quality; recommends eval coverage only for meaningful automation regressions. |
| `slack-faq-fetch` | Pulls recent Slack discussion for a course into a review export, to find the questions nobody has filed yet. |

## The site

`website/generate_website.py` reads every markdown file under `_questions/`,
parses the frontmatter, orders sections per `_metadata.yaml` and questions by
`sort_order`, then writes the content twice:

- the website: pages for students to read
- the JSON feed: the same answers for other programs to read

We use our own generator rather than Jekyll, and dbt is the reason. A good chunk
of the Data Engineering answers contain dbt code, and dbt writes its refs in Jinja
braces, `{{ ref('stg_trips') }}`, which Liquid claims as its own. Every dbt answer
would need escaping, that escaping would live in the source file where the next
person copies it, and an author who forgets breaks the build. Fighting the
templating on every dbt entry was more work than writing the generator.

### Website

One HTML page per course plus an index. Markdown runs through Pygments for syntax
highlighting and gets rendered into the Jinja2 templates in `_layouts/`.

Question ids become the anchors, so an entry keeps its URL when it moves between
sections.

### JSON

The same answers without the presentation. `json/courses.json` indexes the
courses, and each `json/<course>.json` is a flat list of entries:

```json
{
  "id": "74eb249bbf",
  "course": "llm-zoomcamp",
  "section": "General Course-Related Questions",
  "question": "I just discovered the course. Can I still join?",
  "answer": "Yes, but if you want to receive a certificate, you need to submit your project while we're still accepting submissions."
}
```

FAQ automation doesn't use this feed, because it runs inside the repo and reads
`_questions/` straight from disk. Other things do, and the closest one is a course:
LLM Zoomcamp students fetch `json/courses.json` in the first lesson and index it to
build their own RAG pipeline. We teach retrieval over the FAQ that the retrieval
bot answers from.

## The FAQ assistant

Students who ask in Slack rather than opening the site get answered by the
[FAQ assistant](https://github.com/DataTalksClub/faq-assistant), a separate Slack
bot that reads this content as one of its sources.

It runs as a single AWS Lambda with a prebuilt keyword index baked into the
deployment package, so there's no vector database and effectively no fixed cost.
Course channels search that course's FAQ plus the course material, and other
channels search the general [docs](https://github.com/DataTalksClub/docs) corpus.

## Working on it

You need Python 3.13 and [uv](https://docs.astral.sh/uv/). An OpenAI API key is
only needed for the automation and the evals, so the content and the site need
neither a key nor a service.

```bash
git clone https://github.com/DataTalksClub/faq
cd faq
uv sync --dev
```

### Building the site

`make website` builds the static site into `_site/`, and `make test` runs the 102
website tests and 77 automation tests.

```bash
make website
make test
```

### Running FAQ automation

Set a key and feed it an issue body. The key can also live in `.env`. The model
comes from `DEFAULT_MODEL` in `faq_automation/rag_agent.py`, and
`FAQ_MODEL=gpt-5.6-luna` overrides it for one run.

```bash
export OPENAI_API_KEY='...'

cat > test_issue.txt << 'EOF'
### Course
machine-learning-zoomcamp

### Question
How do I check my Python version?

### Answer
Run `python --version` in your terminal.
EOF

uv run python -m faq_automation.cli \
  --issue-body "$(cat test_issue.txt)" \
  --issue-number 42
```

### Running the evals

These need `OPENAI_API_KEY`. The first command runs every end-to-end case.
`--case` runs one `case_id`, where a positive number is a GitHub issue and a
negative one is a synthetic case, so pass those as `--case=-3`.
`--batch` sends the suite as one Batch API job for the same price, though it can
take hours to come back. The search eval needs no key. The last command re-runs
the wrong-course cases 5 times each to measure recall and false positives.

```bash
uv run --project faq_automation python -m faq_automation.evals.runner
uv run --project faq_automation python -m faq_automation.evals.runner --case 303
uv run --project faq_automation python -m faq_automation.evals.runner --batch
uv run --project faq_automation python -m faq_automation.evals.run_search_eval
uv run --project faq_automation python -m faq_automation.evals.probe_wrong_course gpt-5.4-nano 5
```

### Finding candidates

Pull recent Slack activity into review files, then read through them for questions
the FAQ is missing. Set `SLACK_BOT_TOKEN` in `.env` first. It lives in your
[Slack app](https://api.slack.com/apps) under OAuth and Permissions, as the Bot
User OAuth Token starting with `xoxb-`. By default this reads
`_questions/llm-zoomcamp/_metadata.yaml`, fetches the Slack channel named in its
`slack_channel` field, checks the last 7 days, and writes JSON and Markdown
exports to `.tmp/`. Use `--channel` only to override the metadata for one run.
`telegram_fetch` does the same for a course's public Telegram channel and needs
no token.

```bash
cp .env.example .env
uv run python -m faq_automation.slack_fetch
uv run python -m faq_automation.slack_fetch --course data-engineering-zoomcamp
uv run python -m faq_automation.telegram_fetch
```

## Repo layout

```text
faq/
├── _questions/<course>/         # the content: one markdown file per answer
│   ├── _metadata.yaml           # section ids, names, and placement comments
│   └── <section>/NNN_<id>_<slug>.md
├── faq_automation/              # the automation
│   ├── rag_agent.py             # prompt, FAQDecision schema, DEFAULT_MODEL
│   ├── cli.py                   # issue body in, decision JSON out
│   ├── actions.py               # writes files, builds PR bodies and comments
│   ├── core.py                  # frontmatter, metadata, sort order
│   ├── slack_fetch.py           # pulls candidate questions from Slack
│   ├── telegram_fetch.py        # the same for public Telegram channels
│   └── evals/                   # see evals/README.md
│       ├── search_cases.py      # 72 retrieval cases
│       ├── run_search_eval.py   # recall@k and MRR@k, no LLM calls
│       ├── cases.py             # 61 end-to-end cases + check predicates
│       ├── runner.py            # scores cases (flex tier by default)
│       ├── flex.py / batch.py   # the two discounted OpenAI tiers
│       └── probe_wrong_course.py # repeat-runs to measure decision stability
├── .claude/skills/              # add-faq-record, clear-backlog, slack-faq-fetch
├── website/                     # the static site generator
├── _layouts/  assets/           # Jinja2 templates and CSS
└── docs/model-choice.md         # why gpt-5.4-nano
```

## Continuous integration

| Workflow | Trigger | What it does |
|---|---|---|
| `faq-automation.yml` | Issue opened with the `faq-proposal` label | Runs the automation, then opens a PR or closes the issue |
| `test-faq-automation.yml` | PRs and pushes touching the bot | Runs the automation test suite |
| `test-website.yml` | PRs and pushes touching the site | Runs the website test suite |
| `build-website.yml` | Push to `main` | Rebuilds and deploys to GitHub Pages |

The evals don't run in CI. They cost money and move around enough that a single
run would produce flaky failures, as the
[eval README](faq_automation/evals/README.md) covers. Run them by hand when
changing the prompt, the model, or the search index.
