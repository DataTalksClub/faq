---
id: 9e5f381432
question: I can’t create the environment on AWS Elastic Beanstalk with the command proposed during the video
section: 5. Deploying Machine Learning Models
course: machine-learning-zoomcamp
sort_order: 2270
---

I struggled with the command :

eb init -p docker tumor-diagnosis-serving -r eu-west-1

Which resulted in an error when running : eb local run --port 9696

ERROR: NotSupportedError - You can use "eb local" only with preconfigured, generic and multicontainer Docker platforms.

I replaced it with :

eb init -p "Docker running on 64bit Amazon Linux 2" tumor-diagnosis-serving -r eu-west-1

This allowed the recognition of the Dockerfile and the build/run of the docker container.

Added by Mélanie Fouesnard

