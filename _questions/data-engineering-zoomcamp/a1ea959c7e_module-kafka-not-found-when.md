---
course: data-engineering-zoomcamp
id: a1ea959c7e
question: Module “kafka” not found when trying to run producer.py
section: 'Module 6: streaming with kafka'
sort_order: 3900
---

Solution from Alexey: create a virtual environment and run requirements.txt and the python files in that environment.

To create a virtual env and install packages (run only once)

python -m venv env

source env/bin/activate

pip install -r ../requirements.txt

To activate it (you'll need to run it every time you need the virtual env):

source env/bin/activate

To deactivate it:

deactivate

This works on MacOS, Linux and Windows - but for Windows the path is slightly different (it's env/Scripts/activate)

Also the virtual environment should be created only to run the python file. Docker images should first all be up and running.

