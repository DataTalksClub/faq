---
id: ba250275a3
images:
- description: 'image #1'
  id: image_1
  path: images/machine-learning-zoomcamp/image_16b33640.png
question: 'Kaggle: wget: unable to resolve host address raw.githubusercontent.com'
sort_order: 9
---

In Kaggle, when you attempt to `!wget` a dataset from GitHub or any other public repository, you might encounter the following error:

```
--2022-09-17 16:55:24--  https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... failed: Temporary failure in name resolution.
wget: unable to resolve host address 'raw.githubusercontent.com'
```

- In your Kaggle notebook settings, enable internet access for your session. This option is found in the settings panel on the right-hand side of the Kaggle screen.
- You will need to verify your phone number to confirm you are not a bot.

<{IMAGE:image_1}>