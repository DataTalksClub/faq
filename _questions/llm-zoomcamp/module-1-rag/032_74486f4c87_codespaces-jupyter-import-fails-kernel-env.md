---
id: 74486f4c87
question: Using GitHub Codespaces and added a Python package, but imports fail in
  my Jupyter notebook—what should I do?
sort_order: 32
---

If your package imports fail after installing it in GitHub Codespaces, first verify you installed the package into the same environment your notebook kernel is using:

- In the Codespaces terminal, run `uv pip list` and confirm your package shows up there.
- If it’s installed, the most common cause is that the notebook is running with a different virtual environment/workspace kernel than the one you installed into.
- In the Jupyter notebook UI, change the kernel (near the top of the screen) to the environment that matches your repo (e.g., the environment name for your repository).

After switching kernels, restart the notebook kernel and try the import again.