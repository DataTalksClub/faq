---
id: 930f795453
question: Illegal instruction error when running tensorflow/serving image on Mac M2 Apple Silicon (potentially on M1 as well)
section: 10. Kubernetes and TensorFlow Serving
course: machine-learning-zoomcamp
sort_order: 3650
---

Similar to the one above but with a different solution the main reason is that emacski doesn’t seem to maintain the repo any more, the latest image is from 2 years ago at the time of writing (December 2023)

Problem:

While trying to run the docker code on Mac M2 apple silicon:

docker run --platform linux/amd64 -it --rm \

-p 8500:8500 \

-v $(pwd)/clothing-model:/models/clothing-model/1 \

-e MODEL_NAME="clothing-model" \

tensorflow/serving

You get an error:

/usr/bin/tf_serving_entrypoint.sh: line 3:     7 Illegal instruction     tensorflow_model_server --port=8500 --rest_api_port=8501 --model_name=${MODEL_NAME} --model_base_path=${MODEL_BASE_PATH}/${MODEL_NAME} "$@"

Solution:

Use bitnami/tensorflow-serving base image

Launch it either using docker run

docker run -d \

--name tf_serving \

-p 8500:8500 \

-p 8501:8501 \

-v $(pwd)/clothing-model:/bitnami/model-data/1 \

-e TENSORFLOW_SERVING_MODEL_NAME=clothing-model \

bitnami/tensorflow-serving:2

Or the following docker-compose.yaml

version: '3'

services:

tf_serving:

image: bitnami/tensorflow-serving:2

volumes:

- ${PWD}/clothing-model:/bitnami/model-data/1

ports:

- 8500:8500

- 8501:8501

environment:

- TENSORFLOW_SERVING_MODEL_NAME=clothing-model

And run it with

docker compose up

Added by Alex Litvinov

Or new since Oct 2024:

Beta release of Docker VMM - the more performant alternative to Apple Virtualization Framework on macOS (requires Apple Silicon and macOS 12.5 or later).

![Image](images/machine-learning-zoomcamp/image_51551549.png)

