---
id: 47f7c8310a
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_51551549.png
question: GCP BQ ML - Export ML model to make predictions does not work for MacBook
  with Apple M1 chip (arm architecture).
sort_order: 28
---

**Solution:**

Proceed with setting up `serving_dir` on your computer as described in the `extract_model.md` file. Then, instead of using:

```bash
docker pull tensorflow/serving
```

use:

```bash
docker pull emacski/tensorflow-serving
```

Then run:

```bash
docker run -p 8500:8500 -p 8501:8501 --mount type=bind,source=`pwd`/serving_dir/tip_model,target=/models/tip_model -e MODEL_NAME=tip_model -t emacski/tensorflow-serving
```

After that, run the `curl` command as instructed, and you should get a prediction.

**Or new since Oct 2024:**

Beta release of Docker VMM - the more performant alternative to Apple Virtualization Framework on macOS (requires Apple Silicon and macOS 12.5 or later). [https://docs.docker.com/desktop/features/vmm/](https://docs.docker.com/desktop/features/vmm/)

<{IMAGE:image_1}>
