---
course: machine-learning-zoomcamp
id: 4538b68902
question: Host key verification failed.
section: 8. Neural Networks and Deep Learning
sort_order: 2820
---

Problem description:

Getting an error using <git clone :alexeygrigorev/clothing-dataset-small.git>

The error:

Cloning into 'clothing-dataset'...

Host key verification failed.

fatal: Could not read from remote repository.

Please make sure you have the correct access rights

and the repository exists.

Solution description:

when cloning the repo, you can also chose https - then it should work. This happens when you don't have your ssh key configured.

<git clone https://github.com/alexeygrigorev/clothing-dataset-small.git>

Added by Gregory Morris

