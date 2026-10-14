---
id: d63e563e6d
question: "On Windows, why can't my headless Claude Code agent run uv, docker compose, or curl even though they're in --allowedTools?"
sort_order: 5
---

On Windows, Claude Code usually runs shell commands through its **PowerShell** tool instead of Bash. `Bash(...)` rules in `--allowedTools` only apply to the Bash tool. In headless mode (`claude -p`) nobody can approve the PowerShell commands, so they're denied. File reads and edits still work, which is why the agent can change the code but can't run tests or rebuild.

Allow the same commands for PowerShell too:

```text
--allowedTools "Read Edit Write Bash(uv *) Bash(docker compose *) PowerShell(uv *) PowerShell(docker compose *) PowerShell(curl.exe *)"
```

Alternatively, if Git Bash is installed, turn the PowerShell tool off with `CLAUDE_CODE_USE_POWERSHELL_TOOL=0` so commands go through Bash.

Tips:

- In PowerShell, use `curl.exe`. Plain `curl` is an alias for `Invoke-WebRequest` in Windows PowerShell 5.1.
- Keep the allowlist narrow: don't allow `git push` or delete commands. A broad rule like `uv *` also allows `uv run python -c ...`.
- Test the permissions first with a throwaway `claude -p` run that only runs `docker compose ps` and your test command.

See [Claude Code: PowerShell tool](https://code.claude.com/docs/en/tools-reference#powershell-tool).
