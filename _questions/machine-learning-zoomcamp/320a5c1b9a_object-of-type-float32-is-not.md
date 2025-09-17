---
id: 320a5c1b9a
question: Object of type float32 is not JSON serializable
section: 9. Serverless Deep Learning
course: machine-learning-zoomcamp
sort_order: 3160
---

Problem:

While passing local testing of the lambda function without issues, trying to test the same input with a running docker instance results in an error message like

{‘errorMessage’: ‘Unable to marshal response: Object of type float32 is not JSON serializable’, ‘errorType’: ‘Runtime.MarshalError’, ‘requestId’: ‘f155492c-9af2-4d04-b5a4-639548b7c7ac’, ‘stackTrace’: []}

This happens when a model (in this case the dino vs dragon model) returns individual estimation values as numpy float32 values (arrays). They need to be converted individually to base-Python floats in order to become “serializable”.

Solution:

In my particular case, I set up the dino vs dragon model in such a way as to return a label + predicted probability for each class as follows (below is a two-line extract of function predict() in the lambda_function.py):

preds = [interpreter.get_tensor(output_index)[0][0], \

1-interpreter.get_tensor(output_index)[0][0]]

In which case the above described solution will look like this:

preds = [float(interpreter.get_tensor(output_index)[0][0]), \

float(1-interpreter.get_tensor(output_index)[0][0])]

The rest can be made work by following the chapter 9 (and/or chapter 5!) lecture videos step by step.

Added by Konrad Muehlberg

