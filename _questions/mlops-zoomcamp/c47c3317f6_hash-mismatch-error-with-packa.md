---
id: c47c3317f6
question: Hash Mismatch Error with Package Installation
section: Module 2: Experiment tracking
course: mlops-zoomcamp
sort_order: 860
---

Problem:

Getting

ERROR: THESE PACKAGES DO NOT MATCH THE HASHES FROM THE REQUIREMENTS FILE

during MLFlow's installation process, particularly while installing the Numpy package using pip

When I installed mlflow using ‘pip install mlflow’ on 27th May 2022, I got the following error while numpy was getting installed through mlflow:

Collecting numpy

Downloading numpy-1.22.4-cp310-cp310-win_amd64.whl (14.7 MB)

|██████████████              	| 6.3 MB 107 kB/s eta 0:01:19

ERROR: THESE PACKAGES DO NOT MATCH THE HASHES FROM THE REQUIREMENTS FILE.

If you have updated the package versions, please update the hashes. Otherwise, examine the package contents carefully; someone may have tampered with them.

numpy from  (from mlflow):

Expected sha256 3e1ffa4748168e1cc8d3cde93f006fe92b5421396221a02f2274aab6ac83b077

Got    	15e691797dba353af05cf51233aefc4c654ea7ff194b3e7435e6eec321807e90

Solution:

Then when I install numpy separately (and not as part of mlflow), numpy gets installed (same version), and then when I do 'pip install mlflow', it also goes through.

Please note that the above may not be consistently simulatable, but please be aware of this issue that could occur during pip install of mlflow.

Added by Venkat Ramakrishnan

