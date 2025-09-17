---
course: data-engineering-zoomcamp
id: c2f39b0ef3
question: Alternative way to convert Jupyter notebook to Python script  (via jupytext)
section: 'Module 1: Docker and Terraform'
sort_order: 1800
---

If you keep getting errors with nbconvert after: jupyter nbconvert --to script <your_notebook.ipynb>

you could try to convert your Jupyter notebook via another tool called jupytext

Jupytext is another excellent tool for converting Jupyter Notebooks to Python scripts, which works very similar to nbconvert

Install jupytext

pip install jupytext

Convert your Notebook to a Python script

jupytext --to py <your_notebook.ipynb>

