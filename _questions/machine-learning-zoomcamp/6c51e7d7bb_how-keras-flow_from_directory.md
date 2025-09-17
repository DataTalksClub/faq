---
id: 6c51e7d7bb
question: How keras flow_from_directory know the names of classes in images?
section: 8. Neural Networks and Deep Learning
course: machine-learning-zoomcamp
sort_order: 2870
---

Problem:

When we run train_gen.flow_from_directory() as in video 8.5, it finds images belonging to 10 classes. Does it understand the names of classes from the names of folders? Or, there is already something going on deep behind?

Solution:

The name of class is the folder name

If you just create some random folder with the name "xyz", it will also be considered as a class!! The name itself is saying flow_from_directory

a clear explanation below:

Added by Bhaskar Sarma

Error with Tensorflow importing using saturn Cloud preconfigured template:

TypeError: Unable to convert function return value to a Python type! The signature was 	() -> handle.

Successful Dependency Reinstallation:

Just try uninstalling and re-installing tensorflow you got from saturnCloud twice or thrice.

When you uninstalled and reinstalled TensorFlow, it might have resolved underlying issues with dependencies. TensorFlow relies on several libraries (e.g., protobuf, numpy, grpcio) that can sometimes cause conflicts. By reinstalling, you ensured that all dependencies were reinstalled and aligned with the correct version, allowing TensorFlow to work as expected.

Late Recognition of the Change:

In some cases, it might take a moment for the system to recognize the changes in the Python environment after installing packages. It could be that the environment was still "stuck" in an old state before, and after several installation attempts, the correct state was finally loaded, especially after restarting the Jupyter kernel.

Added by Abdiaziz Qaladid

