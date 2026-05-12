---
id: 6aa17f1eab
question: Why do I need to provide a train.py file when I already have the notebook.ipynb
  file?
sort_order: 1
---

`train.py` lets your peer reviewers cross-check that your training process works on someone else's system without having to step through your notebook cell by cell. The reviewers should be able to clone your repo, install dependencies (`pipenv install` / `uv sync` / `pip install -r requirements.txt`), and run `python train.py` to reproduce your model.

Make sure your project's environment file (`Pipfile`, `pyproject.toml`, or `requirements.txt`) lists every dependency `train.py` needs.
