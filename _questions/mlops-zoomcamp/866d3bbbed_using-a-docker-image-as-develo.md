---
id: 866d3bbbed
question: Using a docker image as development environment (Linux)
section: Module 1: Introduction
course: mlops-zoomcamp
sort_order: 730
---

If you don’t want to install anaconda on your machine and don’t want to use codespace or a VPS, you could create a docker image and run it locally.

For this, can use the following Dockerfile:

FROM docker.io/bitnami/minideb:bookworm

RUN install_packages wget ca-certificates vim less silversearcher-ag

# Uncomment the `COPY` and comment the `RUN` line if you have downloaded anaconda manually

# I did this to save bandwith when experimenting with the image creation

RUN wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh && bash Anaconda3-2022.05-Linux-x86_64.sh -b -p /opt/anaconda3

#COPY  Anaconda3-2022.05-Linux-x86_64.sh /tmp/Anaconda3-2022.05-Linux-x86_64.sh

RUN   bash /tmp/Anaconda3-2022.05-Linux-x86_64.sh -b -p /opt/anaconda3 && \

rm /tmp/Anaconda3-2022.05-Linux-x86_64.sh

ENV PATH="/opt/anaconda3/bin:$PATH" \

HOME="/app"

EXPOSE 8888

WORKDIR /app

USER 1001

ENTRYPOINT [ "jupyter", "notebook", "--ip", "0.0.0.0" ]

Build the image using:

docker build -f Dockerfile -t mlops:v0 .

Then you could run it with:

mkdir app

chmod -R 777 app

docker run --name jupyter -p 8888:8888 -v ./app:/app mlops:v0

In the logs you could see the jupyter URL that you need to use to enter the jupyter environment. The files you create in the environment will be written under app directory.

