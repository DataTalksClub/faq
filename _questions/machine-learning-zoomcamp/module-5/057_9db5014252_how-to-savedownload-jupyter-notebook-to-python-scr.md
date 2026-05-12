---
id: 9db5014252
question: How to save/download jupyter notebook to python script
sort_order: 57
---

You can convert a Jupyter notebook to a Python script using the following methods:

- **Using the terminal**
  
  Run the command below in the terminal:

  ```bash
  jupyter nbconvert --to python notebook.ipynb
  ```
  
  This converts the notebook into a Python script with the same name but with a `.py` extension.
  
- **Using the Jupyter Notebook interface**
  
  1. Navigate to `File` in the menu.
  2. Select `Save and Export Notebook As`.
  3. Choose `Executable Scripts`.

  This will download the file to your downloads folder.