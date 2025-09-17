---
id: b389358dc7
question: How to install Conda environment in my local machine?
section: Miscellaneous
course: machine-learning-zoomcamp
sort_order: 4130
---

You don’t install a conda environment. First you create it, then you activate it.

Step 1: how to create a conda environment?

In a terminal write the command (ml-zoomcamp is the name of the environment):

conda create -n ml-zoomcamp

Step 2: how to activate a conda environment?

conda activate ml-zoomcamp

You can verify that it worked if you see (ml-zoomcamp) prepended to your command prompt.

Note:

The answer above assumes Anaconda has already been installed on your local machine. If this is not the case, you can download it from . After installing it, you can verify it succeeded with the following command in a terminal: conda --version.

(added by Kemal Dahha)

