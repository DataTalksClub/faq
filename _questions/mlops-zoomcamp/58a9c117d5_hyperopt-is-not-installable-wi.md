---
id: 58a9c117d5
question: Hyperopt is not installable with Conda
section: Module 2: Experiment tracking
course: mlops-zoomcamp
sort_order: 1250
---

Description

When setting up your venv with

$conda install --file requirements.txt

You may encounter the following error

​​

```

PackagesNotFoundError: The following packages are not available from current channels:

- hyperopt

```

Solution

It is probably because your conda is out of date. You can update Conda with

$conda update -n base -c defaults conda

If that doesn’t work you can always install it via, which is the advice from the

$conda install intel::hyperopt

Added by Marcus Leiwe

