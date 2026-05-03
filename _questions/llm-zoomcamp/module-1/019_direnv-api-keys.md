---
id: 8b2f5e9d04
question: 'API keys: how do I set them once and not re-export every terminal?'
sort_order: 19
---

Use [`direnv`](https://direnv.net/) to scope env vars to a project directory. It loads them automatically when you `cd` in:

```bash
# install direnv (Linux: apt/brew; macOS: brew install direnv)
# add this line to your ~/.bashrc or ~/.zshrc:
eval "$(direnv hook bash)"   # or zsh

# inside your project:
echo 'export OPENAI_API_KEY=sk-...' > .envrc
echo '.envrc' >> .gitignore
direnv allow
```

Important: always add `.envrc` (and `.env`) to `.gitignore` so the key never lands on GitHub.

For GitHub Codespaces, use the built-in [Codespaces secrets](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces) instead of files in the repo.

For Python scripts, the equivalent is `python-dotenv`:

```python
from dotenv import load_dotenv
load_dotenv()  # loads .env from project root
```
