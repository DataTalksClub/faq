---
id: 6698c6cbd4
question: wget is not recognized as an internal or external command
section: 1. Introduction to Machine Learning
course: machine-learning-zoomcamp
sort_order: 270
---

If you get “wget is not recognized as an internal or external command”, you need to install it.

On Ubuntu, run

sudo apt-get install wget

On Windows, the easiest way to install wget is to use :

choco install wget

Or you can download a binary  and put it to any location in your PATH (e.g. C:/tools/)

On Mac, the easiest way to install wget is to use brew.

Brew install wget

Alternatively, you can use a Python wget library, but instead of simply using “wget” you’ll need to use

python -m wget

You need to install it with pip first:

pip install wget

And then in your python code, for example in your jupyter notebook, use:

import wget

wget.download("URL")

This should download whatever is at the URL in the same directory as your code.

(Memoona Tahira)

Alternatively, you can read a CSV file from a URL directly with pandas:

url = "https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv"

df = pd.read_csv(url)

Valid URL schemes include http, ftp, s3, gs, and file.

In some cases you might need to bypass https checks:

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

Or you can use the built-in Python functionality for downloading the files:

import urllib.request

url = ""

urllib.request.urlretrieve(url, "housing.csv")

Urllib.request.urlretrieve() is a standard Python library function available on all devices and platforms. URL requests and URL data retrieval are done with the urllib.request module.

The urlretrieve() function allows you to download files from URLs and save them locally. Python programs use it to download files from the internet.

On any Python-enabled device or platform, you can use the urllib.request.urlretrieve() function to download the file.

(Mohammad Emad Sharifi)

