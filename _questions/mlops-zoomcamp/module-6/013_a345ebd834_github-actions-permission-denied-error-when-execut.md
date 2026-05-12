---
id: a345ebd834
question: 'Github actions: Permission denied error when executing script file'
sort_order: 13
---

This issue occurs when running the following step in the CI YAML file definition:

```yaml
yml
- name: Run Unit Tests
  working-directory: "sources"
  run: ./tests/unit_tests/run.sh
```

When executing the GitHub CI action, the following error occurs:

```
…/tests/unit_test/run.sh Permission error

Error: Process completed with error code 126
```

To resolve this issue, add execution permission to the script and commit the changes:

```bash
git update-index --chmod=+x ./sources/tests/unit_tests/run.sh
```