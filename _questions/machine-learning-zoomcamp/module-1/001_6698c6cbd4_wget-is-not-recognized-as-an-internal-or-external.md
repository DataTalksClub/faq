---
id: 6698c6cbd4
question: wget is not recognized as an internal or external command
sort_order: 1
---

If you encounter the error "wget is not recognized as an internal or external command," wget needs to be installed.

This error may also cause messages like "No such file or directory: 'output.csv.gz'."

**Installation Instructions:**

- **On Ubuntu:**

  ```bash
  sudo apt-get install wget
  ```

- **On macOS:**

  Use [Homebrew](https://brew.sh/):

  ```bash
  brew install wget
  ```

- **On Windows:**

  Use [Chocolatey](https://chocolatey.org/):

  ```bash
  choco install wget
  ```

  Alternatively, download a binary from [GnuWin32](https://gnuwin32.sourceforge.net/packages/wget.htm) and place it in a location that is in your PATH (e.g., `C:/tools/`).

**Alternative Windows Installation:**

1. Download the latest wget binary for Windows from [eternallybored](https://eternallybored.org/misc/wget/).
2. If you downloaded the zip, extract all files (use [7-zip](https://7-zip.org/) if the built-in utility gives an error).
3. Rename the file `wget64.exe` to `wget.exe` if necessary.
4. Move `wget.exe` to your `Git\mingw64\bin\` directory.

**Python Alternatives:**

- Use the Python `wget` library. First, install it:

  ```bash
  pip install wget
  ```

  Then download a file:

  ```python
  import wget

  wget.download("URL")
  ```

  Or from the command line:

  ```bash
  python -m wget <URL>
  ```

- Use `pandas` to read a CSV directly from a URL:

  ```python
  import pandas as pd

  url = "https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv"

  df = pd.read_csv(url)
  ```

  Valid URL schemes include http, ftp, s3, gs, and file.

- Or use `urllib` from the standard library:

  ```python
  import urllib.request

  url = "https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv"

  urllib.request.urlretrieve(url, "housing.csv")
  ```

You can also paste the file URL into your web browser to download normally, then move the file to your working directory.

**Additional Recommendation:**

Consider using the Python library [requests](https://pypi.org/project/requests) for loading gz files.
