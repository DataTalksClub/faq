---
id: c6ff9083c0
question: How can I configure Kestra to use a different LLM provider instead of Google
  Gemini?
sort_order: 30
---

Kestra supports multiple LLM providers via its AI Provider plugins, not just Google Gemini. To configure a different provider:

- Pick a provider from the supported list (including Google Gemini, OpenAI, Anthropic, OpenRouter, DeepSeek, Ollama, Hugging Face, Mistral AI, Azure OpenAI, Amazon Bedrock, GitHub Models, Google Vertex AI, LocalAI, IBM watsonx.ai, Cloudflare Workers AI, DashScope, OCI Generative AI, ZhiPu AI).
- Create or obtain the required credentials (API key, endpoint, or other secrets) for the chosen provider and store them as Kestra secrets or environment variables per your workflow.
- Update the Kestra flow or configuration to use the selected provider instead of GoogleGemini. In practice:
  - For hosted providers with an OpenAI-compatible endpoint (OpenAI, OpenRouter, DeepSeek, Gemini, Mistral, and others), you typically change:
    - base_url (to point to the provider's API endpoint)
    - the API key
    - the model name
    - and any provider-specific field names as documented.
  - For open models or local options (Hugging Face hosted models, Ollama, LocalAI, LM Studio, etc.), configure the provider to point to the local or hosted endpoint and ensure the model/container is accessible.
  - For example, to use OpenRouter, configure the OpenRouter provider and supply your OpenRouter API key.
  - If you want to run models on your own machine, you can use Ollama (or vLLM, etc.) by pointing Kestra to your local endpoint.
  - If you need private networking (VPN) to reach a provider, set up the networking accordingly.

- Important: The code in many courses uses an OpenAI-compatible client, so you usually only need to adjust base_url, API key, and model name. Some providers may require different fields; consult the provider's Kestra plugin docs for the exact configuration.

- For the latest configuration examples for each provider, refer to the Kestra AI Provider documentation: https://kestra.io/plugins/plugin-ai/provider

Current supported providers include:
- Google Gemini
- OpenAI
- Anthropic
- OpenRouter
- DeepSeek
- Ollama
- Hugging Face
- Mistral AI
- Azure OpenAI
- Amazon Bedrock
- GitHub Models
- Google Vertex AI
- LocalAI
- IBM watsonx.ai
- Cloudflare Workers AI
- DashScope
- OCI Generative AI
- ZhiPu AI