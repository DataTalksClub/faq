---
id: 80a2e18431
question: 'docker: Error response from daemon: failed to create task for container:
  failed to create shim task: OCI runtime create failed: runc create failed: unable
  to start container process: exec: "gunicorn": executable file not found in $PATH:
  unknown.'
sort_order: 60
---

This error indicates that the executable `gunicorn` is not found in the container's `$PATH`. To resolve this, you need to add `gunicorn` and `flask` to your `Pipfile`.

Update your `Pipfile` as follows:

```plaintext
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
scikit-learn = "==1.5.2"
gunicorn = "*"
flask = "*"

[dev-packages]

[requires]
python_version = "3.11"
```

After making these changes, follow these steps:

1. Run `pipenv lock` to update the `Pipfile.lock`.
2. Build the Docker image with:
   ```bash
   docker build -t [name] .
   ```
3. Run the Docker container with:
   ```bash
   docker run [name]
   ```