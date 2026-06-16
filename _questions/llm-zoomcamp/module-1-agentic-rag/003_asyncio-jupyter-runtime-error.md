---
id: 7c4e1a3b58
question: 'Agents: "RuntimeError: Already running asyncio in this thread" when calling
  asyncio.run() from Jupyter'
sort_order: 3
---

Jupyter already runs an event loop inside the kernel, so calling `asyncio.run(...)` blows up with:

```
RuntimeError: Already running asyncio in this thread
```

In a notebook cell, just `await` the coroutine directly — no wrapper needed:

```python
result = await main()
```

For the FastMCP server in the agents homework, use the async variant:

```python
await mcp.run_async()
```

Note: in the agents homework's "run the server" question, you're meant to start the MCP server from a terminal (`python weather_server.py`), not from inside the notebook.
