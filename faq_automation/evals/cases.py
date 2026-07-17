"""
Eval cases for the FAQ merge agent.

Each case is a real proposal from GitHub issues (this session and prior history).
Cases are grouped by the failure pattern they test. Each case declares the expected
decision and a set of checks that the agent's output must pass.

Sources:
  - This session's 6 PRs (#290-#302) — issue bodies are the original proposals
  - Prior bot PRs from the gitlog — issue bodies contain the original proposals
  - Correction commits show what humans had to fix after the bot's decision

How to add new cases:
  1. Find the issue: `gh issue view <N> --json body`
  2. Find the PR: `gh pr view <N> --json body` (check what the bot decided)
  3. Find corrections: trace commits touching the file after the bot's commit
  4. Add an EvalCase with the original question/answer and the expected outcome
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class EvalCase:
    """
    A single eval case.

    course:       course directory under _questions/
    issue_number: the GitHub issue number this case came from (0 = synthetic)
    question:     the proposed FAQ question (as submitted)
    answer:       the proposed FAQ answer (as submitted)
    expected_action: NEW | UPDATE | DUPLICATE | WRONG_COURSE
    expected_section: the section_id the entry should land in (for NEW/UPDATE)
    description:  short human-readable description of what this case tests
    checks:       list of (name, predicate) pairs. The predicate receives the
                  FAQDecision object and returns True if the check passes.
    tags:            categorization tags for pattern analysis
    relevant_doc_id: the 10-char doc_id of the FAQ entry this issue became.
                     For NEW cases, the runner removes this doc from the index
                     so the agent can't trivially find it as a duplicate.
    """
    course: str
    issue_number: int
    question: str
    answer: str
    expected_action: str
    expected_section: Optional[str] = None
    description: str = ""
    checks: list = field(default_factory=list)
    tags: list = field(default_factory=list)
    relevant_doc_id: str = ""


# -- Check predicates --------------------------------------------------------

def action_is(expected):
    def check(decision):
        return decision.action == expected
    check.__name__ = f"action == {expected}"
    return check


def section_is(expected):
    def check(decision):
        return decision.section_id == expected
    check.__name__ = f"section == {expected}"
    return check


def suggested_course_is(expected):
    def check(decision):
        return decision.suggested_course == expected
    check.__name__ = f"suggested_course == {expected}"
    return check


def not_wrong_course(decision):
    """The proposal belongs to the course it was filed under — do not reject it."""
    return decision.action != 'WRONG_COURSE'


def no_structural_headers(decision):
    """Content should not use ### headers — flows as prose per CONTRIBUTING.md."""
    content = decision.proposed_content or ""
    for line in content.split('\n'):
        stripped = line.strip()
        if stripped.startswith('#'):
            return False
    return True


def no_sort_order_collision(section_sort_orders):
    """
    Returns a check that verifies the agent's chosen order (if a specific number,
    not -1) does not collide with existing sort_orders in the target section.
    """
    existing = set(section_sort_orders)
    def check(decision):
        if decision.order == -1:
            return True
        return decision.order not in existing
    check.__name__ = "sort_order not colliding with existing"
    return check


def content_is_runnable_python(decision):
    """
    Heuristic: if the content has a fenced python block, check that names used
    as function arguments or attribute accesses are at least defined somewhere
    in the content (imports, assignments, class defs, function params).
    """
    import re
    content = decision.proposed_content or ""
    blocks = re.findall(r'```python\n(.*?)```', content, re.DOTALL)
    if not blocks:
        return True

    defined = set()
    for line in content.split('\n'):
        line = line.strip()
        for pattern in [
            r'^import\s+(\w+)',
            r'^from\s+[\w.]+\s+import\s+(.+)',
            r'^(\w+)\s*=',
            r'^class\s+(\w+)',
            r'^def\s+(\w+)',
            r'for\s+(\w+)\s+in',
        ]:
            for m in re.finditer(pattern, line):
                name = m.group(1).strip()
                if name and not name.startswith('_'):
                    defined.add(name)
        m = re.match(r'^from\s+[\w.]+\s+import\s+(.+)', line)
        if m:
            for name in m.group(1).split(','):
                name = name.strip().split(' as ')[-1].strip()
                if name:
                    defined.add(name)

    import builtins
    safe = set(dir(builtins))
    safe.update({'self', 'cls', 'messages', 'response', 'result', 'client', 'model'})

    for block in blocks:
        for m in re.finditer(r'(?:response_format|parse|model|format)\s*=\s*([A-Z]\w+)', block):
            name = m.group(1)
            if name not in defined and name not in safe:
                return False
        for m in re.finditer(r'(?<!\w\.)([A-Z]\w+)\s*\(', block):
            name = m.group(1)
            if name not in defined and name not in safe:
                return False

    return True


def content_is_concise(decision):
    """Content should not be excessively long for an FAQ."""
    content = decision.proposed_content or ""
    lines = content.strip().split('\n')
    if len(lines) > 40:
        return False
    return True


def has_filename_slug(decision):
    """Filename slug should not be None or 'None'."""
    slug = decision.filename_slug
    if slug is None:
        return False
    if slug and slug.lower() == 'none':
        return False
    return True


def has_trailing_newline(decision):
    """Content should end with a newline."""
    content = decision.proposed_content or ""
    return content.endswith('\n')


def content_has_no_bold_headers(decision):
    """Bold-only lines used as section headers should be avoided in favor of flowing prose."""
    content = decision.proposed_content or ""
    for line in content.split('\n'):
        stripped = line.strip()
        if stripped.startswith('**') and stripped.endswith('**') and len(stripped) < 80:
            return False
    return True


