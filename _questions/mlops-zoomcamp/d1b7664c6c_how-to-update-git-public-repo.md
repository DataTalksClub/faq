---
id: d1b7664c6c
question: How to Update Git Public Repo Without Overwriting Changes
section: Module 2: Experiment tracking
course: mlops-zoomcamp
sort_order: 880
---

Problem: I cloned the public repo, made edits, committed and pushed them to my own repo. Now I want to get the recent commits from the public repo without overwriting my own changes to my own repo. Which command(s) should I use?

This is what my config looks like (in case this might be useful):

[core]

repositoryformatversion = 0

filemode = true

bare = false

logallrefupdates = true

ignorecase = true

precomposeunicode = true

[remote "origin"]

url = git@github.com:my_username/mlops-zoomcamp.git

fetch = +refs/heads/*:refs/remotes/origin/*

[branch "main"]

remote = origin

merge = refs/heads/main

Solution: You should fork DataClubsTak’s repo instead of cloning it. On GitHub, click “Fetch and Merge” under the menu “Fetch upstream” at the main page of your own

