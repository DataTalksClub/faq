---
course: data-engineering-zoomcamp
id: ed8dcfbb5a
question: Docker - The input device is not a TTY (Docker run for Windows)
section: 'Module 1: Docker and Terraform'
sort_order: 640
---

You may have this error:

$ docker run -it ubuntu bash

the input device is not a TTY. If you are using mintty, try prefixing the command with 'winpty'

Solution:

Use winpty before docker command ()

$ winpty docker run -it ubuntu bash

You also can make an alias:
echo "alias docker='winpty docker'" >> ~/.bashrc

OR

echo "alias docker='winpty docker'" >> ~/.bash_profile

