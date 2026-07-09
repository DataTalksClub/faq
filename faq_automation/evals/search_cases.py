"""
Ground-truth dataset for search/retrieval eval.

Each case is a real FAQ proposal issue paired with the doc_id of the FAQ entry
it became (for NEW/UPDATE) or duplicated. The eval checks whether the FAQ agent's
search index returns the right doc_id in the top-k results.

Cases are built from GitHub issues + git history. Synthetic edge cases are appended
to test specific retrieval failure modes (vague queries, cross-module confusion, etc.)
"""

# Real cases: (course, query_text, relevant_doc_id, issue_number, note)
# The query_text is the issue's question (or question + answer prefix for richer context).
# The relevant_doc_id is the 10-char id from the FAQ file's frontmatter.

REAL_CASES = [
    # llm-zoomcamp
    ("llm-zoomcamp", "How do I get structured output (Pydantic objects) from Gemini through the OpenAI-compatible endpoint?", "341f71f28c", 301, ""),
    ("llm-zoomcamp", "Why does a generic AI assistant generate invalid Kestra plugin properties?", "93a3e8b98c", 297, ""),
    ("llm-zoomcamp", "Why is token usage monitored in Kestra workflows?", "a4adc70f41", 293, ""),
    ("llm-zoomcamp", "How do I fix the Docker error mounts denied path not shared from the host?", "dd8b4c9fda", 291, ""),
    ("llm-zoomcamp", "Why do I get IndexError list index out of range when accessing the best chunk?", "1a7b27c4df", 289, ""),
    ("llm-zoomcamp", "Why does download.py hang at 0% when downloading model.onnx from Hugging Face?", "29b69fbe0b", 285, ""),
    ("llm-zoomcamp", "Why use uv package manager instead of pip venv poetry?", "f81dea8f7e", 278, ""),
    ("llm-zoomcamp", "Why can np.allclose return False comparing matrix vs loop vector search?", "e889793af9", 276, ""),
    ("llm-zoomcamp", "OpenRouter Error code 402 when calling responses.create max_output_tokens", "cfb07a27d5", 274, ""),
    ("llm-zoomcamp", "How do I start using Google Gemini models through the OpenAI-compatible endpoint?", "0ae5c221b9", 272, ""),
    ("llm-zoomcamp", "How to fix Python logs shown as Kestra error messages?", "8d33e30f9a", 262, ""),

    # data-engineering-zoomcamp
    ("data-engineering-zoomcamp", "How do I use Spark with BigQuery as a data source and sink?", "f57e5cb1f4", 256, ""),
    ("data-engineering-zoomcamp", "How can I edit Kestra flows locally with Docker Compose?", "e14f6a8ed9", 258, ""),
    ("data-engineering-zoomcamp", "How do I authenticate dbt with BigQuery when service account key creation is disabled?", "5039707c1a", 268, ""),
    ("data-engineering-zoomcamp", "Why use dbt and BigQuery instead of handling all transformations in Python?", "8c9c97f690", 266, ""),
    ("data-engineering-zoomcamp", "Why is the pipeline structured into multiple layers instead of directly analyzing raw data?", "a198f6959c", 264, ""),
    ("data-engineering-zoomcamp", "How to sync data from PostgreSQL to BigQuery for analytics?", "9950018686", 254, ""),
    ("data-engineering-zoomcamp", "How to structure a layered data warehouse raw clean analytics in a batch pipeline?", "a198f6959c", 252, ""),
    ("data-engineering-zoomcamp", "Unable to download parquet file using wget from the TLC Trip Record Data website.", "f6dedaf769", 250, ""),
    ("data-engineering-zoomcamp", "PyFlink session window aggregation fails with declare primary key for sink table", "1da0437718", 248, ""),
    ("data-engineering-zoomcamp", "Flink tumbling window job runs but the PostgreSQL table is empty", "b7ff18706c", 246, ""),
    ("data-engineering-zoomcamp", "PyFlink job keeps restarting with JSON deserialization error", "5e953f0e8e", 244, ""),
    ("data-engineering-zoomcamp", "How to inspect messages in a Kafka topic using offsets?", "9116d0a2a1", 242, ""),
    ("data-engineering-zoomcamp", "Spark error when casting TIMESTAMP_NTZ to BIGINT", "d845dedf73", 240, ""),
    ("data-engineering-zoomcamp", "Why does Spark write multiple parquet files after repartitioning a dataset?", "236aa3c6e4", 237, ""),
    ("data-engineering-zoomcamp", "How to calculate trip duration using Spark timestamps?", "8d33e30f9a", 235, ""),
    ("data-engineering-zoomcamp", "What is the difference between a Spark application job stage and task?", "4d5aa45b03", 228, ""),
    ("data-engineering-zoomcamp", "Incomplete data ingestion due to incorrect pagination starting point", "f97bbac843", 225, ""),
    ("data-engineering-zoomcamp", "Column name from API not found when querying dlt-loaded table", "3b78e09b80", 224, ""),
    ("data-engineering-zoomcamp", "dlt does not create some columns in DuckDB when loading REST API data", "1d0b969028", 222, ""),
    ("data-engineering-zoomcamp", "How do I generate the AGENTS.md file for Codex in dlt?", "f97bbac843", 221, ""),
    ("data-engineering-zoomcamp", "Bruin Python asset fails with ArrowInvalid Cannot locate timezone UTC", "e955c6b69e", 219, ""),
    ("data-engineering-zoomcamp", "Bruin seed timeout with ingestr and DuckDB", "79792b53fc", 217, ""),
    ("data-engineering-zoomcamp", "Fix Bruin time_interval first-run failure", "a500273add", 215, ""),
    ("data-engineering-zoomcamp", "Fix libduckdb.so missing on WSL Windows", "81eb85c2dd", 213, ""),
    ("data-engineering-zoomcamp", "When should I use merge instead of append?", "2442e32be2", 198, ""),
    ("data-engineering-zoomcamp", "What is the difference between rest_api_source and @dlt.resource?", "0655c8c637", 200, ""),
    ("data-engineering-zoomcamp", "How does dlt handle schema evolution?", "3a53549d08", 202, ""),
    ("data-engineering-zoomcamp", "Why does DuckDB show IO Error Could not set lock on file after pressing Ctrl+Z?", "d07a9a8ff9", 187, ""),
    ("data-engineering-zoomcamp", "How do I add the Bruin MCP server to VS Code?", "d5328f1899", 204, ""),
    ("data-engineering-zoomcamp", "Can I have multiple Bruin projects inside the same Git repository?", "f04da64de9", 189, ""),
    ("data-engineering-zoomcamp", "Can I run my dbt project from Kestra?", "e14f6a8ed9", 167, ""),
    ("data-engineering-zoomcamp", "How do I add the dlt MCP server in VS Code?", "cbeb6f678b", 196, ""),
    ("data-engineering-zoomcamp", "How to obtain the DDL of a table in BigQuery?", "7df3102580", 146, ""),

    # machine-learning-zoomcamp
    ("machine-learning-zoomcamp", "When running parse_xg_output I get an error with XGB evals result", "91ff5cb6b6", 35, ""),
    ("machine-learning-zoomcamp", "FastAPI deployment pickle model issues", "69e5f9cbf8", 33, ""),
    ("machine-learning-zoomcamp", "Docker file has a new pipenv grpcio conflict for module 10", "0b60cbb594", 29, ""),
    ("machine-learning-zoomcamp", "What if my answer doesn't match the options in the Homework?", "917b0b0fb5", 25, ""),
    ("machine-learning-zoomcamp", "TypeError while creating OneHotEncoder object", "548dcc8a3c", 23, ""),
]