# -- Eval cases --------------------------------------------------------------

CASES = []

# ========================================================================== #
# GROUP 1: Correct action decision (NEW vs DUPLICATE vs UPDATE)
# ========================================================================== #

# Case 1: PR #296 — should be DUPLICATE (existing module-3 Kestra providers entry)
CASES.append(EvalCase(
    course="llm-zoomcamp",
    issue_number=295,
    question="How can I configure Kestra to use a different LLM provider instead of Google Gemini?",
    answer="""Kestra supports multiple LLM providers through its AI Provider plugins, so you're not limited to Google Gemini. To use a different provider: choose a supported provider, configure credentials, and update your flow.""",
    expected_action="DUPLICATE",
    description="Kestra provider config — should be DUPLICATE (already covered by module-3 provider entry)",
    checks=[action_is("DUPLICATE")],
    tags=["duplicate-detection"],
))

# Case 2: Dataset count is transient, not FAQ-worthy. Issue #287 raised this against
# the wrong course (see the WRONG_COURSE group); this variant refiles it under the
# course it belongs to, so the transient rule is what's under test here.
CASES.append(EvalCase(
    course="llm-zoomcamp",
    issue_number=287,
    question="Should I be concerned that number of documents in FAQ dataset is 1350, not 1208 like in module 02 - vector-search, lesson 04?",
    answer="I suppose that course is not fully updated where it is not crucial but would like to be sure. There are also similar differences in module 01.",
    expected_action="DUPLICATE",
    description="Dataset count discrepancy — too transient/specific for an FAQ, should be DUPLICATE or not created",
    checks=[action_is("DUPLICATE")],
    tags=["duplicate-detection", "relevance"],
))

# Case 3: PR #290 — valid NEW, correct section
CASES.append(EvalCase(
    course="llm-zoomcamp",
    issue_number=289,
    question="Why do I get IndexError: list index out of range when accessing the best chunk?",
    answer="""This usually happens when the number of embeddings does not match the number of document chunks. Make sure you create embeddings directly from the chunk list.""",
    expected_action="NEW",
    expected_section="module-2-vector-search",
    description="IndexError vector search — valid NEW for module-2",
    checks=[action_is("NEW"), section_is("module-2-vector-search")],
    tags=["correct-new"],
    relevant_doc_id="1a7b27c4df",
))

# Case 4: PR #292 — valid NEW
CASES.append(EvalCase(
    course="llm-zoomcamp",
    issue_number=291,
    question="How do I fix the Docker error 'mounts denied: The path /tmp/... is not shared from the host'?",
    answer="""Add the path to Docker File Sharing: Open Docker Desktop, Settings > Resources > File Sharing, add /tmp, restart.""",
    expected_action="NEW",
    expected_section="module-3",
    description="Docker mounts denied — valid NEW for module-3",
    checks=[action_is("NEW"), section_is("module-3")],
    tags=["correct-new"],
    relevant_doc_id="dd8b4c9fda",
))


# Case 6: Issue #300 — duplicate of existing Kestra secrets entries (closed manually)
CASES.append(EvalCase(
    course="llm-zoomcamp",
    issue_number=300,
    question="The provided Kestra flows reference {{ secret('GEMINI_API_KEY') }} but the lesson docs don't spell out where/how to register that secret when running Kestra locally via Docker Compose.",
    answer="""Kestra reads secrets from environment variables prefixed with SECRET_, base64-encoded. So for GEMINI_API_KEY, set export SECRET_GEMINI_API_KEY=$(echo -n "your-real-key" | base64). Add that under the Kestra service environment block, restart the container.""",
    expected_action="DUPLICATE",
    description="Kestra secret config — should be DUPLICATE (already covered by module-3 entries about API key config and base64 secrets)",
    checks=[action_is("DUPLICATE")],
    tags=["duplicate-detection"],
    relevant_doc_id="c8ca21af33",
))

# Case 5: PR #271 — should be DUPLICATE or not NEW (asking for project examples)
CASES.append(EvalCase(
    course="data-engineering-zoomcamp",
    issue_number=270,
    question="Do you have an example of a Data Engineering Zoomcamp final project built on AWS with Airflow, S3, Athena, and a dashboard?",
    answer="""A good AWS-based project would use Airflow for orchestration, S3 for storage, Athena for querying, and a BI tool for dashboards.""",
    expected_action="DUPLICATE",
    description="AWS project example request — not FAQ-worthy, should be DUPLICATE (project examples section already exists)",
    checks=[action_is("DUPLICATE")],
    tags=["relevance"],
))

# ========================================================================== #
# GROUP 2: Section placement
# ========================================================================== #

# Case 6: Issue #199 — merge vs append placed in module-3, should be workshop-1-dlthub
CASES.append(EvalCase(
    course="data-engineering-zoomcamp",
    issue_number=198,
    question="When should I use merge instead of append?",
    answer="""Use merge when existing data can be updated. If a record with the same primary key already exists, it will be updated. If it does not exist, it will be inserted. Common use cases: order status updates, user profile changes, CDC-based data processing.""",
    expected_action="NEW",
    expected_section="workshop-1-dlthub",
    description="Merge vs append — dlt topic, should go to workshop-1-dlthub, NOT module-3 (bot placed in module-3, human moved it)",
    checks=[action_is("NEW"), section_is("workshop-1-dlthub")],
    tags=["section-misplacement", "dlt"],
    relevant_doc_id="2442e32be2",
))

