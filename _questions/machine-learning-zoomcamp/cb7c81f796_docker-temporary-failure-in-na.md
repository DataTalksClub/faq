---
id: cb7c81f796
question: Docker Temporary failure in name resolution
section: 9. Serverless Deep Learning
course: machine-learning-zoomcamp
sort_order: 3310
---

Add the next lines to vim /etc/docker/daemon.json

{

"dns": ["8.8.8.8", "8.8.4.4"]

}

Then, restart docker:  sudo service docker restart

Ibai Irastorza

