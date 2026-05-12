---
id: 930f795453
images:
- description: 'image #1'
  id: image_1
  path: images/machine-learning-zoomcamp/image_51551549.png
question: Illegal instruction error when running tensorflow/serving image on Mac M2
  Apple Silicon (potentially on M1 as well)
sort_order: 27
---

Problem:

While trying to run the following Docker code on Mac M2 Apple Silicon:

```bash
docker run --platform linux/amd64 -it --rm \
-p 8500:8500 \
-v $(pwd)/clothing-model:/models/clothing-model/1 \
-e MODEL_NAME="clothing-model" \
tensorflow/serving
```

You get an error:

```bash
/usr/bin/tf_serving_entrypoint.sh: line 3:     7 Illegal instruction     tensorflow_model_server --port=8500 --rest_api_port=8501 --model_name=${MODEL_NAME} --model_base_path=${MODEL_BASE_PATH}/${MODEL_NAME} "$@"
```

Solution:

1. **Use Bitnami TensorFlow-Serving Base Image**
   
   Launch it either using `docker run`:
   
   ```bash
   docker run -d \
   --name tf_serving \
   -p 8500:8500 \
   -p 8501:8501 \
   -v $(pwd)/clothing-model:/bitnami/model-data/1 \
   -e TENSORFLOW_SERVING_MODEL_NAME=clothing-model \
   bitnami/tensorflow-serving:2
   ```
   
   Or use the following `docker-compose.yaml`:
   
   ```yaml
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
   ```
   
   And run it with:
   
   ```bash
   docker compose up
   ```

2. **Alternative since Oct 2024:**

   Beta release of Docker VMM - the more performant alternative to Apple Virtualization Framework on macOS (requires Apple Silicon and macOS 12.5 or later). [Docker VMM Documentation](https://docs.docker.com/desktop/features/vmm/)

<{IMAGE:image_1}>