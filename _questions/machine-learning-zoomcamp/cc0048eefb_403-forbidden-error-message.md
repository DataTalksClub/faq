---
id: cc0048eefb
question: '403 Forbidden' error message when you try to push to a GitHub repository
section: 1. Introduction to Machine Learning
course: machine-learning-zoomcamp
sort_order: 340
---

Type the following command:

git config -l | grep url

The output should look like this:

remote.origin.url=

Change this to the following format and make sure the change is reflected using command in step 1:

git remote set-url origin "https://github-username@github.com/github-username/github-repository-name.git"

(Added by Dheeraj Karra)

