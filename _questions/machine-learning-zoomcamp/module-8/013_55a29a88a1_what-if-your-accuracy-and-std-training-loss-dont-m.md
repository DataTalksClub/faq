---
id: 55a29a88a1
question: What if your accuracy and std training loss don’t match HW?
sort_order: 13
---

Running the wasp/bee model on a Mac laptop might result in higher reported accuracy and lower standard deviation than expected from the HW answers. This discrepancy could be related to the version of the SGD optimizer being used. A message may appear about new and legacy versions.

- Try running the same code on Google Colab or another platform. The results may align closer with HW answers on Colab.
- Change the runtime to use a T4 GPU for faster execution compared to CPU.