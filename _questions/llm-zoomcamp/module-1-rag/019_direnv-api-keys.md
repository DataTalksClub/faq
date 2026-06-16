---
id: 8b2f5e9d04
question: 'API keys: how do I set them once and not re-export every terminal?'
sort_order: 19
---

Use [`dirdotenv`](https://github.com/alexeygrigorev/dirdotenv). It is like `direnv`, but works with both `.env` and `.envrc`, and is more portable across shells and operating systems.

```bash
uv tool install dirdotenv

# add this line to your ~/.bashrc or ~/.zshrc:
eval "$(dirdotenv hook bash)"   # or zsh

# inside your project:
echo 'OPENAI_API_KEY=sk-...' > .env
echo '.env' >> .gitignore
```

After that, the key is loaded automatically when you `cd` into the project directory.

Important: always add `.env` and `.envrc` to `.gitignore` so keys never land on GitHub.

`direnv` is also fine if you already use it. In that case, create `.envrc`, add your exports there, and run `direnv allow`.

For GitHub Codespaces, use the built-in [Codespaces secrets](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces) instead of files in the repo.

For Python scripts, the equivalent is `python-dotenv`:

```python
from dotenv import load_dotenv
load_dotenv()  # loads .env from project root
```