# Case 7: Issue #201 — rest_api_source vs @dlt.resource placed in general, should be workshop-1-dlthub
CASES.append(EvalCase(
    course="data-engineering-zoomcamp",
    issue_number=200,
    question="What is the difference between rest_api_source({...}) and @dlt.resource in dlt, and when should I use each?",
    answer="""Both are official dlt patterns. The main difference is level of control. JSON config (rest_api_source) is declarative. Custom code (@dlt.resource) is programmatic and more flexible.""",
    expected_action="NEW",
    expected_section="workshop-1-dlthub",
    description="dlt rest_api_source vs @dlt.resource — bot put in general, human moved to workshop-1-dlthub",
    checks=[action_is("NEW"), section_is("workshop-1-dlthub")],
    tags=["section-misplacement", "dlt"],
    relevant_doc_id="0655c8c637",
))

# Case 8: Issue #203 — dlt schema evolution placed in module-3, should be workshop-1-dlthub
CASES.append(EvalCase(
    course="data-engineering-zoomcamp",
    issue_number=202,
    question="How does dlt handle schema evolution?",
    answer="""dlt automatically detects and adapts to most schema changes during ingestion. If new columns appear, dlt adds them. If columns disappear, they remain. If types change, dlt tries safe coercion.""",
    expected_action="NEW",
    expected_section="workshop-1-dlthub",
    description="dlt schema evolution — bot put in module-3, human moved to workshop-1-dlthub",
    checks=[action_is("NEW"), section_is("workshop-1-dlthub")],
    tags=["section-misplacement", "dlt"],
    relevant_doc_id="3a53549d08",
))

# Case 9: Issue #188 — DuckDB lock placed in general, should be module-4 (dbt/DuckDB)
CASES.append(EvalCase(
    course="data-engineering-zoomcamp",
    issue_number=187,
    question='Why does DuckDB show "IO Error: Could not set lock on file" after pressing Ctrl+Z in Ubuntu, and how can it be fixed?',
    answer="""Pressing Ctrl+Z while running duckdb does not exit — it suspends the process. The DuckDB process continues running in the background and still holds a lock on the database file.""",
    expected_action="NEW",
    expected_section="module-4",
    description="DuckDB lock error — bot put in general, human moved to module-4 (dbt/DuckDB)",
    checks=[action_is("NEW"), section_is("module-4")],
    tags=["section-misplacement"],
    relevant_doc_id="d07a9a8ff9",
))

# Case 10: Issue #205 — Bruin MCP placed in general, should be module-5
CASES.append(EvalCase(
    course="data-engineering-zoomcamp",
    issue_number=204,
    question="How do I add the Bruin MCP server to VS Code?",
    answer="""Open the command palette, search for MCP: Add Server, choose Command (stdio), enter 'bruin mcp', name it 'bruin'.""",
    expected_action="NEW",
    expected_section="module-5",
    description="Bruin MCP server — bot put in general, human moved to module-5 (Data Platforms)",
    checks=[action_is("NEW"), section_is("module-5")],
    tags=["section-misplacement", "bruin"],
    relevant_doc_id="d5328f1899",
))

# Case 11: Issue #189 — Bruin multi-projects placed in general, should be module-5
CASES.append(EvalCase(
    course="data-engineering-zoomcamp",
    issue_number=189,
    question="Can I have multiple Bruin projects inside the same Git repository?",
    answer="""Yes, but because bruin init automatically places the .bruin.yml in the Git root, you need to manually relocate the config file and explicitly tell Bruin where it lives.""",
    expected_action="NEW",
    expected_section="module-5",
    description="Bruin multi-projects — bot put in general, human moved to module-5",
    checks=[action_is("NEW"), section_is("module-5")],
    tags=["section-misplacement", "bruin"],
    relevant_doc_id="f04da64de9",
))

# Case 12: Issue #168 — dbt from Kestra, should be module-2 (orchestration)
CASES.append(EvalCase(
    course="data-engineering-zoomcamp",
    issue_number=167,
    question="Can I run my dbt project from Kestra?",
    answer="""Yes, you can integrate dbt with Kestra to combine dbt's transformation capabilities with Kestra's orchestration, monitoring, and Git integration.""",
    expected_action="NEW",
    expected_section="module-2",
    description="dbt from Kestra — valid NEW for module-2 (orchestration)",
    checks=[action_is("NEW"), section_is("module-2")],
    tags=["section-placement"],
    relevant_doc_id="e14f6a8ed9",
))

# Case 13: HW Q2 cosine — should be module-2-homework not module-2-vector-search
CASES.append(EvalCase(
    course="llm-zoomcamp",
    issue_number=0,
    question="In Module 2 Homework Q2, cosine similarity is not in the options and I get a different model — what's wrong?",
    answer="""You may be using the wrong model. The homework expects a specific embedding model.""",
    expected_action="NEW",
    expected_section="module-2-homework",
    description="HW Q2 cosine — should go to module-2-homework (from git history fix)",
    checks=[action_is("NEW"), section_is("module-2-homework")],
    tags=["section-misplacement"],
))

