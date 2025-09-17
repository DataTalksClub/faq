---
id: e04431f782
question: Unprotected private key file!
section: Module 1: Introduction
course: mlops-zoomcamp
sort_order: 390
---

After this command `ssh -i ~/.ssh/razer.pem ubuntu@XX.XX.XX.XX` I got this error: "unprotected private key file". This page () explains how to fix this error. Basically you need to change the file permissions of the key file with this command: chmod 400 ~/.ssh/razer.pem

