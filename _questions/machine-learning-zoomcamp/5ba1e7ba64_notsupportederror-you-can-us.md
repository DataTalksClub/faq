---
id: 5ba1e7ba64
question: NotSupportedError - You can use "eb local" only with preconfigured, generic and multicontainer Docker platforms.
section: 5. Deploying Machine Learning Models
course: machine-learning-zoomcamp
sort_order: 2210
---

Question:

When executing

eb local run  --port 9696

I get the following error:

ERROR: NotSupportedError - You can use "eb local" only with preconfigured, generic and multicontainer Docker platforms.

Answer:

There are two options to fix this:

Re-initialize by running eb init -i and choosing the options from a list (the first default option for docker platform should be fine).

Edit the ‘.elasticbeanstalk/config.yml’ directly changing the default_platform from Docker to default_platform: Docker running on 64bit Amazon Linux 2023

The disadvantage of the second approach is that the option might not be available the following years

Added by Alex Litvinov

An alternative solution is to re-run the init command but change the value after the -p flag from docker to a string like "Docker running on 64bit Amazon Linux". Then, re-run the first command. For example:

eb init -p "Docker running on 64bit Amazon Linux" <appname>

eb local run --port 9696

Added by Lynn Samson

Original solution from

