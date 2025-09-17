---
id: 687d54c6ba
question: Docker-compose takes infinitely long to install zip unzip packages for linux, which are required to unpack datasets
section: Module 3: Data Warehousing
course: data-engineering-zoomcamp
sort_order: 1980
---

A:

1 solution) Add -Y flag, so that apt-get automatically agrees to install additional packages

2) Use python ZipFile package, which is included in all modern python distributions

