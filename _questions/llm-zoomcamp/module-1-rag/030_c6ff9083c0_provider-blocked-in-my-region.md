---
id: c6ff9083c0
question: An AI provider (OpenAI/Gemini) is blocked, unavailable in my region, or I
  just don't want to use it — what can I do?
sort_order: 30
---

You can use **any LLM from any provider** for the course — it isn't tied to OpenAI or Gemini. So if a provider is blocked in your region (or you simply prefer another one), just switch to something else:

- **Hosted, OpenAI-compatible providers** — e.g. Groq, OpenRouter, DeepSeek, Z.ai, Mistral. The course code uses the OpenAI client, so you usually only need to change the `base_url`, the API key, and the model name.
- **Open models via Hugging Face** (e.g. Qwen, Llama) if you prefer hosted open-source models.
- **Serve a model locally** with [Ollama](https://ollama.com/), [vLLM](https://github.com/vllm-project/vllm), LM Studio, or anything else — no external API call at all, so regional blocks don't apply and you don't need a paid key. Most of these also expose an OpenAI-compatible endpoint, so the course code works with only a `base_url` change.
- **A VPN** also works if you just need to reach a provider that's blocked at the network level.

Anything with an OpenAI-compatible endpoint (or a locally served model) will work — pick whatever is available and convenient for you.
