---
id: 0224d980b3
question: 'Groq vs OpenAI: starter.py crashes for missing `OPENAI_API_KEY`, and Groq
  404 / `responses.create` errors / tool-calling failures'
sort_order: 5
---

If you’re using Groq (or another provider) but your code still crashes with OpenAI-related errors, it’s usually one of these issues:

1) `starter.py` crashes with missing credentials even though you’re using Groq
- In many course codebases, `starter.py` contains a `demo`/`__main__` block that instantiates `client = OpenAI()`.
- If you `import starter` (e.g., `from starter import index`) Python executes the file top-to-bottom, including that `OpenAI()` construction line.
- Fix: add a placeholder value in your `.env` so construction doesn’t fail at import time:

```dotenv
OPENAI_API_KEY=not-needed-using-groq-instead
```

It doesn’t need to be a real key if you never actually call the OpenAI client.

2) Groq `404` / “model does not exist”
- Ensure you’re using a valid Groq model id for that provider. The same model name you used for OpenAI may not exist on Groq.

3) `responses.create` / OpenAI Responses API doesn’t work on Groq
- `client.responses.create(...)` and the OpenAI “Responses API” are OpenAI-specific. Groq (and other non-OpenAI providers) may not implement it.
- For Groq, use the older chat-completions API (e.g. `chat.completions.create`) instead.
- Also adjust how you read the response:
  - Prefer `response.choices[0].message.content`
  - Rather than OpenAI Responses fields like `response.output_text` (or `response.output` patterns).

4) Tool-calling/tool execution errors when switching providers
- If the agent/framework expects a specific tool schema or response shape from the OpenAI Responses API, you may need to override/adapt your `llm()` (and any `rag()` wrapper) so the provider’s response is converted into the shape the rest of the pipeline expects.

5) “Rate limit / request too large” retries won’t help if a single request exceeds your limit
- If the error says the *first request* already exceeds the cap (e.g., `Limit 8000, Requested 8581`) then waiting/retrying won’t fix it.
- Reduce prompt/context size per call, e.g. reduce retrieved context by lowering `num_results` (e.g., from 5 to 2) so the assembled input fits within the provider’s per-request/token limits.