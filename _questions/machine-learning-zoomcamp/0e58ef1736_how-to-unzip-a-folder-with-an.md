---
course: machine-learning-zoomcamp
id: 0e58ef1736
question: How to unzip a folder with an image dataset and suppress output?
section: 8. Neural Networks and Deep Learning
sort_order: 2860
---

Problem:

A dataset for homework is in a zipped folder. If you unzip it within a jupyter notebook by means of ! unzip command, you’ll see a huge amount of output messages about unzipping of each image. So you need to suppress this output

Solution:

Execute the next cell:

%%capture

! unzip zipped_folder_name.zip -d destination_folder_name

Added by Alena Kniazeva

Inside a Jupyter Notebook:

import zipfile

local_zip = 'data.zip'

zip_ref = zipfile.ZipFile(local_zip, 'r')

zip_ref.extractall('data')

zip_ref.close()

