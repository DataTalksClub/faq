---
course: machine-learning-zoomcamp
id: 7bcbd64ac9
question: Conda Environment Setup
section: 1. Introduction to Machine Learning
sort_order: 390
---

With regards to creating an environment for the project, do we need to run the command "conda create -n ......." and "conda activate ml-zoomcamp" everytime we open vs code to work on the project?

Answer:

"conda create -n ...." is just run the first time to create the environment. Once created, you just need to run "conda activate ml-zoomcamp" whenever you want to use it.

(Added by Wesley Barreto)

conda env export > environment.yml will also allow you to reproduce your existing environment in a YAML file.  You can then recreate it with conda env create -f environment.yml

