---
course: mlops-zoomcamp
id: b53176b742
question: Error pipenv command not found after pipenv installation
section: 'Module 4: Deployment'
sort_order: 1810
---

When installing pipenv using --user option, not to all users, you would need to update the PATH environment variable to run pipenv commands. 
You can update the env variable but its much better to update your .bashrc or .profile, depends on you OS, to persist the change. Go to your .bashrc file and include or update a line like this:

`PATH="<path_to_your_pipenv_install_dir>:$PATH”`

Or you can try to reinstall pipenv as root, for all users:

sudo -H pip install -U pipenv

Added by Eduardo Muñoz

