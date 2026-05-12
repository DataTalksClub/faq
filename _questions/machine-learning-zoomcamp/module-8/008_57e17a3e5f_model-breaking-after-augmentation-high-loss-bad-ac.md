---
id: 57e17a3e5f
question: Model breaking after augmentation – high loss + bad accuracy
sort_order: 8
---

When resuming training after augmentation, the loss skyrockets (1000+ during the first epoch) and accuracy settles around 0.5 – i.e. the model becomes as good as a random coin flip.

**Check** that the augmented `ImageDataGenerator` still includes the `rescale` option as specified in the preceding step.