"""
Ground-truth dataset for search/retrieval eval.

Each case is a SearchCase dataclass with fields: course, question, answer, doc_id,
case_id, note.

How the data was collected:

1. Listed all faq-proposal issues:
   `gh issue list --state all --label faq-proposal --limit 200`
2. For each issue, extracted the question and answer from the body:
   `gh issue view <N> --json body` then parse ### Question and ### Answer sections
3. Traced the issue to its PR to find the doc_id of the FAQ entry it became:
   `gh pr list --state all --search <case_id>` then extract the file's
   frontmatter id
4. Synthetic edge cases added for vague queries, cross-module confusion, exact
   errors, paraphrases, and negative cases.

To extend coverage: add more issues following the same process, or add synthetic
cases to test specific retrieval failure modes.
"""

from dataclasses import dataclass


@dataclass
class SearchCase:
    course: str           # course directory under _questions/
    question: str         # the issue question (reworded for some cases)
    answer: str           # proposed answer from the issue body (### Answer section)
    doc_id: str           # 10-char id from the FAQ entry's frontmatter
    case_id: int          # positive = GitHub issue number; negative = synthetic
    note: str = ""        # optional note (e.g. "reworded", edge case description)


REAL_CASES = [
    SearchCase('llm-zoomcamp', 'Why does FastEmbed crash with an SSL or network error even though the model is already cached locally?', 'Use the same cache directory and pass local_files_only=True after the cache has been populated.', '6609b934b6', 342, 'regression: cached FastEmbed model should retrieve offline-loading guidance'),
    SearchCase('llm-zoomcamp', 'Why does the dlt pipeline pull fewer rows or tables than expected right after running the agent?', 'Logfire may not have exported and indexed the complete trace before the pipeline queries it, which also undercounts the token total.', '8ede00dc4c', 336, 'regression: delayed Logfire trace ingestion in dlt workshop homework'),
    SearchCase('llm-zoomcamp', "Why doesn't my SQLite exporter receive any spans after I switch from ConsoleSpanExporter in Module 5?", 'A second global TracerProvider is not registered in the same notebook process, so spans continue to use the first provider and traces.db stays empty.', 'ba1d5f13e7', 329, 'regression: empty SQLite exporter and provider override are the same homework issue'),
    SearchCase('llm-zoomcamp', 'Should I be concerned that the number of documents in the FAQ dataset is 1350 instead of 1208 as shown in the vector-search video?', 'The course may have been updated since the video was recorded. Similar differences appear in Module 1.', 'e2d595f23c', 287, 'exact issue: vague answer must not bury the question match'),
    SearchCase('llm-zoomcamp', 'I used the same RAG code as the lecture, but my retrieved documents and final answer are different. Is my implementation wrong?', 'The course dataset changes over time. A notebook that downloads the latest documents builds a different index from the snapshot used when the lecture was recorded.', 'e2d595f23c', 287, 'reworded: mutable dataset differs from lecture snapshot'),
    SearchCase('llm-zoomcamp', 'LLM Zoomcamp Module 5 homework: why does starter.py require OPENAI_API_KEY when I use Groq, why does responses.create fail, and why do retries not fix a request that exceeds Groq token limits?', 'Configure starter.py with the Groq API key and OpenAI-compatible base URL. Use chat.completions.create instead of the OpenAI Responses API, select a model ID available on Groq, read response.choices[0].message.content, and reduce num_results when the retrieved context makes one request too large.', '01517c80df', 316, 'regression: retrieve monitoring-homework FAQ, not Module 1 ToyAIKit FAQ'),
    SearchCase('llm-zoomcamp', 'In the Kestra module, why do we track how many tokens the LLM uses?', 'Token usage tracking helps measure cost and efficiency of LLM-based workflows. It allows developers to optimize prompts, reduce unnecessary output, and control operational expenses in production systems.', 'a4adc70f41', 293, 'reworded'),
    SearchCase('llm-zoomcamp', 'My RAG code crashes when I try to get the top result — it says list index out of range', 'This usually happens when the number of embeddings does not match the number of document chunks.  Make sure you create embeddings directly from the chunk list:  contents = [chunk[\"content\"] for chunk in chunks] X = embedder.encode_batch(contents)  The number of rows in X should be equal to len(chu', '1a7b27c4df', 289, 'reworded'),
]

# Synthetic challenge cases: (course, question, answer, doc_id, case_id, note)
# answer is empty for synthetic cases
SYNTHETIC_CASES = [
    SearchCase('llm-zoomcamp', 'It crashes when I try to search', '', '1a7b27c4df', -1, 'vague: IndexError search crash'),
    SearchCase('llm-zoomcamp', 'the download just hangs', '', '29b69fbe0b', -2, 'vague: ONNX hang'),
    SearchCase('llm-zoomcamp', 'getting a 402 error', '', 'cfb07a27d5', -3, 'vague: OpenRouter 402'),
    SearchCase('data-engineering-zoomcamp', "docker compose won't start", '', '30dcc71db8', -4, 'vague: Docker volume backup'),
    SearchCase('data-engineering-zoomcamp', 'my data is wrong after loading', '', '52e74f0053', -5, 'vague: BigQuery unexpected years'),
    SearchCase('data-engineering-zoomcamp', 'DuckDB connection error in dbt', '', 'd07a9a8ff9', -6, 'cross-module: DuckDB in dbt context'),
    SearchCase('data-engineering-zoomcamp', 'Kestra Docker volume not working', '', 'e14f6a8ed9', -7, 'cross-module: Kestra+Docker'),
    SearchCase('llm-zoomcamp', 'IndexError: list index out of range', '', '1a7b27c4df', -8, 'exact error message'),
    SearchCase('data-engineering-zoomcamp', 'IO Error: Could not set lock on file', '', 'd07a9a8ff9', -9, 'exact error message'),
    SearchCase('llm-zoomcamp', 'APIStatusError: Error code: 402', '', 'cfb07a27d5', -10, 'exact error message'),
    SearchCase('llm-zoomcamp', "Module 2 homework vector search results don't match", '', 'e889793af9', -11, 'homework context'),
    SearchCase('data-engineering-zoomcamp', "homework 6 Spark record counts don't match", '', 'bcafec775a', -12, 'homework context'),
    SearchCase('data-engineering-zoomcamp', 'How to get the table creation SQL from BigQuery', '', '7df3102580', -14, 'paraphrased: DDL query'),
    SearchCase('data-engineering-zoomcamp', 'Running dbt transformations inside Kestra orchestrator', '', 'e14f6a8ed9', -15, 'paraphrased: dbt+Kestra'),
    SearchCase('llm-zoomcamp', 'Parse JSON response into Python objects with Gemini', '', '341f71f28c', -16, 'paraphrased: structured output'),
    SearchCase('llm-zoomcamp', 'How to set GEMINI_API_KEY secret for the Kestra flows in Module 3 homework?', '', '3860e5fe8b', 300, 'duplicate: Kestra secrets, two relevant docs'),
    SearchCase('llm-zoomcamp', 'Kestra flow fails with missing GEMINI_API_KEY secret using docker compose', '', 'c8ca21af33', 300, 'duplicate: Kestra base64 secret, second relevant doc'),
]

# Every case names the retrieval failure it exercises in its note. Exact
# proposal-to-FAQ matches are not kept: the entry was written from the proposal,
# so the wording is near-identical and keyword search finds it without being
# tested. They tell us nothing about the query the next student will type.
ALL_CASES = REAL_CASES + SYNTHETIC_CASES
