---
id: 563feb7fd1
question: Mage updated in UI
section: Module 3: Orchestration
course: mlops-zoomcamp
sort_order: 1340
---

When you see the mage version change in the UI after you’ve started the container, and you want to update, follow these steps. Read the release notes first to see if there’s a fix that affected your work and would benefit from an update.

If you want to remain in the previous version is also fine; unless the fixes were specifically for our zoomcamp course-work (check slack and/or the repository for any new instructions or PRs added).

Close the browser page

In the terminal console, bring down the container `docker compose down`

Rebuild the container with new mage image `docker compose build --no-cache`

Verify that you see `[magic-platform 1/4] FROM docker.io/mageai/mageai:alpha` meaning that the container is being rebuild with a new version

If the image is not updated, ctrl+c to cancel the process and pull the image manually with `docker pull mageai/mageai:alpha` then rebuild

Then restart the docker container with `./scripts/start.sh` as before

ps: this is the same sequence of steps if you want to switch to the latest tagged image instead of using the alpha image.

What does alpha and latest mean?

Latest is the fully released version ready for production use, and it has gone through verification, testing, QA and whatever else the release cycle entails.

Alpha is the potentially buggy version with fresh new fixes and newly added features; but not yet put through the full beta test (if there’s one), integration testing and other QA steps. So expect issues to occur.

