---
course: machine-learning-zoomcamp
id: c4ad81910b
question: Install Docker (udocker) in Google Colab
section: 9. Serverless Deep Learning
sort_order: 3350
---

I’ve tried to do everything in Google Colab. Here is a way to work with Docker in Google Colab:

%%shell

pip install udocker

udocker --allow-root install

!udocker --allow-root run hello-world

Added by Ivan Brigida

