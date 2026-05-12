---
id: 1a166fc048
question: Error invoking API Gateway deploy API locally
sort_order: 17
---

When attempting to test the API gateway in [9.7 - API Gateway: Exposing the Lambda Function](https://www.youtube.com/watch?v=wyZ9aqQOXvs&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR), running the command:

```bash
python test.py
```

You might encounter the following error message:

```python
{'message': 'Missing Authentication Token'}
```


You need to ensure you have the correct deployed API URL for the specific path you are invoking. An example of a correct URL format is:

```
https://<random_string>.execute-api.us-east-2.amazonaws.com/test/predict
```