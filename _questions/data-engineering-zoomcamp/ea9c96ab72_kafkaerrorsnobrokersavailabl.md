---
course: data-engineering-zoomcamp
id: ea9c96ab72
question: 'kafka.errors.NoBrokersAvailable: NoBrokersAvailable'
section: 'Module 6: streaming with kafka'
sort_order: 3990
---

If you have this error, it most likely that your kafka broker docker container is not working.

Use docker ps to confirm

Then in the docker compose yaml file folder, run docker compose up -d to start all the instances.

