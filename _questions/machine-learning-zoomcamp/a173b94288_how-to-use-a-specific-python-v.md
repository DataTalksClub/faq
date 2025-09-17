---
id: a173b94288
question: How to use a specific python version (e.g. 3.11) from conda with pipenv?
section: 5. Deploying Machine Learning Models
course: machine-learning-zoomcamp
sort_order: 2350
---

First of all, you should avoid being in a virtual environment when using pipenv. You can point pipenv directly to the Python 3.11 interpreter from your Conda installation:

Activate conda env conda activate env_name

Get python path which python

Deactivate conda env conda deactivate

Use pipenv with the python path found in 3 pipenv --python /path/to/python

(added by Kemal Dahha)

