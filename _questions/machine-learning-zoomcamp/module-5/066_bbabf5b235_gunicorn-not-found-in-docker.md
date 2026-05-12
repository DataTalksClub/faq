---
id: bbabf5b235
question: 'Docker container fails: ''gunicorn: executable file not found in $PATH'''
sort_order: 66
---

`gunicorn` wasn't installed inside the image because it's not in the Pipfile/lockfile. Add it under `[packages]`:

```toml
[packages]
gunicorn = "*"
```

Then `pipenv lock` and rebuild. Same applies for `waitress` if you're on Windows.
