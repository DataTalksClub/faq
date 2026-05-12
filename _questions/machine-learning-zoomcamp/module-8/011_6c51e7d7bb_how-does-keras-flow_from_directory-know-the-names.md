---
id: 6c51e7d7bb
question: How does keras flow_from_directory know the names of classes in images?
sort_order: 11
---

Keras `flow_from_directory` understands the names of classes from the names of folders.


- When using `train_gen.flow_from_directory()`, the class names are derived from the folder names within the specified directory.
- For example, if you create a folder named "xyz", it will be considered a class.
- This behavior aligns with the function name `flow_from_directory`.

A detailed explanation can be found in this [tutorial](https://vijayabhaskar96.medium.com/tutorial-image-classification-with-keras-flow-from-directory-and-generators-95f75ebe5720).


