---
course: machine-learning-zoomcamp
id: 2490b9e786
question: Reproducibility in different OS
section: Miscellaneous
sort_order: 4180
---

When trying to rerun the docker file in Windows, as opposed to developing in WSL/Linux, I got the error of:

```

Warning: Python 3.11 was not found on your system…

Neither ‘pipenv’ nor ‘asdf’ could be found to install Python.

You can specify specific versions of Python with:

$ pipenv –python path\to\python

```

The solution was to add Python311 installation folder to the PATH and restart the system and run the docker file again. That solved the error.

(Added by Abhijit Chakraborty)

