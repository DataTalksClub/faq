---
id: 23ed7bdf10
question: WSL instructions
section: Module 1: Introduction
course: mlops-zoomcamp
sort_order: 310
---

If you wish to use WSL on your windows machine, here are the setup instructions:

Command: Sudo apt install wget

Get . wget <download address>

Command: git clone <github repository address>

Jupyter: pip3 install jupyter

Added by Gregory Morris ()

All in all softwares at one shop:

You can use anaconda which has all built in services like pycharm, jupyter

Added by Khaja Zaffer ()

Alternatively, you can download miniforge, which is a more lightweight open-source version of conda, which doesn’t rely on the proprietary Anaconda repository and allows you to use mamba, as a default package manager, which greatly improves environment solving speed.

For a clear, step-by-step guide to installing miniforge, the Texas Tech University High Performance Computing Center has an excellent comprehensive guide:

Added by Jon Areas ()

For windows “wsl --install” in Powershell

Added by Vadim Surin ()

If python is still showing as 3.10 after installing anaconda with Python 3.9, try running ‘source .bashrc’ from ${HOME} folder, for any reason if its still not working, add ‘export PATH=”<anaconda install path>/bin:$PATH”’

