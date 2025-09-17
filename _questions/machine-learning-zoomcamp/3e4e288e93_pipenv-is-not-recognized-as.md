---
course: machine-learning-zoomcamp
id: 3e4e288e93
question: '''pipenv'' is not recognized as an internal or external command, operable
  program or batch file.'
section: 5. Deploying Machine Learning Models
sort_order: 1990
---

This error happens because pipenv is already installed but you can't access it from the path.

This error comes out if you run.

pipenv  --version

pipenv shell

Solution for Windows

Open this option

![Image](images/machine-learning-zoomcamp/image_6db28918.png)

Click here

![Image](images/machine-learning-zoomcamp/image_3b4fce52.png)

Click in Edit Button

![Image](images/machine-learning-zoomcamp/image_b2712e9d.png)

Make sure the next two locations are on the PATH, otherwise, add it.

C:\Users\AppData\....\Python\PythonXX\

C:\Users\AppData\....\Python\PythonXX\Scripts\

![Image](images/machine-learning-zoomcamp/image_a4cd7017.png)

Added by Alejandro Aponte

Note: this answer assumes you don’t use Anaconda. For Windows, using Anaconda would be a better choice and less prone to errors.

