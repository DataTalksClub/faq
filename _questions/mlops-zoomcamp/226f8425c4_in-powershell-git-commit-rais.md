---
course: mlops-zoomcamp
id: 226f8425c4
question: In Powershell, Git commit raises utf-8 encoding error after creating pre-commit
  yaml file
section: 'Module 6: Best practices'
sort_order: 2280
---

Problem description

git commit -m 'Updated xxxxxx'

An error has occurred: InvalidConfigError:

==> File .pre-commit-config.yaml

=====> 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte

Solution description

Set uft-8 encoding when creating the pre-commit yaml file:

pre-commit sample-config | out-file .pre-commit-config.yaml -encoding utf8

Added by MarcosMJD

