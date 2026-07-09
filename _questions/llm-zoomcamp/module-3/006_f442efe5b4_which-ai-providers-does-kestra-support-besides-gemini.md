---
id: f442efe5b4
question: Which AI providers does Kestra support besides Gemini? Can I use Groq, Ollama, or a local model?
sort_order: 6
---

Kestra's AI plugin is provider-agnostic: it supports OpenAI, Gemini, Anthropic, xAI, Grok, and any OpenAI-compatible provider, including local models served through Ollama or LM Studio. You swap the provider block in a flow without changing anything else. See the [full list of supported providers](https://kestra.io/plugins/plugin-ai/provider).

The course uses Gemini because it has a generous free tier, but you are free to use any provider. The [awesome-llms list](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/awesome-llms.md) in the course repo tracks free and free-tier options; Groq is a popular choice because it is OpenAI-compatible and works with both the chat completions and responses APIs.

There are two ways to use AI in Kestra:

- The **AI plugin** (`io.kestra.plugin.ai`) is the generic one. It is the most flexible for switching providers, though new vendor-specific API features take a bit longer to land here.
- The **provider-specific plugins** (e.g. `plugin-gemini`, `plugin-openai`) expose features unique to that vendor, such as Gemini video generation, before they reach the generic AI plugin.

For OpenAI-compatible providers that don't have their own plugin (DeepSeek, Groq, xAI), point the OpenAI plugin at the provider's base URL instead of the default endpoint.
