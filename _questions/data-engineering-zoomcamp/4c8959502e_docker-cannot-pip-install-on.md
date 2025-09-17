---
course: data-engineering-zoomcamp
id: 4c8959502e
question: Docker - Cannot pip install on Docker container (Windows)
section: 'Module 1: Docker and Terraform'
sort_order: 650
---

You may have this error:

Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<pip._vendor.u

rllib3.connection.HTTPSConnection object at 0x7efe331cf790>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution')':

/simple/pandas/

Possible solution might be:

$ winpty docker run -it --dns=8.8.8.8 --entrypoint=bash python:3.9

