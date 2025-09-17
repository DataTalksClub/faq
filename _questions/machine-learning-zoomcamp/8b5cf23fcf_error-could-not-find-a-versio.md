---
course: machine-learning-zoomcamp
id: 8b5cf23fcf
question: 'Error: Could not find a version that satisfies the requirement tflite_runtime
  (from versions:none)'
section: 9. Serverless Deep Learning
sort_order: 3230
---

Problem: When trying to install tflite_runtime with

!pip install --extra-index-url tflite_runtime

one gets an error message above.

Solution:

fflite_runtime is only available for the os-python version combinations that can be found here:

your combination must be missing here

you can see if any of these work for you

and install the needed one using pip

eg

pip install

as it is done in the lectures code:

Alternatively, use a virtual machine (with VM VirtualBox, for example) with a Linux system. The other way is to run a code at a virtual machine within cloud service, for example you can use Vertex AI Workbench at GCP (notebooks and terminals are provided there, so all tasks may be performed).

Added by Alena Kniazeva, modified by Alex Litvinov

