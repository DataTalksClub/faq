---
id: e269cf9e38
question: 'Exception: Jupyter command `jupyter-notebook` not found.'
sort_order: 15
---

Even after exporting paths correctly, you may find that Jupyter is installed but `jupyter-notebook` is not found. Follow these steps to resolve the issue:

Full steps:

1. **Update and Upgrade Packages:**
   ```bash
   sudo apt update && sudo apt -y upgrade
   ```

2. **Install Python:**
   ```bash
   sudo apt install python3-pip python3-dev
   ```

3. **Install Python Virtualenv:**
   ```bash
   sudo -H pip3 install --upgrade pip
   sudo -H pip3 install virtualenv
   ```

4. **Create a Python Virtual Environment:**
   ```bash
   mkdir notebook
   cd notebook
   virtualenv jupyterenv
   source jupyterenv/bin/activate
   ```

5. **Install Jupyter Notebook:**
   ```bash
   pip install jupyter
   ```

6. **Run Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```
   
For full instructions, refer to [this guide](https://learningdataengineering540969211.wordpress.com/2022/02/24/week-5-de-zoomcamp-5-2-1-installing-spark-on-linux/) or the original instructions [here](https://speedysense.com/install-jupyter-notebook-on-ubuntu-20-04/).