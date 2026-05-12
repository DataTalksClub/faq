---
id: 3b78e09b80
question: 'Which tool should I use for Python environments?'
sort_order: 42
---

We recommend [uv](https://docs.astral.sh/uv/) for both installing Python and managing project virtual environments. It's fast, has no licensing concerns, and produces clean reproducible builds.

```bash
# Install uv (one-line installer; see https://docs.astral.sh/uv/ for your OS):
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install a Python version:
uv python install 3.11

# Create and activate a project venv:
uv venv --python 3.11
source .venv/bin/activate    # Linux / macOS
.venv\Scripts\activate       # Windows

# Add packages:
uv add pandas scikit-learn jupyter
```

Module 5 includes a uv + FastAPI workshop that walks through this setup end-to-end.
