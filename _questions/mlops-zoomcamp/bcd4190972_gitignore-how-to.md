---
course: mlops-zoomcamp
id: bcd4190972
question: .gitignore how-to
section: 'Module 1: Introduction'
sort_order: 330
---

If you create a folder data and download datasets or raw files in your local repository. Then to push all your code to remote repository without this files or folder please use gitignore file. The simple way to create it do the following steps
1. Create empty .txt file (using text editor or command line)

2. Safe as .gitignore (. must use the dot symbol)

3. Add rules
 *.parquet - to ignore all parquet files

data/ - to ignore all files in folder data

For more pattern read GIT documentation

Added by Olga Rudakova (olgakurgan@gmail.com)

