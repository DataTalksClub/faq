---
id: ace84c3970
question: Keras model training fails with “Failed to find data adapter”
section: 8. Neural Networks and Deep Learning
course: machine-learning-zoomcamp
sort_order: 2940
---

While training a Keras model you get the error “Failed to find data adapter that can handle input: <class 'keras.src.preprocessing.image.ImageDataGenerator'>, <class 'NoneType'>” you may have unintentionally passed the image generator instead of the dataset to the model

train_gen = ImageDataGenerator(rescale=1./255)

train_ds = train_gen.flow_from_directory(…)

history_after_augmentation = model.fit(

train_gen, # this should be train_ds!!!

epochs=10,

validation_data=test_gen # this should be test_ds!!!

)

The fix is simple and probably obvious once pointed out, use the training and validation dataset (train_ds and val_ds) returned from flow_from_directory

Added by Tzvi Friedman

