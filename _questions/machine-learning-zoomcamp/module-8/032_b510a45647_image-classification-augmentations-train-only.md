---
id: b510a45647
question: When training an image classification model, why should random data augmentations
  only be applied to training images (and not evaluation images)?
sort_order: 32
---

Data augmentation (e.g., random rotation, random cropping, horizontal flipping) makes the model generalize better by teaching it to handle different variations of the same underlying image.

The key constraint is that evaluation/validation images should stay deterministic. If you apply random transforms during evaluation, the evaluation set effectively changes from run to run, so metrics can fluctuate and it becomes harder to compare model performance fairly across experiments.

A typical setup uses separate transforms:

- For training: use augmented transforms that include randomness.
- For evaluation: use deterministic transforms only (no random rotation/crop/flip).

For example in PyTorch:

```python
train_dataset = datasets.ImageFolder(
    './data/train',
    transform=train_transform_augmented
)

evaluation_dataset = datasets.ImageFolder(
    './data/evaluation',
    transform=evaluation_transform
)
```

Key point: apply random augmentation to training images, but use deterministic transformations for evaluation so that comparisons remain consistent.