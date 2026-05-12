---
id: 0cfb31c221
question: Pytest error 'module not found' when using custom packages in the source
  code
sort_order: 11
---

Project structure:

```
/sources/production/model_service.py
/sources/tests/unit_tests/test_model_service.py
```

The test file contains:

```python
from production.model_service import ModelService
```

- Running `python test_model_service.py` from the `sources` directory works.
- Running `pytest ./test/unit_tests` fails with: `No module named 'production'`.

- Use the following command:
  
  ```bash
  python -m pytest ./test/unit_tests
  ```

- `pytest` does not automatically add to the `sys.path` the path where it is run.
- Alternatives include:
  - Running `python -m pytest`
  - Exporting the `PYTHONPATH` before executing `pytest`:
    
    ```bash
    export PYTHONPATH=.
    ```