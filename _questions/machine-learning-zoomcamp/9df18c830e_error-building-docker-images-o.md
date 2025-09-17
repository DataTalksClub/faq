---
id: 9df18c830e
question: Error building Docker images on Mac with M1 silicon
section: 5. Deploying Machine Learning Models
course: machine-learning-zoomcamp
sort_order: 1810
---

Do you get errors building the Docker image on the Mac M1 chipset?

The error I was getting was:

Could not open '/lib64/ld-linux-x86-64.so.2': No such file or directory

The fix (from ): vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

Open mlbookcamp-code/course-zoomcamp/01-intro/environment/Dockerfile

Replace line 1 with

FROM --platform=linux/amd64 ubuntu:latest

Now build the image as specified. In the end it took over 2 hours to build the image but it did complete in the end.

David Colton

