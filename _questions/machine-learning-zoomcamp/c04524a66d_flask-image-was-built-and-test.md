---
course: machine-learning-zoomcamp
id: c04524a66d
question: Flask image was built and tested successfully, but tensorflow serving image
  was built and unable to test successfully. What could be the problem?
section: Miscellaneous
sort_order: 4240
---

The TF and TF Serving versions have to match (as per solution from the slack channel)

Added by Chiedu Elue

For Module 10.3, if you are on apple silicon:

if you see this error when trying to run TF-Serving locally with docker:

/usr/bin/tf_serving_entrypoint.sh: line 3:     7 Illegal instruction     tensorflow_model_server --port=8500 --rest_api_port=8501 --model_name=${MODEL_NAME} --model_base_path=${MODEL_BASE_PATH}/${MODEL_NAME} "$@"

if found this

Docker release 4.35.0 (172550) for Mac introduces Docker VMM Beta, a replacement for the Apple Virtualisation Framework using Rosetta. Good news is that I can run the native TF Serving image now on.

Till Meineke (Dec 11 2024)

