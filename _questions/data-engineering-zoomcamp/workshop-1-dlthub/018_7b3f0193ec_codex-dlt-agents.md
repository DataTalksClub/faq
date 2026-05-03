---
id: 7b3f0193ec
question: How do I generate the AGENTS.md file for Codex in dlt?
sort_order: 18
---

To generate the AGENTS.md file for Codex in dlt, follow these steps:

1. Open a terminal and run:

```bash
dlt ai setup codex
```

2. The command currently generates a file named `AGENT.md`. Since Codex looks for `AGENTS.md` (plural) by default, rename it:

```bash
mv AGENT.md AGENTS.md
```
