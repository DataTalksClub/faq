---
id: b396205ad7
question: Error “[Errno 13] Permission denied: '/home/ubuntu/.aws/credentials’” when running any aws command
section: Module 6: Best practices
course: mlops-zoomcamp
sort_order: 2380
---

After installing awscliv2 in linux you can get this error every time you try to run an aws command that needs to use the credentials. For example, if you run aws configure, you can insert the key and secret but finally you receive the error message.

The user ubuntu does not have permission to read/write files in .aws folder and neither credentials and config files exists. What I have done to solve:

Go to .aws folder, usually /home/ubuntu/.aws

Create an empty credentials and config files:

touch credentials

touch config

Modify the permissions:

sudo chmod -R 777 credentials

sudo chmod -R 777 config

Now, you can run aws configure

Run aws configure, modify the keys and secret and save them to the credentials file. And then you can execute your aws commands from your python scripts or in the command line.

Added by Eduardo Muñoz

