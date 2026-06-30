---
id: 3860e5fe8b
question: How do I configure the Gemini (and OpenAI/Tavily) API keys for the Kestra
  module?
sort_order: 1
---

Kestra reads secrets from environment variables that are prefixed with `SECRET_` and whose value is **base64-encoded**. You export them in the terminal *before* starting Kestra. For Gemini you need two variables — the plain one (used by the AI Copilot) and the base64-encoded `SECRET_` one (used by the flows):

```bash
export GEMINI_API_KEY="your-gemini-api-key-here"                              # used by AI Copilot
export SECRET_GEMINI_API_KEY=$(echo -n $GEMINI_API_KEY | base64)             # used by the flows
export SECRET_OPENAI_API_KEY=$(echo -n "your-openai-api-key-here" | base64)  # required for flow 3
export SECRET_TAVILY_API_KEY=$(echo -n "your-tavily-api-key-here" | base64)  # required for web search (flows 3, 5, 6)
```

Then start (or restart) Kestra so it picks up the variables:

```bash
docker compose up -d
```

Inside a flow, reference a secret **without** the `SECRET_` prefix:

```yaml
{{ secret('GEMINI_API_KEY') }}
```

See the [setup lesson](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/03-orchestration/lessons/03-setup.md) for the full walkthrough. Never commit your keys to Git.
