---
id: ac62d9ccf0
question: Getting a syntax error while trying to get the password from aws-cli
section: 9. Serverless Deep Learning
course: machine-learning-zoomcamp
sort_order: 3080
---

The command aws ecr get-login --no-include-email returns an invalid choice error:

The solution is to use the following command instead:  aws ecr get-login-password

Could simplify the login process with, just replace the <ACCOUNT_NUMBER> and <REGION> with your values:

export PASSWORD=`aws ecr get-login-password`

docker login -u AWS -p $PASSWORD <ACCOUNT_NUMBER>.dkr.ecr.<REGION>.amazonaws.com/clothing-tflite-images

Added by Martin Uribe

