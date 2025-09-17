---
course: mlops-zoomcamp
id: cc4481d2fa
question: Video 3.2.1 - Various issues with Global Data Products
section: 'Module 3: Orchestration'
sort_order: 1390
---

Running the GDP block takes forever.

Exception: Pipeline run xx for global data product training_set: failed

AttributeError: 'NoneType' object has no attribute 'to_dict'

We need to replicate the pipelines and codes into each sub-project as the Settings indicate that only one project can be active at any one time, which means the sub-projects do not communicate with each other. (Needs confirmation during office hours.)

Things you can try:

Make sure the following lines in the GDP block are for the actual project and pipeline you’re running

"project": "unit_2_training",

"repo_path": "/home/src/mlops/unit_2_training",

Interrupt and Restart Kernel from the Run menu

Bring docker down and restarting it via the script

If both of the above does not resolve, recreate everything from scratch:

Remove the connections from the hyperparameter_tuning/sklearn block in the Tree panel to its upstream blocks. Click on the connector → Remove Connection

Remove the Global Data Product block from the Tree panel, right click → Delete Block (ignore dependencies)

Click on All blocks and select the Global Data Products, drag+drop this block to be the first in the pipeline

Rename the block to what is used in the video

Run the block to test it (Play button or Ctrl+Enter)

If it helps, do the same for the file in path “unit_3_observability” (ella’s full disclosure: unit_2 works after I removed all things GDP and recreate, now I cannot replicate the same success for unit_3. Still trying…)

Error with creating Global Data Product on Mage: AttributeError: 'NoneType' object has no attribute 'to_dict'

Solution: Global product is currently not cross product. You will have to create the data preparation pipeline in unit_2_training and configure to build.

Added by Oluwadara Adedeji

