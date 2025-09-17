---
id: b2eabcd7dc
question: Docker - Setting up Docker on Mac
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 670
---

Check this article for details -

From researching it seems this method might be out of date, it seems that since docker changed their licensing model, the above is a bit hit and miss. What worked for me was to just go to the docker website and download their dmg. Haven’t had an issue with that method.

brew install conflict with docker desktop and command line tools. You need to install docker desktop first and then the command line tools. [Issue](https://github.com/Homebrew/brew/issues/16309)

brew install –cask docker

brew install docker docker-compose

