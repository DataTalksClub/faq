---
id: 320a5c1b9a
question: Object of type float32 is not JSON serializable
sort_order: 11
---

While passing local testing of the lambda function without issues, trying to test the same input with a running Docker instance results in an error message like:

```bash
{
  'errorMessage': 'Unable to marshal response: Object of type float32 is not JSON serializable',
  'errorType': 'Runtime.MarshalError',
  'requestId': 'f155492c-9af2-4d04-b5a4-639548b7c7ac',
  'stackTrace': []
}
```

This occurs when a model returns estimation values as NumPy `float32` values. These need to be converted to base-Python floats to become serializable.

In the following example, the dino vs dragon model returns a label and predicted probability for each class. Below is an excerpt of the `predict()` function in `lambda_function.py`:

```python
preds = [interpreter.get_tensor(output_index)[0][0], \
         1-interpreter.get_tensor(output_index)[0][0]]
```

To fix the serialization issue, convert the values to floats:

```python
preds = [float(interpreter.get_tensor(output_index)[0][0]), \
         float(1-interpreter.get_tensor(output_index)[0][0])]
```

You can resolve the rest by following the instructions in Chapter 9 (and/or Chapter 5) lecture videos.