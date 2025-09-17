---
course: machine-learning-zoomcamp
id: f6d64d22b9
question: 'Q: ValueError: Path not found or generated: WindowsPath(''C:/Users/username/.virtualenvs/envname/Scripts'')'
section: 5. Deploying Machine Learning Models
sort_order: 2010
---

After entering `pipenv shell` don’t forget to use `exit` before `pipenv --rm`, as it may cause errors when trying to install packages, it is unclear whether you are “in the shell”(using Windows) at the moment as there are no clear markers for it.

It can also mess up PATH, if that’s the case, here’s terminal commands for fixing that:

# for Windows

set VIRTUAL_ENV ""

# for Unix

export VIRTUAL_ENV=""

Also manually re-creating removed folder at `C:\Users\username\.virtualenvs\removed-envname` can help, removed-envname can be seen at the error message.

Added by Andrii Larkin

