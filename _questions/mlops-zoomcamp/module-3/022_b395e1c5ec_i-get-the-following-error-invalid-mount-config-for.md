---
id: b395e1c5ec
question: 'I get the following error: invalid mount config for type "bind": invalid
  specification: destination can''t be ''/'' when running docker compose up when running
  mage'
sort_order: 22
---

You should not run `docker compose up` for the mage repo directly. Instead, use:

```bash
bash ./scripts/start.sh
```

**Additional Information**

- The `start.sh` script handles necessary environment variable settings before executing `docker compose up`.
- Key environment variables such as `PROJECT_NAME` and `MAGE_CODE_PATH` should be set, potentially in your `.env` file.
- Note that if you are starting a new mage project, like in a capstone project, you may not have a `start.sh` script or a `scripts` directory, so ensure the environment variables are set correctly.

Update by another student from the MLOps Zoomcamp.