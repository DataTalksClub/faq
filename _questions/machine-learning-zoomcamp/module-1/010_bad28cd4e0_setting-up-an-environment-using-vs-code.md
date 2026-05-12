---
id: bad28cd4e0
question: Setting up an environment using VS Code
sort_order: 10
---

I found this video quite helpful: [Creating Virtual Environment for Python from VS Code](https://www.youtube.com/watch?v=8h9w0meM8i4)

**Native Jupyter Notebooks Support in VS Code**

In VS Code, you can have native Jupyter Notebooks support, i.e., you do not need to open a web browser to code in a Notebook. If you have port forwarding enabled, run a `jupyter notebook` command from a remote machine, and have a remote connection configured in `.ssh/config` (as Alexey’s [video](https://www.youtube.com/watch?v=IXSiYkP23zo) suggests), VS Code can execute remote Jupyter Notebook files on a remote server from your local machine: [Visual Studio Code Jupyter Notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).

**Git Support in VS Code**

You can work with GitHub from VS Code. Staging and commits are easy from the VS Code’s UI:

[Visual Studio Code Source Control Overview](https://code.visualstudio.com/docs/sourcecontrol/overview)