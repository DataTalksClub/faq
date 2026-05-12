---
id: 02ff7e82ce
question: Pytest error ‘module not found’ when using pre-commit hooks if using custom
  packages in the source code
sort_order: 12
---

Project structure:

```
/sources/production/model_service.py
/sources/tests/unit_tests/test_model_service.py 
```

In `test_model_service.py`:

```python
from production.model_service import ModelService
```

A `git commit -t ‘test’` raises `No module named ‘production’` when calling the pytest hook:

```yaml
- repo: local

  hooks:
    - id: pytest-check
      name: pytest-check
      entry: pytest
      language: system
      pass_filenames: false
      always_run: true
      args: [
        "tests/"
      ]
```

Use this hook instead:

```yaml
- repo: local

  hooks:
    - id: pytest-check
      name: pytest-check
      entry: "./sources/tests/unit_tests/run.sh"
      language: system
      types: [python]
      pass_filenames: false
      always_run: true
```

Ensure that `run.sh` sets the correct directory and runs pytest:

```bash
cd "$(dirname "$0")"

cd ../..

export PYTHONPATH=.

pipenv run pytest ./tests/unit_tests
```