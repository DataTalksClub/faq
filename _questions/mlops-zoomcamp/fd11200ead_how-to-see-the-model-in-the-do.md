---
course: mlops-zoomcamp
id: fd11200ead
question: How to see the model in the docker container in app/?
section: 'Module 4: Deployment'
sort_order: 1770
---

If anyone is troubleshooting or just interested in seeing the model listed on the image svizor/zoomcamp-model:mlops-3.10.0-slim.

Create a dockerfile. (yep thats all) and build “docker build -t zoomcamp_test .”

FROM svizor/zoomcamp-model:mlops-3.10.0-slim

Run “docker run -it zoomcamp_test ls /app” output -> model.bin

This will list the contents of the app directory and “model.bin” should output. With this you could just copy your files, for example “copy myfile .” maybe a requirements file and this can be run for example “docker run -it myimage myscript arg1 arg2 ”. Of course keep in mind a build is needed everytime you change the Dockerfile.

Another variation is to have it run when you run the docker file.

“””

FROM svizor/zoomcamp-model:mlops-3.10.0-slim

WORKDIR /app

CMD ls

“””

Just keep in mind CMD is needed because the RUN commands are used for building the image and the CMD is used at container runtime. And in your example you probably want to run a script or should we say CMD a script.

Quinn Avila

