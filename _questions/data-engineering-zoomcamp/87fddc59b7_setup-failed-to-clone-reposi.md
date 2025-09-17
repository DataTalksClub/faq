---
course: data-engineering-zoomcamp
id: 87fddc59b7
question: Setup - Failed to clone repository.
section: 'Module 4: analytics engineering with dbt'
sort_order: 2480
---

Error: Failed to clone repository.

git clone git@github.com:DataTalksClub/data-engineering-zoomcamp.git /usr/src/develop/…

Cloning into '/usr/src/develop/...

Warning: Permanently added ',140.82.114.4' (ECDSA) to the list of known hosts.

git@github.com: Permission denied (publickey).

fatal: Could not read from remote repository.

Issue: You don’t have permissions to write to DataTalksClub/data-engineering-zoomcamp.git

Solution 1: Clone the repository and use this forked repo, which contains your github username. Then, proceed to specify the path, as in:

[your github username]/data-engineering-zoomcamp.git

Solution 2: create a fresh repo for dbt-lessons. We’d need to do branching and PRs in this lesson, so it might be a good idea to also not mess up your whole other repo. Then you don’t have to create a subfolder for the dbt project files

Solution 3: Use https link

