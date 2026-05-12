---
id: 0e58ef1736
question: How to unzip a folder with an image dataset and suppress output?
sort_order: 10
---

If you unzip a dataset within a Jupyter Notebook using the `! unzip` command, you may encounter extensive output messages for each file. To suppress this output, follow these solutions:

Using Magic Commands

```python
%%capture

! unzip zipped_folder_name.zip -d destination_folder_name
```

Using Python's zipfile Library

```python
import zipfile

local_zip = 'data.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('data')
zip_ref.close()
```

Use Solution 1 to suppress output directly in the notebook. Solution 2 provides an alternative approach using Python code.