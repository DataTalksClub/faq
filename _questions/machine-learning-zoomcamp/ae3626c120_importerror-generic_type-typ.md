---
course: machine-learning-zoomcamp
id: ae3626c120
question: 'ImportError: generic_type: type "InterpreterWrapper" is already registered!'
section: 9. Serverless Deep Learning
sort_order: 3120
---

When I run   import tflite_runtime.interpreter as tflite , I get an error message says “ImportError: generic_type: type "InterpreterWrapper" is already registered!”

Solution description

This error occurs when you import both tensorflow  and tflite_runtime.interpreter  “import tensorflow as tf” and “import tflite_runtime.interpreter as tflite” in the same notebook.  To fix the issue, restart the kernel and import only tflite_runtime.interpreter " import tflite_runtime.interpreter as tflite".

Asia Saeed

