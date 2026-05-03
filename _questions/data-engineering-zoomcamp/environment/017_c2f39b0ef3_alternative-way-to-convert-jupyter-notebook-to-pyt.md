---
id: c2f39b0ef3
question: Alternative way to convert Jupyter notebook to Python script (via jupytext)
sort_order: 17
---

If you keep getting errors with nbconvert after executing:

```bash
jupyter nbconvert --to script <your_notebook.ipynb>
```

You could try converting your Jupyter notebook using another tool called Jupytext. Jupytext is an excellent tool for converting Jupyter Notebooks to Python scripts, similar to nbconvert.

1. **Install Jupytext**
   
   ```bash
   pip install jupytext
   ```

2. **Convert your Notebook to a Python script**

   ```bash
   jupytext --to py <your_notebook.ipynb>
   ```