---
course: mlops-zoomcamp
id: b395e1c5ec
question: 'I get below error invalid mount config for type "bind": invalid specification:
  destination can''t be ''/'' when running docker compose up when running mage'
section: 'Module 3: Orchestration'
sort_order: 1480
---

You should not run docker compose up for mage repo, should always use bash ./scripts/start.sh

A

>>> Update from another student of mlops zoomcamp: The start.sh script also runs docker compose up. And depending on how you start your mage project (like starting a fresh one in the capstone project), you may not have a start.sh or scripts directory. The most important thing about start.sh is that it sets the PROJECT_NAME and MAGE_CODE_PATH before executing docker compose up. These ENV variables can and probably should be set in your .env file.

Update added by Claudia van Dijk

