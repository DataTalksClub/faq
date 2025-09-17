---
course: mlops-zoomcamp
id: 884bb9afb7
question: Passing envs to my docker image
section: 'Module 4: Deployment'
sort_order: 1760
---

Problem description: I was having issues because my python script was not reading AWS credentials from env vars, after building the image I was running it like this:

docker run -it homework-04 -e AWS_ACCESS_KEY_ID=xxxxxxxx -e AWS_SECRET_ACCESS_KEY=xxxxxx

Solution 1:

Environment Variables: 
You can set the AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY and AWS_SESSION_TOKEN (if you are using AWS STS) environment variables. You can set these in your shell, or you can include them in your Docker run command like this:

I found out by myself that those variables must be passed before specifying the name of the image, as follow:

docker run -e AWS_ACCESS_KEY_ID=xxxxxxxx -e AWS_SECRET_ACCESS_KEY=xxxxxx -it homework-04

Solution 2:

If you want to pass an env file, you can also do so by adding, for an env file called .env:

docker run -it homework-04 --env-file .env

Solution 3 (if AWS credentials were not found):
AWS Configuration Files: 
The AWS SDKs and CLI will check the ~/.aws/credentials and ~/.aws/config files for credentials if they exist. You can map these files into your Docker container using volumes:

docker run -it --rm -v ~/.aws:/root/.aws homework:v1

Added by Erick Cal

Last edited by: Fustincho