# Issue #303 / PR #304 — Gemini workflow model error placed in module-1-rag,
# should be module-3 (Kestra orchestration)
CASES.append(EvalCase(
    course="llm-zoomcamp",
    issue_number=303,
    question="gemini-2.5-flash (or other model) is not available. What do I do?",
    answer="""Models become deprecated & workflows will produce errors like this:

```json
{
    "error": {
        "code": 404,
        "message": "This model models/gemini-2.5-flash is no longer available to new users. Please update your code to use a newer model for the latest features and improvements.",
        "status": "NOT_FOUND"
    }
}
```

Try updating your workflow `.yml` documents to use `gemini-3.5-flash` instead. Then re-run the workflow.

If this answer is outdated, review documentation for available models.""",
    expected_action="NEW",
    expected_section="module-3",
    description="Gemini model unavailable in workflow YAML — should go to module-3 orchestration, not module-1-rag",
    checks=[action_is("NEW"), section_is("module-3")],
    tags=["section-misplacement", "retrieval-bias", "kestra"],
    relevant_doc_id="d51bbe2da0",
))

# ========================================================================== #
# GROUP 3: Content quality — code, headers, formatting
# ========================================================================== #

# Case 14: PR #302 — code with undefined variables
CASES.append(EvalCase(
    course="llm-zoomcamp",
    issue_number=301,
    question="How can I get structured output (Pydantic objects) from Gemini via the OpenAI-compatible endpoint when responses.parse isn't available?",
    answer="""Use the OpenAI SDK's chat-completions parsing flow. Example:

```python
client = OpenAI(api_key=os.getenv("GEMINI_API_KEY"), base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
response = client.chat.completions.parse(model="gemini-3.1-flash-lite", messages=messages, response_format=Questions)
result = response.choices[0].message.parsed
```""",
    expected_action="NEW",
    expected_section="module-1-rag",
    description="Structured output from Gemini — code must define Pydantic model and messages",
    checks=[action_is("NEW"), section_is("module-1-rag"), content_is_runnable_python, no_structural_headers],
    tags=["code-quality"],
    relevant_doc_id="341f71f28c",
))

# Case 15: PR #298 — structural headers in content
CASES.append(EvalCase(
    course="llm-zoomcamp",
    issue_number=297,
    question="Why does a generic AI assistant generate Kestra flow YAML with properties that don't exist, and how can I avoid it?",
    answer="""A general AI isn't grounded in Kestra's plugin schemas. It may surface plausible but invalid property names. Cross-check against the official plugin docs and use Kestra's AI Copilot.""",
    expected_action="NEW",
    expected_section="module-3",
    description="Kestra YAML hallucinated properties — content should not have structural headers",
    checks=[action_is("NEW"), section_is("module-3"), no_structural_headers],
    tags=["content-formatting"],
    relevant_doc_id="93a3e8b98c",
))

# Case 16: PR #294 — verbose/generic content
CASES.append(EvalCase(
    course="llm-zoomcamp",
    issue_number=293,
    question="Why is token usage monitored in Kestra workflows?",
    answer="""Token usage tracking helps measure cost and efficiency of LLM-based workflows.""",
    expected_action="NEW",
    expected_section="module-3",
    description="Token usage — should be concise, no structural headers, not verbose",
    checks=[action_is("NEW"), section_is("module-3"), no_structural_headers, content_is_concise],
    tags=["content-formatting", "verbosity"],
    relevant_doc_id="a4adc70f41",
))

# Case 17: Issue #202 — content with ## headers (schema evolution)
CASES.append(EvalCase(
    course="data-engineering-zoomcamp",
    issue_number=202,
    question="How does dlt handle schema evolution?",
    answer="""## What happens when the source schema changes?

If new columns appear, dlt adds the new columns to the destination table.
If existing columns disappear, the columns remain in the table.
If existing columns change their data type, dlt will try to safely coerce the data.

## How it works under the hood

dlt uses a schema propagation mechanism that tracks column types.""",
    expected_action="NEW",
    description="dlt schema evolution — proposed answer has ## headers that should be stripped",
    checks=[action_is("NEW"), no_structural_headers],
    tags=["content-formatting"],
    relevant_doc_id="3a53549d08",
))

# Case 18: Issue #194 — None filename slug
CASES.append(EvalCase(
    course="data-engineering-zoomcamp",
    issue_number=193,
    question="Why are there unexpected years in lpep_pickup_datetime after loading taxi data into BigQuery?",
    answer="""This usually happens due to a corrupted or incorrect load process. Common causes: CSV schema autodetect misinterpreting timestamp format, or mixing Parquet and CSV loads into the same table.""",
    expected_action="NEW",
    description="BigQuery timestamp years — bot generated 'None' as filename slug (human fixed it)",
    checks=[action_is("NEW"), has_filename_slug],
    tags=["filename-slug"],
))

# ========================================================================== #
# GROUP 4: Correct NEW entries from various courses (positive cases)
# ========================================================================== #

# Case 19: PR #275 — OpenRouter 402 error
CASES.append(EvalCase(
    course="llm-zoomcamp",
    issue_number=274,
    question="OpenRouter: Error code 402 when calling responses.create (max_output_tokens)",
    answer="""OpenRouter can return APIStatusError with code 402 when responses.create() is called without a max_output_tokens limit. Pass a lower limit: max_output_tokens=1024.""",
    expected_action="NEW",
    expected_section="module-1-homework",
    description="OpenRouter 402 error — valid NEW for module-1-homework",
    checks=[action_is("NEW"), section_is("module-1-homework")],
    tags=["correct-new"],
    relevant_doc_id="cfb07a27d5",
))

