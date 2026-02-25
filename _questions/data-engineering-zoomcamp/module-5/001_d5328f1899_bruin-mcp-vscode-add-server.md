---
id: d5328f1899
question: How do I add the Bruin MCP server to VS Code?
sort_order: 1
---

1. Open the command palette in your IDE and search for "MCP: Add Server..." 
2. Choose "Command (stdio)" 
3. Enter the command: `bruin mcp` 
4. Name the server "bruin" 
5. Choose how to add it:
   - Globally: If you are doing local development
   - Remotely/Workspace: If you are doing development in GitHub Codespaces
6. You should now see "bruin" listed when you use the "MCP: List Servers" command in VS Code.