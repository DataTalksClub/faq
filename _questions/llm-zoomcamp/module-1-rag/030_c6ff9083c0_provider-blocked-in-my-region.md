---
id: c6ff9083c0
question: Do I have to use OpenAI or Gemini, or can I use a different provider?
sort_order: 30
---

If the providers used in the course aren't available or are blocked in your region (or you simply prefer another one), you can use any other LLM provider — the course isn't tied to OpenAI or Gemini. Just switch to something else:

- Hosted, OpenAI-compatible providers — e.g. Groq, OpenRouter, DeepSeek, Z.ai, Mistral. The course code uses the OpenAI client, so you usually only need to change the `base_url`, the API key, and the model name.
- Open models via Hugging Face (e.g. Qwen, Llama) if you prefer hosted open-source models.
- Serve a model locally with [Ollama](https://ollama.com/), [vLLM](https://github.com/vllm-project/vllm), LM Studio, or anything else — no external API call at all, so regional blocks don't apply and you don't need a paid key. Most of these also expose an OpenAI-compatible endpoint, so the course code works with only a `base_url` change.
- Rent a GPU machine and serve the model there (e.g. with vLLM) if your own machine can't run the model you want. This gives you a private OpenAI-compatible endpoint to point the course code at — just remember to stop/delete the instance when you're done so you don't keep paying for it.
- A VPN also works if you just need to reach a provider that's blocked at the network level.

Anything with an OpenAI-compatible endpoint (or a locally served model) will work — pick whatever is available and convenient for you.
