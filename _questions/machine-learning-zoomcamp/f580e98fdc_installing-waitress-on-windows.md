---
course: machine-learning-zoomcamp
id: f580e98fdc
question: 'Installing waitress on Windows via GitBash: “waitress-serve” command not
  found'
section: 5. Deploying Machine Learning Models
sort_order: 2150
---

Running 'pip install waitress' as a command on GitBash was not downloading the executable file 'waitress-serve.exe'. You need this file to be able to run commands with waitress in Git Bash. To solve this:

open a Jupyter notebook and run the same command ' pip install waitress'. This way the executable file will be downloaded. The notebook may give you this warning : 'WARNING: The script waitress-serve.exe is installed in 'c:\Users\....\anaconda3\Scripts' which is not on PATH. Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.'

Add the path where 'waitress-serve.exe' is installed into gitbash's PATH as such:

enter the following command in gitbash: nano ~/.bashrc

add the path to 'waitress-serve.exe' to PATH using this command: export PATH="/path/to/waitress:$PATH"

close gitbash and open it again and you should be good to go

Added by Bachar Kabalan

