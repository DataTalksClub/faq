---
id: 2dab05f2be
question: How to Delete an Experiment Permanently from MLFlow UI
sort_order: 870
---

After deleting an experiment from UI, the deleted experiment still persists in the database.

Solution: To delete this experiment permanently, follow these steps.

Assuming you are using sqlite database;

Install ipython sql using the following command: pip install ipython-sql

In your jupyter notebook, load the SQL magic scripts with this: %load_ext sql

Load the database with this: %sql sqlite:///nameofdatabase.db

Run the following SQL script to delete the experiment permanently: check[ link ](https://stackoverflow.com/a/68431980/14151292)

