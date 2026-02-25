---
id: e3ce42af1a
question: How do you read data stored in GCS on pandas with your local computer?
sort_order: 37
---

To do this:

1. Install `gcsfs`:
   
   ```bash
   pip install gcsfs
   ```

2. Copy the URI path to the file and use the following command to read it:
   
   ```python
   df = pandas.read_csv('gs://path/to/your/file.csv')
   ```