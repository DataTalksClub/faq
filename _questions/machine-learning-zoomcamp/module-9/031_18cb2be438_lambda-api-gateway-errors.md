---
id: 18cb2be438
question: 'Lambda API Gateway errors:'
sort_order: 31
---

```plaintext
Authorization header requires 'Credential' parameter. Authorization header requires 'Signature' parameter. Authorization header requires 'SignedHeaders' parameter. Authorization header requires existence of either a 'X-Amz-Date' or a 'Date' header.

Missing Authentication Token
```

To test invoke a method using Boto3, you can use the following Python script:

```python
import boto3

client = boto3.client('apigateway')

response = client.test_invoke_method(
    restApiId='your_rest_api_id',
    resourceId='your_resource_id',
    httpMethod='POST',
    pathWithQueryString='/test/predict', # Adjust path as per API setup
    body='{"url": "https://habrastorage.org/webt/rt/d9/dh/rtd9dhsmhwrdezeldzoqgijdg8a.jpeg"}')

print(response['body'])
```
