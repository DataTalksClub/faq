---
id: 9e7b3f0c25
question: 'Agents: "AttributeError: ''str'' object has no attribute ''output''" when
  using OpenAI''s Responses API on a non-OpenAI model'
sort_order: 7
---

The new OpenAI Responses API (`client.responses.create(...)`, accessed via `response.output`) is OpenAI-specific. Other providers (Mistral, Groq, Gemini, etc.) don't implement it.

For non-OpenAI providers, use the chat-completions API and read `response.choices[0].message.content`:

```python
response = client.chat.completions.create(
    model="<provider-model>",
    messages=[{"role": "user", "content": prompt}],
    tools=tools_schema,  # may need adapting per provider
)
return response.choices[0].message.content
```

You'll also have to adapt the tools schema to whatever shape your provider expects.
