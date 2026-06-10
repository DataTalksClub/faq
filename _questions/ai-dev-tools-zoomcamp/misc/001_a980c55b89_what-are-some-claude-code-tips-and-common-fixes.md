---
id: a980c55b89
question: 'What are some Claude Code tips and common fixes?'
sort_order: 1
---

Tips:

- Use `/compact` regularly to avoid losing context in long conversations.
- Use `/clear` to start fresh while keeping project context.
- Check conversation size with `/status`.
- Put project rules in a `CLAUDE.md` file at the repo root.
- Use the `--verbose` flag for debugging.

Common issues and fixes:

- "Command not found: claude" - Claude isn't in PATH. Use `npx @anthropic-ai/claude-code` or fix your PATH.
- Context loss / Claude becomes less capable - use `/compact` before the context gets too long.
- Claude ignores CLAUDE.md - check the file exists (`ls -la CLAUDE.md`) and that you're in the right directory.
- Claude writes failing tests - work TDD: have it write tests first, review them, then implement.
- Claude forgets how to compile - keep build commands in CLAUDE.md and remind it explicitly.
