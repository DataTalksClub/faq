---
id: c04524a66d
question: 'Docker: Flask image was built and tested successfully, but tensorflow serving
  image was built and unable to test successfully. What could be the problem?'
sort_order: 31
---

The TF and TF Serving versions have to match.

For Module 10.3, if you are on Apple Silicon and you encounter the following error when trying to run TF-Serving locally with Docker:

```bash
/usr/bin/tf_serving_entrypoint.sh: line 3:     7 Illegal instruction     tensorflow_model_server --port=8500 --rest_api_port=8501 --model_name=${MODEL_NAME} --model_base_path=${MODEL_BASE_PATH}/${MODEL_NAME} "$@"
```

You may find a solution in this [GitHub comment](https://github.com/tensorflow/serving/issues/1816#issuecomment-2445056791).

Docker release 4.35.0 for Mac introduces Docker VMM Beta, a replacement for the Apple Virtualisation Framework using Rosetta. You can now run the native TF Serving image.