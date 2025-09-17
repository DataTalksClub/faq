---
id: 00b076410d
question: Jupyter nbconvert error
section: Module 4: Deployment
course: mlops-zoomcamp
sort_order: 1860
---

If you encounter an error when converting your notebook.ipnb into a Python script using the command:

jupyter nbconvert --to script your_notebook.ipynb

and you see the error message:

Jupyter command `jupyter-nbconvert` not found.

follow these steps:

Verify that you're in the directory containing your Jupyter notebook.( I’ve got this error message that confused me).

Install the necessary package: If the issue persists, you may need to install the nbconvert package. Run the following command:
pip install nbconvert

:After installing nbconvert, use the following command to convert your notebook to a Python script:

jupyter nbconvert your_notebook.ipynb --to python
Note: The correct command is slightly different (--to python instead of --to script).

Added by Anatolii Kryvko