# Case 20: PR #277 — np.allclose precision
CASES.append(EvalCase(
    course="llm-zoomcamp",
    issue_number=276,
    question="Why can np.allclose(scores, scores_loop) return False when comparing the matrix and loop approaches?",
    answer="""Matrix multiplication and element-wise loops can produce slightly different floating-point results due to the order of operations.""",
    expected_action="NEW",
    expected_section="module-2-vector-search",
    description="np.allclose precision — valid NEW for module-2",
    checks=[action_is("NEW"), section_is("module-2-vector-search")],
    tags=["correct-new"],
    relevant_doc_id="e889793af9",
))

# Case 21: PR #279 — why uv
CASES.append(EvalCase(
    course="llm-zoomcamp",
    issue_number=278,
    question="Why use uv package/project manager instead of the more traditional Python tools like pip, venv, and poetry?",
    answer="""uv is a fast Python package manager written in Rust that combines dependency resolution, virtual environment management, and project management.""",
    expected_action="NEW",
    expected_section="module-1-rag",
    description="Why uv — valid NEW for module-1-rag",
    checks=[action_is("NEW"), section_is("module-1-rag")],
    tags=["correct-new"],
    relevant_doc_id="f81dea8f7e",
))

# Case 22: PR #263 — Kestra error messages
CASES.append(EvalCase(
    course="llm-zoomcamp",
    issue_number=262,
    question="How to fix Python logs shown as Kestra error messages?",
    answer="""Kestra captures stderr output as error logs. Use stdout or configure the logging level.""",
    expected_action="NEW",
    expected_section="module-3",
    description="Kestra error messages — valid NEW for module-3",
    checks=[action_is("NEW"), section_is("module-3")],
    tags=["correct-new"],
    relevant_doc_id="8d33e30f9a",
))

# Case 23: PR #257 — Spark with BigQuery
CASES.append(EvalCase(
    course="data-engineering-zoomcamp",
    issue_number=256,
    question="How do I use Spark with BigQuery as a data source and sink?",
    answer="""Use the spark-bigquery-connector to read from and write to BigQuery from Spark.""",
    expected_action="NEW",
    expected_section="module-6",
    description="Spark + BigQuery — valid NEW for module-6 (Spark). Agent falsely matches dbt+BigQuery entry as duplicate.",
    checks=[action_is("NEW"), section_is("module-6")],
    tags=["correct-new", "false-duplicate"],
    relevant_doc_id="2b59e8e6c1",
))

# Case 24: PR #259 — edit Kestra flows locally
CASES.append(EvalCase(
    course="data-engineering-zoomcamp",
    issue_number=258,
    question="How can I edit Kestra flows locally with Docker Compose and keep them version controlled?",
    answer="""Mount your flows directory as a volume in docker-compose.yml so Kestra reads from your local files.""",
    expected_action="NEW",
    expected_section="module-2",
    description="Edit Kestra flows locally — valid NEW. Agent falsely matches dbt+Kestra entry as duplicate.",
    checks=[action_is("NEW"), section_is("module-2")],
    tags=["correct-new", "false-duplicate"],
    relevant_doc_id="958ab42c43",
))

# ========================================================================== #
# GROUP 5: UPDATE and DUPLICATE edge cases
# ========================================================================== #

# Case 25: Provider FAQ — should be UPDATE or DUPLICATE, not degrade content
CASES.append(EvalCase(
    course="llm-zoomcamp",
    issue_number=0,
    question="Do I have to use OpenAI, or can I use a different provider?",
    answer="""You can use any LLM provider — the course isn't tied to OpenAI. Switch to Groq, OpenRouter, DeepSeek, Gemini, or serve locally with Ollama or vLLM.""",
    expected_action="UPDATE",
    description="Provider FAQ — if UPDATE chosen, content must not degrade the existing comprehensive answer",
    checks=[no_structural_headers, content_is_concise],
    tags=["update-quality"],
))

# Case 26: Issue #197 — dlt MCP server in VS Code
CASES.append(EvalCase(
    course="data-engineering-zoomcamp",
    issue_number=196,
    question="How do I add the dlt MCP server in VS Code?",
    answer="""Open the command palette, search for MCP: Add Server, choose Command (stdio), type the dlt-mcp command, set the id to 'dlt'.""",
    expected_action="NEW",
    expected_section="workshop-1-dlthub",
    description="dlt MCP server VS Code — should go to workshop-1-dlthub",
    checks=[action_is("NEW"), section_is("workshop-1-dlthub")],
    tags=["section-placement", "dlt"],
    relevant_doc_id="cbeb6f678b",
))

# Case 27: Issue #147 — BigQuery DDL
CASES.append(EvalCase(
    course="data-engineering-zoomcamp",
    issue_number=146,
    question="How to obtain the DDL of a table in BigQuery?",
    answer="""Use the INFORMATION_SCHEMA.TABLES view to get the DDL: SELECT ddl FROM project.dataset.INFORMATION_SCHEMA.TABLES WHERE table_name = 'my_table'""",
    expected_action="NEW",
    expected_section="module-3",
    description="BigQuery DDL — valid NEW for module-3 (Data Warehousing)",
    checks=[action_is("NEW"), section_is("module-3")],
    tags=["correct-new"],
    relevant_doc_id="7df3102580",
))

# Case 28: Issue #108 — docker -i vs -t (DE zoomcamp)
CASES.append(EvalCase(
    course="data-engineering-zoomcamp",
    issue_number=107,
    question="What's the difference between -i and -t in docker run -it?",
    answer="""-i keeps STDIN open even if not attached. -t allocates a pseudo-TTY. Together (-it) they give you an interactive terminal.""",
    expected_action="NEW",
    expected_section="module-1-docker",
    description="docker -i vs -t — valid NEW for module-1-docker",
    checks=[action_is("NEW"), section_is("module-1-docker")],
    tags=["correct-new"],
))

