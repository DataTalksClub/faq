---
id: b3030c88e7
question: wget is not recognized as an internal or external command
sort_order: 5
---

If you encounter the error "wget is not recognized as an internal or external command," wget needs to be installed.

This error may also cause messages like "No such file or directory: 'output.csv.gz'."

### Installation Instructions:

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

#### Alternative Windows Installation:

1. Download the latest wget binary for Windows from [eternallybored](https://eternallybored.org/misc/wget/).
2. If you downloaded the zip, extract all files (use [7-zip](https://7-zip.org/) if the built-in utility gives an error).
3. Rename the file `wget64.exe` to `wget.exe` if necessary.
4. Move `wget.exe` to your `Git\mingw64\bin\` directory.

#### Python Alternative:

- Use the Python wget library:

  First, install using pip:

  ```bash
  pip install wget
  ```

- Use it with Python:

  ```bash
  python -m wget
  ```

You can also paste the file URL into your web browser to download normally, then move the file to your working directory.

### Additional Recommendation:

Consider using the Python library [requests](https://pypi.org/project/requests) for loading gz files.