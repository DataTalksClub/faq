---
id: 664833c280
question: How to fix docker compose error: Error response from daemon: pull access denied for spark-3.3.1, repository does not exist or may require 'docker login': denied: requested access to the resource is denied
section: Module 6: streaming with kafka
course: data-engineering-zoomcamp
sort_order: 4010
---

If you get this error, know that you have not built your sparks and juypter images. This images aren’t readily available on dockerHub.

In the spark folder, run ./build.sh from a bash cli to to build all images before running docker compose

