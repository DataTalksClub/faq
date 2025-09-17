---
id: a2d10b83d9
question: Pipenv installation not working (AttributeError: module 'collections' has no attribute 'MutableMapping')
section: Module 4: Deployment
course: mlops-zoomcamp
sort_order: 1560
---

If one gets pipenv failures for pipenv install command -

AttributeError: module 'collections' has no attribute 'MutableMapping'

It happens because you use the system Python (3.10) for pipenv.

If you previously installed pipenv with apt-get, remove it - sudo-apt remove pipenv

Make sure you have a non-system Python installed in your environment. The easiest way to do it is to install anaconda or miniconda

Next, install pipenv to your non-system Python. If you use the setup from the lectures, it’s just this: pip install pipenv

Now re-run pipenv install XXXX (relevant dependencies) - should work

Tested and worked on AWS instance, similar to the config Alexey presented in class.

Added by Daniel HenSSL

