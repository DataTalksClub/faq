---
id: fe5fb33959
question: 'ModuleNotFoundError: No module named ''numpy._core'' when running gunicorn / waitress'
sort_order: 65
---

This is a numpy/sklearn version mismatch between the env that pickled the model and the env that's loading it. Common fix:

- Match versions. If the model was trained with numpy 2.x, install numpy 2.x in the deployment env:
  ```bash
  pipenv install "numpy>=2.0"
  # or
  uv add "numpy>=2.0"
  ```
- Or downgrade to a known-good combination (e.g., `numpy==1.24.3`) and re-pickle the model.

If you're using Docker, the same versions need to be in the image. With `pipenv install --system --deploy` inside Docker, the lockfile is the source of truth — pin versions there.
