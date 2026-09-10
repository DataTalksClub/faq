---
id: 54b98d3581
question: 'How do I use Groq instead of OpenAI in the dlt workshop?'
sort_order: 16
---

In the dlt workshop's `homework/agent.py`, change the PydanticAI model string from the `openai:` provider to the `groq:` provider (no OpenAI key needed):

```python
faq_agent = Agent(
    "groq:openai/gpt-oss-120b",
    deps_type=SearchDeps,
    instructions=INSTRUCTIONS,
)
```

Set the corresponding key in `.env`:

```dotenv
GROQ_API_KEY=your-groq-api-key
```

The `SearchDeps`, instructions, and `@faq_agent.tool` code do not need to change. Use a model ID currently available from Groq — `llama-3.3-70b-versatile` was retired in August 2026, so don't copy it from older examples.
