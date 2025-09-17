---
id: e269cf9e38
question: Exception: Jupyter command `jupyter-notebook` not found.
section: Module 5: pyspark
course: data-engineering-zoomcamp
sort_order: 3420
---

Even after we have exported our paths correctly you may find that  even though Jupyter is installed you might not have Jupyter Noteboopgak for one reason or another. Full instructions are found  (for my walkthrough) or  (where I got the original instructions from) but are included below. These instructions include setting up a virtual environment (handy if you are on your own machine doing this and not a VM):

Full steps:

Update and upgrade packages:

sudo apt update && sudo apt -y upgrade

Install Python:

sudo apt install python3-pip python3-dev

Install Python virtualenv:

sudo -H pip3 install --upgrade pip

sudo -H pip3 install virtualenv

Create a Python Virtual Environment:

mkdir notebook

cd notebook

virtualenv jupyterenv

source jupyterenv/bin/activate

Install Jupyter Notebook:

pip install jupyter

Run Jupyter Notebook:

jupyter notebook

