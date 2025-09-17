---
id: 32c95df124
question: Error: failed to compute cache key: "/model2.bin" not found: not found
section: 5. Deploying Machine Learning Models
course: machine-learning-zoomcamp
sort_order: 1960
---

Initially, I did not assume there was a model2. I copied the original model1.bin and dv.bin. Then when I tried to load using

COPY ["model2.bin", "dv.bin", "./"]

then I got the error above in MINGW64 (git bash) on Windows.

The temporary solution I found was to use

COPY ["*", "./"]

which I assume combines all the files from the original docker image and the files in your working directory.

Added by Muhammed Tan

