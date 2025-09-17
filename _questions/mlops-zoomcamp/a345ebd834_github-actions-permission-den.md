---
course: mlops-zoomcamp
id: a345ebd834
question: 'Github actions: Permission denied error when executing script file'
section: 'Module 6: Best practices'
sort_order: 2320
---

Problem description

This is the step in the ci yml file definition:

- name: Run Unit Tests

working-directory: "sources"

run: ./tests/unit_tests/run.sh

When executing github ci action, error raises:

…/tests/unit_test/run.sh Permission error

Error: Process completed with error code 126

Solution description

Add execution  permission to the script and commit+push:

git update-index --chmod=+x .\sources\tests\unit_tests\run.sh

Added by MarcosMJD