# ========================================================================== #
# GROUP 6: Content quality edge cases
# ========================================================================== #

# Case 29: Proposal with bold-only headers that should be prose
CASES.append(EvalCase(
    course="data-engineering-zoomcamp",
    issue_number=202,
    question="How does dlt handle schema evolution?",
    answer="""dlt automatically detects and adapts to most schema changes during ingestion.

**What happens when the source schema changes?**

If new columns appear, dlt adds the new columns to the destination table.

**How it works under the hood**

dlt uses a schema propagation mechanism that tracks column types.""",
    expected_action="NEW",
    description="dlt schema evolution — bold-only lines as headers should be converted to prose",
    checks=[action_is("NEW"), content_has_no_bold_headers],
    tags=["content-formatting"],
    relevant_doc_id="3a53549d08",
))

# Case 30: Outdated API reference (chat.completions vs Responses)
CASES.append(EvalCase(
    course="llm-zoomcamp",
    issue_number=0,
    question="How do I call the LLM using the OpenAI API in the course?",
    answer="""Use the OpenAI SDK's chat.completions.create method:

```python
from openai import OpenAI
client = OpenAI()
response = client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": "Hello"}])
```""",
    expected_action="NEW",
    description="Outdated API — content using deprecated chat.completions when course uses Responses API",
    checks=[no_structural_headers],
    tags=["code-quality"],
))

# Case 31: PR #286 — ONNX download hang
CASES.append(EvalCase(
    course="llm-zoomcamp",
    issue_number=285,
    question="Why does download.py hang at 0% when downloading model.onnx from Hugging Face?",
    answer="""The download can hang due to network issues or large file size. Use a direct download URL or wget with resume support.""",
    expected_action="NEW",
    expected_section="module-2-vector-search",
    description="ONNX download hang — valid NEW for module-2-vector-search",
    checks=[action_is("NEW"), section_is("module-2-vector-search")],
    tags=["correct-new"],
    relevant_doc_id="29b69fbe0b",
))

# Case 32: PR #249 — PyFlink session window (DE streaming)
CASES.append(EvalCase(
    course="data-engineering-zoomcamp",
    issue_number=248,
    question="PyFlink session window job fails with 'please declare primary key for sink table' error",
    answer="""The error occurs because the sink table needs a primary key declaration for upsert mode.""",
    expected_action="NEW",
    expected_section="module-7",
    description="PyFlink session window — valid NEW for module-7. Agent falsely matches Spark timestamp entry.",
    checks=[action_is("NEW"), section_is("module-7")],
    tags=["correct-new", "false-duplicate"],
    relevant_doc_id="e08b9c753f",
))

# Case 33: PR #251 — wget CloudFront download
CASES.append(EvalCase(
    course="data-engineering-zoomcamp",
    issue_number=250,
    question="Why does wget fail to download the CloudFront parquet file even with --no-check-certificate?",
    answer="""CloudFront may block wget's default user agent. Use a browser user agent.""",
    expected_action="NEW",
    expected_section="module-1-data",
    description="wget CloudFront — valid NEW. No duplicate exists (f6dedaf769 not in current FAQ).",
    checks=[action_is("NEW"), section_is("module-1-data")],
    tags=["correct-new", "false-duplicate"],
    relevant_doc_id="",
))

# ========================================================================== #
# GROUP 7: DUPLICATE verification (doc IN index — agent should find it)
# These confirm the agent correctly identifies existing entries.
# ========================================================================== #

# Verify: IndexError vector search entry exists -> should be DUPLICATE
CASES.append(EvalCase(
    course="llm-zoomcamp",
    issue_number=289,
    question="Why do I get IndexError: list index out of range when accessing the best chunk?",
    answer="The number of embeddings does not match the number of document chunks.",
    expected_action="DUPLICATE",
    description="DUPLICATE verification — IndexError entry exists in FAQ, agent should find it",
    checks=[action_is("DUPLICATE")],
    tags=["duplicate-verify"],
))

# Verify: Bruin MCP entry exists -> should be DUPLICATE
CASES.append(EvalCase(
    course="data-engineering-zoomcamp",
    issue_number=204,
    question="How do I add the Bruin MCP server to VS Code?",
    answer="Open command palette, MCP Add Server, choose Command stdio, enter bruin mcp.",
    expected_action="DUPLICATE",
    description="DUPLICATE verification — Bruin MCP entry exists in FAQ, agent should find it",
    checks=[action_is("DUPLICATE")],
    tags=["duplicate-verify"],
))

# Verify: DuckDB lock entry exists -> should be DUPLICATE
CASES.append(EvalCase(
    course="data-engineering-zoomcamp",
    issue_number=187,
    question="Why does DuckDB show IO Error Could not set lock on file after pressing Ctrl+Z?",
    answer="Pressing Ctrl+Z suspends the process instead of exiting.",
    expected_action="DUPLICATE",
    description="DUPLICATE verification — DuckDB lock entry exists in FAQ, agent should find it",
    checks=[action_is("DUPLICATE")],
    tags=["duplicate-verify"],
))

# Verify: OpenRouter 402 entry exists -> should be DUPLICATE
CASES.append(EvalCase(
    course="llm-zoomcamp",
    issue_number=274,
    question="OpenRouter Error code 402 when calling responses.create max_output_tokens",
    answer="Pass a lower max_output_tokens limit in your responses.create call.",
    expected_action="DUPLICATE",
    description="DUPLICATE verification — OpenRouter 402 entry exists in FAQ, agent should find it",
    checks=[action_is("DUPLICATE")],
    tags=["duplicate-verify"],
))

