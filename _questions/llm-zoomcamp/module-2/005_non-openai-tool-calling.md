---
id: 2a8f6c4d91
question: 'Agents: which non-OpenAI models support tool / function calling?'
sort_order: 5
---

Confirmed working alternatives for tool calling in this course:

- [Groq](https://console.groq.com/docs/tool-use) — `llama-3.3-70b-versatile`, DeepSeek R1, Llama 4. Free tier, OpenAI-compatible API.
- [Mistral](https://docs.mistral.ai/capabilities/function_calling/) — most models. Schema differs slightly from OpenAI.
- [Google Gemini](https://ai.google.dev/gemini-api/docs/function-calling) — `gemini-2.5-flash` etc., free tier. Available either through Google's GenAI SDK or via the [OpenAI-compatible endpoint](https://ai.google.dev/gemini-api/docs/openai).
- [Ollama](https://ollama.com/blog/tool-support) — `llama3.1` and similar, local. Use `ollama.chat(..., tools=[...])`.

You'll typically need to adapt the homework's `chat_assistant.py` / `mcp_client.py` slightly when not using OpenAI — the tool schema and the response shape differ between providers.
