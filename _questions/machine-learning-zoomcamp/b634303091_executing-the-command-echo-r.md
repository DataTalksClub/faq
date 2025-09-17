---
course: machine-learning-zoomcamp
id: b634303091
question: Executing the command echo ${REMOTE_URI} returns nothing.
section: 9. Serverless Deep Learning
sort_order: 3070
---

Solution description

In the unit 9.6, Alexey ran the command echo ${REMOTE_URI} which turned the URI address in the terminal. There workaround is to set a local variable (REMOTE_URI) and assign your URI address in the terminal and use it to login the registry, for instance, REMOTE_URI=2278222782.dkr.ecr.ap-south-1.amazonaws.com/clothing-tflite-images (fake address). One caveat is that you will lose this variable once the session is terminated.

I also had the same problem on Ubuntu terminal. I executed the following two commands:

$ export REMOTE_URI=1111111111.dkr.ecr.us-west-1.amazonaws.com/clothing-tflite-images:clothing-model-xception-v4-001

$ echo $REMOTE_URI

111111111.dkr.ecr.us-west-1.amazonaws.com/clothing-tflite-images:clothing-model-xception-v4-001

Note: 1. no curly brackets (e.g. echo ${REMOTE_URI}) needed unlike in video 9.6,

2. Replace REMOTE_URI with your URI

(Bhaskar Sarma)

