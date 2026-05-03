---
id: 4f1fe161b1
question: 'Environment: which OS / cloud / dev setup should I use? (local vs GCP VM
  vs Codespaces, AWS alternative, OS support)'
sort_order: 2
---

## OS support

Linux is the smoothest, but the course works on macOS and Windows too. Students in the most recent cohorts have completed it on all three. Windows users typically need WSL2 to avoid friction with shell scripts in later modules.

## Where to run the course

You have three good options. Pick whichever suits you:

1. Local machine (laptop / PC). Easiest if you're already comfortable with Docker locally. Windows users should use WSL2 from the start.
2. GitHub Codespaces. A free Linux dev environment with Docker, Python, and many CLI tools pre-installed. Useful if your laptop is underpowered, or if you switch between home and office machines. Ports for things like Kestra/pgAdmin are exposed via Codespaces' forwarded URL — not `http://localhost`.
3. Google Cloud VM. The course videos demonstrate this setup. Useful if you want a persistent remote environment to SSH into, especially while staying logged in across machines.

You don't need both Codespaces and a GCP VM — pick one. You will need a GCP account regardless because the course uses BigQuery (in Module 3 and the project), but GCP for compute is optional.

## Can I use AWS / Snowflake / Azure / a different stack?

Yes. The capstone project is graded on creating a data pipeline and producing a visualization — it doesn't mandate any specific cloud. Considerations:

- The lessons are recorded against GCP, so you'll need to translate steps yourself.
- You may need to explain your choice during peer review.
- Fewer fellow students will be using AWS/Azure, so help in Slack may be slower.

If you only want to run the course locally without any cloud, you can do that for everything except Module 3's BigQuery homework, which requires GCP.

## Is the course Windows / macOS / Linux friendly?

All three work. Linux is best by default. On Windows, install WSL2 and run everything inside a WSL distro — Git Bash and MINGW64 are not always sufficient for shell scripts later in the course.
