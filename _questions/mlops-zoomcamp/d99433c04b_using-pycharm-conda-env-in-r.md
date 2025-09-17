---
id: d99433c04b
question: Using PyCharm & Conda env in remote development
section: Module 1: Introduction
course: mlops-zoomcamp
sort_order: 640
---

Problem: PyCharm (remote) doesn’t see conda execution path. So, I cannot use conda env (which is located on a remote server).

Solution: In remote server in command line write “conda activate envname”, after write “which python” - it gives you python execution path. After you can use this path when you will add new interpreter in PyCharm: add local interpreter -> system interpreter -> and put the path with python.

Salimov Ilnaz ()

