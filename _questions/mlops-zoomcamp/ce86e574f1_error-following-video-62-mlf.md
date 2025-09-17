---
course: mlops-zoomcamp
id: ce86e574f1
question: 'Error following video 6.2: mlflow=1.27.0'
section: 'Module 6: Best practices'
sort_order: 2210
---

When following the video instructions and running the Dockerfile I get an error that the Dockerfile build failed in line 8, because there is no matching distribution for mlflow=1.27.0. Below is the code output:

4.900 ERROR: No matching distribution found for mlflow==1.27.0

4.901 ERROR: Couldn't install package: {}

4.901  Package installation failed...

------

Dockerfile:8

--------------------

6 |     COPY [ "Pipfile", "Pipfile.lock", "./" ]

7 |

8 | >>> RUN pipenv install --system --deploy

9 |

10 |     COPY [ "lambda_function.py", "model.py", "./" ]

--------------------

ERROR: failed to solve: process "/bin/sh -c pipenv install --system --deploy" did not complete successfully: exit code: 1