# Synthetic edge cases: test specific retrieval failure modes
SYNTHETIC_CASES = [
    # Vague queries — should still find the right entry
    ("llm-zoomcamp", "It crashes when I try to search", "1a7b27c4df", 0, "vague: IndexError search crash"),
    ("llm-zoomcamp", "the download just hangs", "29b69fbe0b", 0, "vague: ONNX hang"),
    ("llm-zoomcamp", "getting a 402 error", "cfb07a27d5", 0, "vague: OpenRouter 402"),
    ("data-engineering-zoomcamp", "docker compose won't start", "30dcc71db8", 0, "vague: Docker volume backup"),
    ("data-engineering-zoomcamp", "my data is wrong after loading", "52e74f0053", 0, "vague: BigQuery unexpected years"),

    # Cross-module confusion — tool name appears in multiple modules
    ("data-engineering-zoomcamp", "DuckDB connection error in dbt", "d07a9a8ff9", 0, "cross-module: DuckDB in dbt context"),
    ("data-engineering-zoomcamp", "Kestra Docker volume not working", "e14f6a8ed9", 0, "cross-module: Kestra+Docker"),

    # Error message exact match — should retrieve the matching troubleshooting entry
    ("llm-zoomcamp", "IndexError: list index out of range", "1a7b27c4df", 0, "exact error message"),
    ("data-engineering-zoomcamp", "IO Error: Could not set lock on file", "d07a9a8ff9", 0, "exact error message"),
    ("llm-zoomcamp", "APIStatusError: Error code: 402", "cfb07a27d5", 0, "exact error message"),

    # Homework-specific — should find homework section entries
    ("llm-zoomcamp", "Module 2 homework vector search results don't match", "e889793af9", 0, "homework context"),
    ("data-engineering-zoomcamp", "homework 6 Spark record counts don't match", "4d5aa45b03", 0, "homework context"),

    # Negative case — query that shouldn't match anything strongly
    ("llm-zoomcamp", "What is the meaning of life?", "NONE", 0, "negative: should return no strong match"),

    # Paraphrased — different wording, same concept
    ("data-engineering-zoomcamp", "How to get the table creation SQL from BigQuery", "7df3102580", 0, "paraphrased: DDL query"),
    ("data-engineering-zoomcamp", "Running dbt transformations inside Kestra orchestrator", "e14f6a8ed9", 0, "paraphrased: dbt+Kestra"),
    ("llm-zoomcamp", "Parse JSON response into Python objects with Gemini", "341f71f28c", 0, "paraphrased: structured output"),

    # Real duplicate: issue #300 closed as duplicate of two existing Kestra secret entries.
    # Ground truth: primary match is the API key config entry, secondary is the base64 fix.
    ("llm-zoomcamp", "How to set GEMINI_API_KEY secret for the Kestra flows in Module 3 homework?", "3860e5fe8b", 300, "duplicate: Kestra secrets, two relevant docs"),
    ("llm-zoomcamp", "Kestra flow fails with missing GEMINI_API_KEY secret using docker compose", "c8ca21af33", 300, "duplicate: Kestra base64 secret, second relevant doc"),
]

ALL_CASES = REAL_CASES + SYNTHETIC_CASES
