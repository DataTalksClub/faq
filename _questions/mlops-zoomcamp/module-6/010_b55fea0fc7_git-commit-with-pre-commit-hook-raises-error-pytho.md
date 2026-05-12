---
id: b55fea0fc7
question: 'Git: Commit with pre-commit hook raises error ‘''PythonInfo'' object has
  no attribute ''version_nodot'''
sort_order: 10
---

When attempting to commit in Git, the following error occurs:

```bash
git commit -m 'Updated xxxxxx'

[INFO] Initializing environment for GitHub.
[INFO] Installing environment for GitHub.
[INFO] Once installed this environment will be reused.

An unexpected error has occurred: CalledProcessError: command:
…
return code: 1
expected return code: 0
stdout:
AttributeError: 'PythonInfo' object has no attribute 'version_nodot'
```

To resolve this issue, clear the app-data of the virtual environment using the following command:

```bash
python -m virtualenv api -vvv --reset-app-data
```
