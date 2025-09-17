---
id: be8e47a85c
question: How do I push from Saturn Cloud to Github?
section: 8. Neural Networks and Deep Learning
course: machine-learning-zoomcamp
sort_order: 2750
---

Connecting your GPU on Saturn Cloud to Github repository is not compulsory, since you can just download the notebook and copy it to the Github folder. But if you like technology to do things for you, then follow the solution description below:

Solution description: Follow the instructions in these github docs to create an SSH private and public key:

Then the second video on this module about saturn cloud would show you how to add the ssh keys to secrets and authenticate through a terminal.

Or alternatively, you could just use the public keys provided by Saturn Cloud by default. To do so, follow these steps:

Click on your username and on manage

Down below you will see the Git SSH keys section.

Copy the default public key provided by Saturn Cloud

Paste these key into the SSH keys section of your github repo

Open a terminal on Saturn Cloud and run this command “ssh -T ”

You will receive a successful authentication notice.

Odimegwu David

Q: What versions of TensorFlow and NumPy should I use to ensure compatibility in Saturn Cloud notebooks?

A: To avoid compatibility issues when using TensorFlow in Saturn Cloud notebooks, we recommend the following versions:

bash

Copy code

!pip install numpy==1.24 tensorflow==2.10.0 These versions are tested and work seamlessly in the Saturn Cloud environment. Once installed, you should be able to develop and run your machine learning workflows without any issues.

Added by Abdiaziz Qaladid

