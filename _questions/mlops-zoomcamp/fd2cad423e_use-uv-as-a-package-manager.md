---
id: fd2cad423e
question: Use uv as a package manager
section: Module 1: Introduction
course: mlops-zoomcamp
sort_order: 740
---

There is an option to run the project without anaconda and not much pain with maintaining multiple pythons on your machine. The new package manager uv is a speedy and powerful one written in Rust. It’s good to use in your python projects overall.

uv venv --python 3.9.7 # install python 3.9.7 that is used in the course

source .venv/bin/activate # activate the environment

python -V # should be 3.9.7

uv pip install pandas scikit-learn notebook seaborn pyarrow # install required packages

jupyter notebook # run jupyter notebook

And cleanup has never been easy. Deactivate the environment and delete the folder

deactivate

rm -rf .venv

Added by Masha Loianych

