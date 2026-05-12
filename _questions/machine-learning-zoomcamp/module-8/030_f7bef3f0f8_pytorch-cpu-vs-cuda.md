---
id: f7bef3f0f8
question: Should I install the CUDA build of PyTorch, or is CPU-only enough?
sort_order: 30
---

For learning and the homework, the CPU-only build is fine and much smaller (~200 MB vs ~2 GB).

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
# or
uv add torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

You only need the CUDA build if you have an NVIDIA GPU on the same machine. Otherwise, train on Google Colab (free GPU runtimes) and keep your local install CPU-only.
