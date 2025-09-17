---
course: machine-learning-zoomcamp
id: dc705a3c4e
question: Tflite_runtime unable to install
section: Miscellaneous
sort_order: 3960
---

I am getting this error message when I tried to install tflite in a pipenv environment

Error:  An error occurred while installing tflite_runtime!

Error text:

ERROR: Could not find a version that satisfies the requirement tflite_runtime (from versions: none)

ERROR: No matching distribution found for tflite_runtime

This version of tflite do not run on python 3.10, the way we can make it work is by install python 3.9, after that it would install the tflite_runtime without problem.

Pastor Soto

Check all available versions here:

If you don’t find a combination matching your setup, try out the options at

which you can install as shown in the lecture, e.g.

pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.7.0-cp38-cp38-linux_x86_64.whl

Finally, if nothing works, use the TFLite included in TensorFlow for local development, and use Docker for testing Lambda.

Rileen Sinha (based on discussions on Slack)