# Verify: dlt schema evolution entry exists -> should be DUPLICATE
CASES.append(EvalCase(
    course="data-engineering-zoomcamp",
    issue_number=202,
    question="How does dlt handle schema evolution?",
    answer="dlt automatically detects and adapts to most schema changes.",
    expected_action="DUPLICATE",
    description="DUPLICATE verification — dlt schema evolution entry exists in FAQ",
    checks=[action_is("DUPLICATE")],
    tags=["duplicate-verify"],
))

# ========================================================================== #
# GROUP 8: WRONG_COURSE — student picked the wrong course in the dropdown
# The `course` field is what the student selected; the content belongs elsewhere.
# ========================================================================== #

# Case: Issue #311 — RAG monitoring code filed under ML zoomcamp
CASES.append(EvalCase(
    course="machine-learning-zoomcamp",
    issue_number=311,
    question="How do I adapt the RAGWithMetrics class to work with OpenAI-compatible endpoints like Google Gemini?",
    answer="""The course material leverages OpenAI's Responses API (`client.responses.create`), which is not universally implemented by other LLM providers. To use `RAGWithMetrics` with Gemini via its OpenAI-compatible endpoint, switch the internal execution to `chat.completions.create` and adjust the extraction paths: the text moves to `response.choices[0].message.content`, and token usage moves to `usage.prompt_tokens` / `usage.completion_tokens`.""",
    expected_action="WRONG_COURSE",
    description="RAGWithMetrics monitoring — LLM zoomcamp module-5 content filed under ML zoomcamp",
    checks=[action_is("WRONG_COURSE"), suggested_course_is("llm-zoomcamp")],
    tags=["wrong-course"],
))

# Case: Issue #287 — LLM zoomcamp vector search dataset filed under ML zoomcamp
CASES.append(EvalCase(
    course="machine-learning-zoomcamp",
    issue_number=287,
    question="Should I be concerned that number of documents in FAQ dataset is 1350, not 1208 like in module 02 - vector-search, lesson 04?",
    answer="I suppose that course is not fully updated where it is not crucial but would like to be sure. There are also similar differences in module 01.",
    expected_action="WRONG_COURSE",
    description="FAQ dataset doc count — LLM zoomcamp vector search content filed under ML zoomcamp",
    checks=[action_is("WRONG_COURSE"), suggested_course_is("llm-zoomcamp")],
    tags=["wrong-course"],
))

# Case: Issue #148 — BigQuery cost estimation filed under ML zoomcamp
# The same proposal was refiled correctly as issue #150 (data-engineering-zoomcamp).
CASES.append(EvalCase(
    course="machine-learning-zoomcamp",
    issue_number=148,
    question="How we can estimate the cost of executed queries within a specified range of time in bigquery, and determine what users and when in time this executions were made.",
    answer="""The metadata table that contains all the history related with query and Jobs executions is called 'JOBS_BY_PROJECT' and we can find it in the path `<your_project_id>.<your_region>.INFORMATION_SCHEMA.JOBS_BY_PROJECT`; the following query must be executed within the bigquery query editor.

```sql
SELECT
  DATE(creation_time) as date,
  user_email,
  SUM(total_bytes_billed) / 1099511627776 * 6.25 as estimated_cost_usd,
  COUNT(*) as query_count
FROM `project-id.region-us.INFORMATION_SCHEMA.JOBS_BY_PROJECT`
WHERE creation_time >= DATE_ADD(CURRENT_TIMESTAMP(), INTERVAL -60 DAY)
GROUP BY date, user_email
ORDER BY estimated_cost_usd DESC
```""",
    expected_action="WRONG_COURSE",
    description="BigQuery query cost — DE zoomcamp content filed under ML zoomcamp (refiled correctly as #150)",
    checks=[action_is("WRONG_COURSE"), suggested_course_is("data-engineering-zoomcamp")],
    tags=["wrong-course"],
))

# Case: Issue #97 — Spark global temp views filed under ML zoomcamp
# The same proposal was refiled correctly as issues #96/#98 (data-engineering-zoomcamp).
CASES.append(EvalCase(
    course="machine-learning-zoomcamp",
    issue_number=97,
    question="How do you share a DataFrame across multiple Spark sessions?",
    answer="""Spark provides Global Temporary Views to share DataFrames across different Spark sessions within the same Spark application. Unlike regular temporary views, global temporary views are accessible from any session.

```python
df.createOrReplaceGlobalTempView('trips_global')
spark.sql("SELECT * FROM global_temp.trips_global").show()
```

Global temporary views are stored in the `global_temp` database and must be referenced using the `global_temp.` prefix.""",
    expected_action="WRONG_COURSE",
    description="Spark global temp views — DE zoomcamp content filed under ML zoomcamp (refiled correctly as #96/#98)",
    checks=[action_is("WRONG_COURSE"), suggested_course_is("data-engineering-zoomcamp")],
    tags=["wrong-course"],
))

