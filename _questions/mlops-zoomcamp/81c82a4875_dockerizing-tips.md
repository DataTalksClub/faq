---
course: mlops-zoomcamp
id: 81c82a4875
question: Dockerizing tips
section: 'Module 4: Deployment'
sort_order: 1670
---

Ensure the correct image is being used to derive from.

Copy the data from local to the docker image using the COPY command to a relative path. Using absolute paths within the image might be troublesome.

Use paths starting from /app and don’t forget to do WORKDIR /app before actually performing the code execution.

Most common commands

Build container using docker build -t mlops-learn .

Execute the script using docker run -it --rm mlops-learn

<mlops-learn> is just a name used for the image and does not have any significance.

