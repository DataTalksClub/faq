---
course: mlops-zoomcamp
id: 186389973c
question: 'Connection in use: (''127.0.0.1'', 5000)'
section: 'Module 2: Experiment tracking'
sort_order: 810
---

You have something running on the 5000 port. You need to stop it.

Answer: On terminal in mac .

Run ps -A | grep gunicorn

Look for the number process id which is the 1st number after running the command

![Image](images/mlops-zoomcamp/image_ad7daf39.png)

kill 13580

where 13580  represents the process number.

Or by executing the following command it will kill all the processes using port 5000:

>> sudo fuser -k 5000/tcp

Answered by Vaibhav Khandelwal

Just execute in the command below in the command line to kill the running port

->> kill -9 $(ps -A | grep python | awk '{print $1}')

Answered by kamaldeen (kamaldeen32@gmail.com)

Change to different port (5001 in this case)

>> mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5001

Answered by krishna (nellaikrishna@gmail.com)