# Case: Issue #109 — pgAdmin/Postgres Docker setup filed under ML zoomcamp
CASES.append(EvalCase(
    course="machine-learning-zoomcamp",
    issue_number=109,
    question="GitHub Codespaces: Running pgadmin in Docker",
    answer="""With the default instructions, running pgAdmin in Docker may result in a blank screen after logging into the pgAdmin console. This is due to session or proxy issues behind Codespaces' reverse proxy. Add `PGADMIN_CONFIG_PROXY_X_HOST_COUNT: 1` and `PGADMIN_CONFIG_PROXY_X_PREFIX_COUNT: 1` to the pgAdmin service environment, then restart the container.""",
    expected_action="WRONG_COURSE",
    description="pgAdmin in Codespaces — DE zoomcamp module-1 content filed under ML zoomcamp",
    checks=[action_is("WRONG_COURSE"), suggested_course_is("data-engineering-zoomcamp")],
    tags=["wrong-course"],
))

# Case: synthetic — MLflow model registry filed under DE zoomcamp
CASES.append(EvalCase(
    course="data-engineering-zoomcamp",
    issue_number=0,
    question="How do I promote a model from Staging to Production in the MLflow model registry?",
    answer="""Use the MLflow client to transition the model version stage:

```python
from mlflow.tracking import MlflowClient
client = MlflowClient()
client.transition_model_version_stage(name="nyc-taxi-regressor", version=2, stage="Production")
```

The registry keeps the full version history, so you can roll back by transitioning an earlier version back to Production.""",
    expected_action="WRONG_COURSE",
    description="MLflow model registry — MLOps zoomcamp content filed under DE zoomcamp",
    checks=[action_is("WRONG_COURSE"), suggested_course_is("mlops-zoomcamp")],
    tags=["wrong-course", "synthetic"],
))

# Case: synthetic — Terraform/GCS bucket filed under LLM zoomcamp
CASES.append(EvalCase(
    course="llm-zoomcamp",
    issue_number=0,
    question="Why does terraform apply fail with 'Error 403: Request violates constraint constraints/gcp.resourceLocations' when creating the GCS bucket?",
    answer="""Your GCP organization policy restricts which regions resources can be created in. Change the `location` in your `google_storage_bucket` resource to an allowed region, or ask your org admin to relax the `gcp.resourceLocations` constraint for your project.""",
    expected_action="WRONG_COURSE",
    description="Terraform GCS bucket — DE zoomcamp module-1 content filed under LLM zoomcamp",
    checks=[action_is("WRONG_COURSE"), suggested_course_is("data-engineering-zoomcamp")],
    tags=["wrong-course", "synthetic"],
))

# ========================================================================== #
# GROUP 9: WRONG_COURSE false-positive guards
# Near misses that must NOT be rejected as wrong course. Every case outside
# this group is also an implicit guard — the runner fails any case that
# unexpectedly returns WRONG_COURSE.
# ========================================================================== #

# Guard: Docker is DE's signature tool but ML zoomcamp deploys with it too
CASES.append(EvalCase(
    course="machine-learning-zoomcamp",
    issue_number=0,
    question="Why does my Docker container exit immediately after running docker run for the churn prediction service?",
    answer="""The container exits when its main process finishes. If your Dockerfile's `CMD` runs a script that returns, there is nothing left to keep the container alive. Serve the model with a long-running process instead, e.g. `CMD ["gunicorn", "--bind", "0.0.0.0:9696", "predict:app"]`.""",
    expected_action="NEW",
    description="Docker container exits — shared tool, but ML zoomcamp owns model deployment. Must not be WRONG_COURSE.",
    checks=[action_is("NEW")],
    tags=["wrong-course-guard", "synthetic"],
))

# Guard: Kestra is DE's signature tool but the LLM course uses it in module-3
CASES.append(EvalCase(
    course="llm-zoomcamp",
    issue_number=0,
    question="How do I pass the output of one Kestra task as input to the next task in the flow?",
    answer="""Reference the upstream task's output with an expression, e.g. `{{ outputs.extract.vars.uri }}`. Kestra only exposes outputs that the task declares, so check the task's output attributes in the plugin documentation.""",
    expected_action="NEW",
    description="Kestra task outputs — shared tool, but LLM zoomcamp module-3 covers Kestra. Must not be WRONG_COURSE.",
    checks=[action_is("NEW")],
    tags=["wrong-course-guard", "synthetic"],
))

# Guard: course-agnostic tooling belongs to whichever course it was filed under
CASES.append(EvalCase(
    course="machine-learning-zoomcamp",
    issue_number=0,
    question="How do I add a package to an existing uv project without recreating the virtual environment?",
    answer="""Run `uv add <package>` from the project directory. It resolves the dependency, updates `pyproject.toml` and `uv.lock`, and installs into the existing `.venv`. Use `uv sync` afterwards on other machines to reproduce the same environment.""",
    expected_action="NEW",
    description="uv package management — course-agnostic tooling. Must not be WRONG_COURSE.",
    checks=[action_is("NEW")],
    tags=["wrong-course-guard", "synthetic"],
))

# Guard: an uncovered topic inside the course is NEW, not WRONG_COURSE
CASES.append(EvalCase(
    course="machine-learning-zoomcamp",
    issue_number=0,
    question="Why does my ROC AUC score come out below 0.5 on the churn validation set?",
    answer="""An AUC below 0.5 means the model ranks positives below negatives — usually the predicted probabilities are inverted. Check that you pass the probability of the positive class, `y_pred = model.predict_proba(X_val)[:, 1]`, and not column 0.""",
    expected_action="NEW",
    description="ROC AUC below 0.5 — squarely ML zoomcamp classification. Must not be WRONG_COURSE.",
    checks=[action_is("NEW")],
    tags=["wrong-course-guard", "synthetic"],
))
