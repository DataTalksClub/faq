---
id: b4d1cdc85f
question: Docker - Error during connect: In the default daemon configuration on Windows, the docker client must be run with elevated privileges to connect.: Post: "http://%2F%2F.%2Fpipe%2Fdocker_engine/v1.24/containers/create" : open //./pipe/docker_engine: The system cannot find the file specified
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 580
---

As the official  says, the Docker engine can either use the

Hyper-V or WSL2 as its backend. However, a few constraints might apply

Windows 10 Pro / 11 Pro Users: 
In order to use Hyper-V as its back-end, you MUST have it enabled first, which you can do by following the tutorial:

Windows 10 Home / 11 Home Users: 
On the other hand, Users of the 'Home' version do NOT have the option Hyper-V option enabled, which means, you can only get Docker up and running using the WSL2 credentials(Windows Subsystem for Linux). Url

You can find the detailed instructions to do so here: rt g

In case, you run into another issue while trying to install WSL2 (WslRegisterDistribution failed with error: 0x800701bc), Make sure you update the WSL2 Linux Kernel, following the guidelines here:

