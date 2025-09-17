---
id: beef541941
question: Bind for 0.0.0.0:5432 failed: port is already allocated
section: Module 5: Monitoring
course: mlops-zoomcamp
sort_order: 2070
---

Problem: When trying to start the postgres services through docker-compose up, this error occurs

Note: This issue occurs since port 5432 is already used by some other service.

Solution: update the port mapping for postgres service to 5433:5432 in docker compose yaml

Added by Sumeet Lalla

