---
id: ba23a5c708
question: "Pre-commit fails with 'RuntimeError: The Poetry configuration is invalid'"
sort_order: 22
---

If pre-commit fails with something like:

```
RuntimeError: The Poetry configuration is invalid:
  - data.extras.pipfile_deprecated_finder[2] must match pattern ^[a-zA-Z-_.0-9]+$
```

This is caused by a version mismatch between the version of the tool pinned in `pre-commit-config.yaml` and the version installed via `Pipfile.lock`. Check the versions in `Pipfile.lock` and update `pre-commit-config.yaml` to match (or vice versa).
