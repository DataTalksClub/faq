---
id: 2dc4089953
question: Why do we need the --rm flag
section: 5. Deploying Machine Learning Models
course: machine-learning-zoomcamp
sort_order: 1880
---

What is the reason we don’t want to keep the docker image in our system and why do we need to run docker containers with `--rm` flag?

For best practice, you don’t want to have a lot of abandoned docker images in your system. You just update it in your folder and trigger the build one more time.

They consume extra space on your disk. Unless you don’t want to re-run the previously existing containers, it is better to use the `--rm` option.

The right way to say: “Why do we remove the docker container in our system?”. Well the docker image is still kept; it is the container that is not kept. Upon execution, images are not modified; only containers are.

The option `--rm` is for removing containers. The images remain until you remove them manually. If you don’t specify a version when building an image, it will always rebuild and replace the latest tag. `docker images` shows you all the image you have pulled or build so far.

During development and testing you usually specify `--rm` to get the containers auto removed upon exit. Otherwise they get accumulated in a stopped state, taking up space. `docker ps -a` shows you all the containers you have in your host. Each time you change Pipfile (or any file you baked into the container), you rebuild the image under the same tag or a new tag. It’s important to understand the difference between the term “docker image” and “docker container”. Image is what we build with all the resources baked in. You can move it around, maintain it in a repository, share it. Then we use the image to spin up instances of it and they are called containers.

Added by Muhammad Awon

