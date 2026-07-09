---
id: 8e21752415
question: How do I avoid hitting OpenAI rate limits (429 errors) during the course?
sort_order: 31
---

Free-tier and low-spend OpenAI accounts have per-minute and per-day request limits that are easy to blow through when a notebook loops over many documents. Reduce the number of API calls before you worry about handling the error after the fact.

- **Retry with backoff.** The `openai` Python client retries automatically with exponential backoff; raise the limit so transient 429s resolve themselves instead of crashing the run:

  ```python
  from openai import OpenAI

  client = OpenAI(max_retries=5)
  ```

- **Lower concurrency.** In a thread/process pool, keep the pool small (2-3 workers) so you stay under the per-minute cap. A larger pool finishes one batch fast and then fails on the next.
- **Cache results.** Write embeddings and LLM responses to disk (JSONL, pickle, or a vector DB) and reload on re-run. Re-executing a notebook should not re-call the API for inputs you already processed.
- **Batch where possible.** Group independent inputs into a single request (e.g. embed a list of texts in one call) instead of looping one-by-one.
- **Use a cheaper/free provider.** `gpt-4o-mini` is cheap enough for the whole course; Groq's free tier (`llama-3.3-70b-versatile`) has generous per-minute limits via the OpenAI-compatible endpoint.

If you already see `insufficient_quota`, that is a billing issue, not a rate limit — see [OpenAI: Error: RateLimitError: Error code: 429](openai-error-ratelimiterror-error-code-429).
