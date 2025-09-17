---
id: b3030c88e7
question: wget is not recognized as an internal or external command
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 520
---

“wget is not recognized as an internal or external command”, you need to install it.

“​​No such file or directory: 'output.csv.gz'”, may also caused by wget not recognized

. 
On Ubuntu, run:

$ sudo apt-get install wget

On MacOS, the easiest way to install wget is to use :

$ brew install wget

On Windows, the easiest way to install wget is to use :

$ choco install wget
Or you can download a binary (https://gnuwin32.sourceforge.net/packages/wget.htm) and put it to any location in your PATH (e.g. C:/tools/)

Also, you can following this step to install Wget on MS Windows

* Download the latest wget binary for windows from [eternallybored] (https://eternallybored.org/misc/wget/) (they are available as a zip with documentation, or just an exe)

* If you downloaded the zip, extract all (if windows built in zip utility gives an error, use [7-zip] (https://7-zip.org/)).

* Rename the file `wget64.exe` to `wget.exe` if necessary.

* Move wget.exe to your `Git\mingw64\bin\`.

Alternatively, you can use a Python wget library, but instead of simply using “wget” you’ll need to use 
python -m wget

You need to install it with pip first:

pip install wget

Alternatively, you can just paste the file URL into your web browser and download the file normally that way. You’ll want to move the resulting file into your working directory.

Also recommended a look at the python library requests for the loading gz file

