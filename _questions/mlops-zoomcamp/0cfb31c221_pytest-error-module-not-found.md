---
course: mlops-zoomcamp
id: 0cfb31c221
question: Pytest error ‘module not found’ when if using custom packages in the source
  code
section: 'Module 6: Best practices'
sort_order: 2300
---

Problem description

Project structure:

/sources/production/model_service.py

/sources/tests/unit_tests/test_model_service.py (“from production.model_service import ModelService)

When running python test_model_service.py from the sources directory, it works.

When running pytest ./test/unit_tests fails. ‘No module named ‘production’’

Solution description

Use python -m pytest ./test/unit_tests

Explanation: pytest does not add to the sys.path the path where pytest is run.

You can run python -m pytest, or alternatively export PYTHONPATH=. Before executing pytest

Added by MarcosMJD

