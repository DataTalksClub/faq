---
course: data-engineering-zoomcamp
id: 47f7c8310a
question: GCP BQ ML - Export ML model to make predictions does not work for MacBook
  with Apple M1 chip (arm architecture).
section: 'Module 3: Data Warehousing'
sort_order: 2280
---

Solution: proceed with setting up serving_dir on your computer as in the extract_model.md file. Then instead of

docker pull tensorflow/serving

use

docker pull emacski/tensorflow-serving

Then

docker run -p 8500:8500 -p 8501:8501 --mount type=bind,source=`pwd`/serving_dir/tip_model,target=/models/tip_model -e MODEL_NAME=tip_model -t emacski/tensorflow-serving

Then run the curl command as written, and you should get a prediction.

Or new since Oct 2024:

Beta release of Docker VMM - the more performant alternative to Apple Virtualization Framework on macOS (requires Apple Silicon and macOS 12.5 or later).

![Image](images/data-engineering-zoomcamp/image_51551549.png)

