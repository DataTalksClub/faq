---
id: 4f1fe161b1
question: 'Where should I run the course: local machine, GitHub Codespaces, or a
  GCP VM?'
sort_order: 2
---

You have three good options. Pick whichever suits you:

1. Local machine (laptop / PC). Easiest if you're already comfortable with Docker locally. Windows users should use WSL2 from the start.
2. GitHub Codespaces. A free Linux dev environment with Docker, Python, and many CLI tools pre-installed. Useful if your laptop is underpowered, or if you switch between home and office machines. Ports for things like Kestra/pgAdmin are exposed via Codespaces' forwarded URL — not `http://localhost`.
3. Google Cloud VM. The course videos demonstrate this setup. Useful if you want a persistent remote environment to SSH into, especially while staying logged in across machines.

You don't need both Codespaces and a GCP VM — pick one. You will need a GCP account regardless because the course uses BigQuery (in Module 3 and the project), but GCP for compute is optional.
