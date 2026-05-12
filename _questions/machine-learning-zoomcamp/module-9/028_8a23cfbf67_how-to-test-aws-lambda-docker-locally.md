---
id: 8a23cfbf67
question: How to test AWS Lambda + Docker locally?
sort_order: 28
---

This deployment setup can be tested locally using [AWS RIE](https://github.com/aws/aws-lambda-runtime-interface-emulator/#test-an-image-with-rie-included-in-the-image) (Runtime Interface Emulator).

If your Docker image is built upon the base AWS Lambda image (e.g., `FROM public.ecr.aws/lambda/python:3.10`), use specific ports for `docker run` and a specific localhost link for testing:

```bash
docker run -it --rm -p 9000:8080 name
```

This command runs the image as a container and starts an endpoint locally at:

`localhost:9000/2015-03-31/functions/function/invocations`

Post an event to the following endpoint using a curl command:

```bash
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```

Examples of Curl Testing:

- **Windows Testing:**
  
  ```bash
  curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d "{\"url\": \"https://habrastorage.org/webt/rt/d9/dh/rtd9dhsmhwrdezeldzoqgijdg8a.jpeg\"}"
  ```

- **Unix Testing:**
  
  ```bash
  curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"url": "https://habrastorage.org/webt/rt/d9/dh/rtd9dhsmhwrdezeldzoqgijdg8a.jpeg"}'
  ```

If during testing you encounter an error like this:

```json
{
  "errorMessage": "Unable to marshal response: Object of type float32 is not JSON serializable",
  "errorType": "Runtime.MarshalError",
  "requestId": "7ea5d17a-e0a2-48d5-b747-a16fc530ed10",
  "stackTrace": []
}
```

just convert your response in `lambda_handler()` to a string using `str(result)`.