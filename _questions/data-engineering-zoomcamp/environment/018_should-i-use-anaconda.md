---
id: a1b2c3d4e5
question: Should I use Anaconda for this course?
sort_order: 18
---

No. The officially recommended way now is [`uv`](https://docs.astral.sh/uv/) for both installing Python and managing project dependencies.

Quick start:

```bash
# Install uv (one-line installer; see https://docs.astral.sh/uv/ for your OS):
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install a Python version:
uv python install 3.11

# Create a project venv:
uv venv --python 3.11
source .venv/bin/activate    # Linux / macOS
.venv\Scripts\activate       # Windows

# Add packages:
uv add pandas sqlalchemy "psycopg[binary]"
```

`uv` replaces the parts of Anaconda we previously used: Python version management, virtual environments, and dependency installation. It's faster, smaller, and has no licensing concerns.
