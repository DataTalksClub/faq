---
id: 1322100525
question: Error downloading  tensorflow/serving:2.7.0 on Apple M1 Mac
section: 10. Kubernetes and TensorFlow Serving
course: machine-learning-zoomcamp
sort_order: 3640
---

While trying to run the docker code on M1:

docker run --platform linux/amd64 -it --rm \

-p 8500:8500 \

-v $(pwd)/clothing-model:/models/clothing-model/1 \

-e MODEL_NAME="clothing-model" \

tensorflow/serving:2.7.0

It outputs the error:

Error:

Status: Downloaded newer image for tensorflow/serving:2.7.0

[libprotobuf FATAL external/com_google_protobuf/src/google/protobuf/generated_message_reflection.cc:2345] CHECK failed: file != nullptr:

terminate called after throwing an instance of 'google::protobuf::FatalException'

what():  CHECK failed: file != nullptr:

qemu: uncaught target signal 6 (Aborted) - core dumped

/usr/bin/tf_serving_entrypoint.sh: line 3:     8 Aborted                 tensorflow_model_server --port=8500 --rest_api_port=8501 --model_name=${MODEL_NAME} --model_base_path=${MODEL_BASE_PATH}/${MODEL_NAME} "$@"

Solution

docker pull emacski/tensorflow-serving:latest

docker run -it --rm \

-p 8500:8500 \

-v $(pwd)/clothing-model:/models/clothing-model/1 \

-e MODEL_NAME="clothing-model" \

emacski/tensorflow-serving:latest-linux_arm64

See more here:

Added by Daniel Egbo

