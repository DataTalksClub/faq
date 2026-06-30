---
id: 0224d980b3
question: 'toyaikit: how do I use it with a non-OpenAI provider (e.g. Groq 404 error)
  or with Anthropic instead of OpenAI?'
sort_order: 5
---

If you get a `404` (or similar) when using toyaikit with Groq or another non-OpenAI provider, it's because `OpenAIResponsesRunner` / `OpenAIClient` call OpenAI's Responses endpoint (`responses.create`), which only OpenAI implements. Switch to the **chat completions** classes, which use the standard `chat.completions.create` endpoint that Groq and other OpenAI-compatible providers support.

### OpenAI or Groq (chat completions)

```python
import os
from openai import OpenAI
from toyaikit.tools import Tools
from toyaikit.llm import OpenAIChatCompletionsClient
from toyaikit.chat.runners import OpenAIChatCompletionsRunner

tools = Tools()
tools.add_tools(my_tools_object)   # functions need type hints + an Args: docstring

# OpenAI:
llm_client = OpenAIChatCompletionsClient(model="gpt-4o-mini", client=OpenAI())

# Groq (same runner, just point the OpenAI client at Groq's base URL):
groq_client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)
llm_client = OpenAIChatCompletionsClient(model="llama-3.3-70b-versatile", client=groq_client)

runner = OpenAIChatCompletionsRunner(
    tools=tools,
    developer_prompt="You are a helpful assistant.",
    llm_client=llm_client,
)
result = runner.loop(prompt="What's the weather in Berlin?")
print(result.last_message)
```

### Anthropic

```python
from toyaikit.tools import Tools
from toyaikit.llm import AnthropicClient
from toyaikit.chat.runners import AnthropicMessagesRunner

tools = Tools()
tools.add_tools(my_tools_object)

# Reads ANTHROPIC_API_KEY from the environment automatically:
llm_client = AnthropicClient(model="claude-haiku-4-5")

runner = AnthropicMessagesRunner(
    tools=tools,
    developer_prompt="You are a helpful assistant.",
    llm_client=llm_client,
)
result = runner.loop(prompt="What's the weather in Berlin?")
print(result.last_message)
```

Notes:

- `runner.loop(prompt=...)` runs one turn programmatically and returns a result with `.last_message`, `.all_messages`, and `.tokens` — no chat interface needed. Use `runner.run()` only for the interactive Jupyter loop.
- Pass an explicit, current model id. For Anthropic, `claude-haiku-4-5` / `claude-sonnet-4-5` work; an outdated id can 404.
- For Groq you'll see a harmless `UnknownModelWarning: No pricing data...` — the call still succeeds, only cost calculation is skipped.
