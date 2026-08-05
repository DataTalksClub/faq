---
id: 8ecd1e8262
question: How do I adapt the handwritten agent loop in Module 1 Lesson 14 for a non-OpenAI
  provider using Chat Completions tool calling?
sort_order: 14
---

If your provider exposes an OpenAI-compatible `chat.completions.create(...)` endpoint with tool calling, you can adapt the Lesson 14 handwritten agent loop by switching from the Responses API to Chat Completions and by reading tool calls from the assistant message.

Key differences from the Responses-based loop:

- Use `client.chat.completions.create(model=..., messages=..., tools=...)` instead of `client.responses.create(..., input=...)`.
- Get tool calls from `response.choices[0].message.tool_calls` (not from `response.output`).
- Append the full assistant message (including its requested tool calls) to `messages` before adding tool results.
- For each tool call, add a `role="tool"` message with the matching `tool_call_id` and the tool result as `content`.
- Keep looping until the returned assistant message has no `tool_calls`.

You can use code like this after you define your `search` function and `search_tool` schema:

```python
import json


def make_tool_result(call, tool_handlers):
    """Run one tool call and format its result for Chat Completions."""
    tool_name = call.function.name
    tool_args = json.loads(call.function.arguments)

    if tool_name not in tool_handlers:
        result = {"error": f"Unknown tool requested: {tool_name}"}
    else:
        result = tool_handlers[tool_name](**tool_args)

    return {
        "role": "tool",
        "tool_call_id": call.id,
        "content": json.dumps(result, indent=2),
    }


def agent_loop(
    client,
    model,
    instructions,
    question,
    tools,
    tool_handlers,
    max_iterations=5,
):
    messages = [
        {"role": "developer", "content": instructions},
        {"role": "user", "content": question},
    ]

    for iteration in range(1, max_iterations + 1):
        print(f"Iteration {iteration}...")

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools,
        )

        message = response.choices.message

        # Preserve the assistant message, including its tool calls.
        messages.append(message)

        tool_calls = getattr(message, "tool_calls", None) or []

        # No tool calls means the model has returned its final answer.
        if not tool_calls:
            answer = message.content or ""
            print("\nASSISTANT:\n")
            print(answer)
            return answer

        # A model can request more than one tool in one response.
        for call in tool_calls:
            print("Function call:", call.function.name, call.function.arguments)
            tool_result = make_tool_result(call, tool_handlers)
            messages.append(tool_result)

    raise RuntimeError(f"Agent exceeded the maximum of {max_iterations} iterations.")
```

Example usage (using the Lesson 14 FAQ search tool):

```python
answer = agent_loop(
    client=openai_client,
    model=MODEL_ID,
    instructions=instructions,
    question="How do I run Ollama locally?",
    tools=[search_tool],
    tool_handlers={"search": search},
)
```

This pattern applies only if your provider supports the OpenAI-compatible Chat Completions tool-calling format. If the provider’s `tools` schema or response fields differ, you’ll need to adjust accordingly.