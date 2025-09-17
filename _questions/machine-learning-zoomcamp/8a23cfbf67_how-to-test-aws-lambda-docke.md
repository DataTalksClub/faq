---
course: machine-learning-zoomcamp
id: 8a23cfbf67
question: How to test AWS Lambda + Docker locally?
section: 9. Serverless Deep Learning
sort_order: 3330
---

This deployment setup can be tested locally using  (runtime interface emulator).

Basically, if your Docker image was built upon base AWS Lambda image (FROM public.ecr.aws/lambda/python:3.10) - just use certain ports for “docker run” and a certain “localhost link” for testing:

docker run -it --rm -p 9000:8080 name

This command runs the image as a container and starts up an endpoint locally at:

localhost:9000/2015-03-31/functions/function/invocations

Post an event to the following endpoint using a curl command:

curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'

Examples of curl testing:

* windows testing:

curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d "{\"url\": \"https://habrastorage.org/webt/rt/d9/dh/rtd9dhsmhwrdezeldzoqgijdg8a.jpeg\"}"

* unix testing:

curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"url": "https://habrastorage.org/webt/rt/d9/dh/rtd9dhsmhwrdezeldzoqgijdg8a.jpeg"}'

If during testing you encounter an error like this:

# {"errorMessage": "Unable to marshal response: Object of type float32 is not JSON serializable", "errorType": "Runtime.MarshalError", "requestId": "7ea5d17a-e0a2-48d5-b747-a16fc530ed10", "stackTrace": []}

just turn your response at lambda_handler() to string - str(result).

Added by Andrii Larkin

