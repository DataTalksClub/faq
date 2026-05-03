---
id: cbeb6f678b
question: How do I add the dlt MCP server in VS Code?
sort_order: 14
---

- Open the command palette in VS Code:
  - Windows: `Ctrl + Shift + P`
  - Mac: `Cmd + Shift + P`
- Run MCP: Add Server...
- Select "Command (stdio)"
- Type `uv run --with dlt[duckdb] --with dlt-mcp[search] python -m dlt_mcp` and press Enter.
- Set the id to `dlt` and press Enter
- Set the configuration target:
  - `Remote` if you are using GitHub Codespaces
  - `Workspace` otherwise

To verify that the MCP was added correctly:

- Open the command palette
- Type "MCP: List Servers"
- You should see "dlt Running" (like in the attached screenshot)
- If it is stopped, you can either:
  - Start it by selecting it and choosing "Start Server"
  - Prompt Copilot to use the mcp server (e.g. "list the dlt pipelines")

Lastly, make sure that when you initialize your dlt project (when you run `dlt init dlthub:taxi_pipeline duckdb`) you choose copilot as your agent.