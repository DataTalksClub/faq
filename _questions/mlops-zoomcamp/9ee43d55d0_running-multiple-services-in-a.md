---
id: 9ee43d55d0
question: Running multiple services in a Docker container
section: Module 4: Deployment
course: mlops-zoomcamp
sort_order: 1680
---

If you are trying to run Flask gunicorn & MLFlow server from the same container, defining both in Dockerfile with CMD will only run MLFlow & not Flask.

Solution: Create separate shell script with server run commands, for eg:

> 	script1.sh

#!/bin/bash

gunicorn --bind=0.0.0.0:9696 predict:app

Another script with e.g. MLFlow server:

>	script2.sh

#!/bin/bash

mlflow server -h 0.0.0.0 -p 5000 --backend-store-uri=sqlite:///mlflow.db --default-artifact-root=g3://zc-bucket/mlruns/

Create a wrapper script to run above 2 scripts:

>	wrapper_script.sh

#!/bin/bash

# Start the first process

./script1.sh &

# Start the second process

./script2.sh &

# Wait for any process to exit

wait -n

# Exit with status of process that exited first

exit $?

Give executable permissions to all scripts:

chmod +x *.sh

Now we can define last line of Dockerfile as:

> 	Dockerfile

CMD ./wrapper_script.sh

Dont forget to expose all ports defined by services!

