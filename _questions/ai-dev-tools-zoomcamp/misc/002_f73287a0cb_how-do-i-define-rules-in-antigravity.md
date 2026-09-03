---
id: f73287a0cb
question: 'How do I define rules in Antigravity?'
sort_order: 2
---

Rules in Google Antigravity are defined using Markdown files that outline standards, conventions, constraints, and checklists to guide your agents.

You can define rules at two main levels depending on your scope:

### Workspace Rules

Workspace-level rules are stored directly within your project directory and govern behavior for that specific codebase.

1. Create a folder named `.agents/rules` in your workspace or git root directory.
2. Add a new `.md` file inside this folder (for example, `coding-standards.md` or `testing-rules.md`).
3. Write your constraints, formatting preferences, or workflow requirements in plain Markdown. You can also specify activation parameters (such as manual triggers or automatic matching) at the top of the file.

### Global Customization Menu

If you want to add quick or global rules directly through the interface without manually creating directories:

1. Click the **three-dot icon** in the top right corner of the Agent chat window.
2. Select **Customizations**.
3. Click the **+** button to add and save your custom instructions or rule sets.
