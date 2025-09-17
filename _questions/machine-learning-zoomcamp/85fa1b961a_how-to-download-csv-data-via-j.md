---
course: machine-learning-zoomcamp
id: 85fa1b961a
question: How to download CSV data via Jupyter NB and the Kaggle API, for one seamless
  experience
section: 5. Deploying Machine Learning Models
sort_order: 1770
---

You’ll need a kaggle account

Go to settings, API and click `Create New Token`. This will download a `kaggle.json` file which contains your `username` and `key` information

In the same location as your Jupyter NB, place the `kaggle.json` file

Run `!chmod 600 <ENTER YOUR FILEPATH>/kaggle.json`

Make sure to import os via `import os` and then run:

os.environ['KAGGLE_CONFIG_DIR'] = <STRING OF YOUR FILE PATH>

Finally you can run directly in your NB: `!kaggle datasets download -d kapturovalexander/bank-credit-scoring`

And then you can unzip the file and access the CSV via: `!unzip -o bank-credit-scoring.zip`

>>> Michael Fronda <<<

