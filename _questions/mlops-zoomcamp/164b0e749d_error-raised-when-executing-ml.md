---
course: mlops-zoomcamp
id: 164b0e749d
question: Error raised when executing mlflow’s pyfunc.load_model in lambda function.
section: 'Module 4: Deployment'
sort_order: 1730
---

When the request is processed in lambda function, mlflow library raises:

2022/09/19 21:18:47 WARNING mlflow.pyfunc: Encountered an unexpected error (AttributeError("module 'dataclasses' has no attribute '__version__'")) while detecting model dependency mismatches. Set logging level to DEBUG to see the full traceback.

Solution: Increase the memory of the lambda function.

Added by MarcosMJD

