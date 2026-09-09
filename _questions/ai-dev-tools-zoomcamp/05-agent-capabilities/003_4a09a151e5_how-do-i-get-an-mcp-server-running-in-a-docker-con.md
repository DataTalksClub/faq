---
id: 4a09a151e5
question: 'How do I get an MCP server running in a Docker container to work with Antigravity?'
sort_order: 3
---

Antigravity's MCP config lives at `~/.gemini/antigravity/mcp_config.json`. Either open the container as a dev-container, or put a `docker run ...` command in the MCP config. If you use stdio, make sure your launcher (e.g. a `.bat` file) passes input on stdin and writes to stdout. Many people find it easier to run inside a WSL VM and use "Connect to WSL" remote development in VS Code/Antigravity.
