---
id: 80a2e18431
question: docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: exec: "gunicorn": executable file not found in $PATH: unknown.
section: Miscellaneous
course: machine-learning-zoomcamp
sort_order: 4280
---

You need to add gunicorn and flask just to be safe to Pipfile with nano Pipfile.

add

[[source]]

url = "https://pypi.org/simple"

verify_ssl = true

name = "pypi"

[packages]

scikit-learn = "==1.5.2"

gunicorn = "*"

flask 	    = “*”

[dev-packages]

[requires]

python_version = "3.11"

After that run pipenv lock then do the docker build -t [name] .  and docker run [name]

(Added by Ico)

