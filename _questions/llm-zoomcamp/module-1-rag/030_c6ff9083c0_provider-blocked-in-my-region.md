---
id: c6ff9083c0
question: An AI provider (OpenAI/Gemini) is blocked or unavailable in my region — what
  can I do?
sort_order: 30
---

You have several options:

- **Run models locally with [Ollama](https://ollama.com/)** — no external API call at all, so regional blocks don't apply. Good for following along without a paid key.
- **Use an OpenAI-compatible provider that's available where you are** — e.g. Groq, OpenRouter, or Z.ai. The course code uses the OpenAI client, so you usually only need to change the `base_url`, the API key, and the model name.
- **Use open models via Hugging Face** (e.g. Qwen) if you prefer hosted open-source models.
- **A VPN** also works if you just need to reach a provider that's blocked at the network level.

The course isn't tied to any single provider — anything with an OpenAI-compatible endpoint (or a local model) will do.
