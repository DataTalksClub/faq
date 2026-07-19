---
id: dd53e420ef
question: What needs to change in `agent.py` to use Gemini instead of OpenAI?
sort_order: 32
---

To use Gemini with PydanticAI, update the provider prefix in your `Agent` setup from `openai:` to `google:`.

For example:

```python
faq_agent = Agent(
    "google:gemini-3.1-flash-lite",
    deps_type=SearchDeps,
    instructions=INSTRUCTIONS,
)
```

Also update your API key environment variable to the Gemini one the code expects (typically `GOOGLE_API_KEY`).