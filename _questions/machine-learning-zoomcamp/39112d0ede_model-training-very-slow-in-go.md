---
id: 39112d0ede
question: Model training very slow in google colab with T4 GPU
section: 8. Neural Networks and Deep Learning
course: machine-learning-zoomcamp
sort_order: 3010
---

When training the models, in the fit function, you can specify the number of workers/threads.

The number of threads apparently also works for GPUs, and came very handy in google colab for the T4 GPU, since it was very very slow, and workers default value is 1.

I changed the workers variable to 2560, following this thread in stackoverflow. I am using the free T4 GPU.  ()

Added by Ibai Irastorza

