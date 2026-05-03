---
id: e5d8a2c761
question: 'Project: what does "reproducibility" mean — do reviewers need access to
  my API keys?'
sort_order: 11
---

Never share API keys or hosted-service credentials in your repo. Reproducibility means a peer reviewer can clone the repo and follow your README to recreate the system from scratch — using their own credentials.

Concretely:

- Provide a script (or notebook) that ingests the dataset and (re)builds the search index locally.
- Ship a `.env.example` with the variable names but no values; have the reviewer create their own `.env` with their own keys. Keep `.env` in `.gitignore`.
- Use a cheap model (`gpt-4o-mini`, Groq, etc.) so reviewers don't burn through credits when running your project.
- Pin dependency versions (`requirements.txt` / `pyproject.toml` lock file) and document the Python version (and Docker version, if used).
