---
id: 39112d0ede
question: Model training very slow in google colab with T4 GPU
sort_order: 24
---

When training models in Google Colab, you can improve performance by specifying the number of workers/threads in the `fit` function.

Increasing the number of threads can also be beneficial for GPUs. This adjustment proved useful for the T4 GPU in Google Colab, as the default value for workers is 1, which can result in very slow processing.

To improve performance:

- Change the `workers` variable to a higher value, such as 2560, to accelerate model training.

For further information, consult this [Stack Overflow thread](https://stackoverflow.com/questions/68208398/how-to-find-the-number-of-cores-in-google-colabs-gpu).