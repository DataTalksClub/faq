---
id: 2584892a72
question: Using image_dataset_from_directory instead of ImageDataGenerator for loading
  images
sort_order: 25
---

From the Keras documentation:

Deprecated: [`tf.keras.preprocessing.image.ImageDataGenerator`](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/ImageDataGenerator) is not recommended for new code.

Prefer loading images with [`tf.keras.utils.image_dataset_from_directory`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/image_dataset_from_directory) and transforming the output [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset) with preprocessing layers.

For more information, see the tutorials for [loading images](https://www.tensorflow.org/tutorials/load_data/images) and [augmenting images](https://www.tensorflow.org/tutorials/images/data_augmentation), as well as the [preprocessing layer guide](https://www.tensorflow.org/guide/keras/preprocessing_layers).