---
course: mlops-zoomcamp
id: bfbe05dcd9
question: Old version of glibc when running XGBoost
section: 'Module 2: Experiment tracking'
sort_order: 1170
---

Starting from version 2.1.0, XGBoost distributes its Python package in two variants:

manylinux_2_28: For recent Linux distributions with glibc 2.28 or newer. This variant includes all features, such as GPU algorithms and federated learning/

manylinux2014: For older Linux distributions with glibc versions older than 2.28. This variant lacks support for GPU algorithms and federated learning.

If you're installing XGBoost via pip, the package manager automatically selects the appropriate variant based on your system's glibc version. Starting May 31, 2025, the manylinux2014 variant will no longer be distributed.

This means that systems with glibc versions older than 2.28 will not be able to install future versions of XGBoost via pip unless they upgrade their glibc version or build XGBoost from source.

Added by Jon Areas (areasjx@gmail.com)

