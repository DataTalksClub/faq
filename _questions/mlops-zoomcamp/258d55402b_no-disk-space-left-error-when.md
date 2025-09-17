---
id: 258d55402b
question: no disk space left error when doing docker compose up
section: Module 5: Monitoring
course: mlops-zoomcamp
sort_order: 2030
---

Solution. Using docker CLI run docker system prune to remove unused things (build cache, containers, images etc)

Also, to see what’s taking space before pruning you can run docker system df

By Alex Litvinov

