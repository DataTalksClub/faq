---
id: 6e1d8a7b29
question: 'OpenAI: "RateLimitError 429 / insufficient_quota" — my account has no credit'
sort_order: 13
---

```
RateLimitError: Error code: 429 - {'error': {'message': 'You exceeded your current quota...',
'type': 'insufficient_quota'}}
```

Despite the name, `insufficient_quota` is not a temporary rate-limit you can wait out — it means your OpenAI account has no paid credit. Two options:

- Add a small amount (~$5–$10) on https://platform.openai.com and use a cheap model like `gpt-4o-mini`.
- Switch to a free alternative:
  - [Groq](https://console.groq.com/) — free tier, OpenAI-compatible API, supports tool use.
  - [Google Gemini](https://aistudio.google.com/) — free tier, e.g. `gemini-2.0-flash`.
  - [Ollama](https://ollama.com/) — runs locally, fully free.

The course's curated list of OpenAI-compatible providers: https://github.com/DataTalksClub/llm-zoomcamp/blob/main/awesome-llms.md#openai-api-alternatives
