---
course: mlops-zoomcamp
id: ff0f22df21
question: ‘Invalid base64’ error after running `aws kinesis put-record`
section: 'Module 4: Deployment'
sort_order: 1610
---

Problem description:  You might get an error ‘Invalid base64’ after running the ‘aws kinesis put-record’ command on your local machine. This might be the case if you are using the AWS CLI version 2 (note that in the video 4.4, around 57:42, you can see a warning since the instructor is using v1 of the CLI.

Solution description: To get around this, pass the argument ‘--cli-binary-format raw-in-base64-out’. This will encode your data string into base64 before passing it to kinesis

Added by M

