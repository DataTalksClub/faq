---
course: mlops-zoomcamp
id: 02ff7e82ce
question: Pytest error ‘module not found’ when using pre-commit hooks if using custom
  packages in the source code
section: 'Module 6: Best practices'
sort_order: 2310
---

Problem description

Project structure:

/sources/production/model_service.py

/sources/tests/unit_tests/test_model_service.py (“from production.model_service import ModelService)

git commit -t ‘test’ raises ‘No module named ‘production’’ when calling pytest hook

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

Solution description

Use this hook instead:

- repo: local

hooks:

- id: pytest-check

name: pytest-check

entry: "./sources/tests/unit_tests/run.sh"

language: system

types: [python]

pass_filenames: false

always_run: true

And make sure that run.sh sets the right directory and run pytest:

cd "$(dirname "$0")"

cd ../..

export PYTHONPATH=.

pipenv run pytest ./tests/unit_tests

Added by MarcosMJD

