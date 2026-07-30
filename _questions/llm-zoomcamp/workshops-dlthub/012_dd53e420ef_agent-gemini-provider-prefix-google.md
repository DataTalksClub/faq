---
id: dd53e420ef
question: What needs to change in `agent.py` to use Gemini instead of OpenAI?
sort_order: 12
---

In the dlt workshop's `homework/agent.py`, change the PydanticAI model string
from the `openai:` provider to the `google:` provider:

For example:

```python
faq_agent = Agent(
    "google:gemini-3.1-flash-lite",
    deps_type=SearchDeps,
    instructions=INSTRUCTIONS,
)
```

Set the corresponding key in `.env`:

```dotenv
GOOGLE_API_KEY=your-gemini-api-key
```

The `SearchDeps`, instructions, and `@faq_agent.tool` code do not need to
change.
