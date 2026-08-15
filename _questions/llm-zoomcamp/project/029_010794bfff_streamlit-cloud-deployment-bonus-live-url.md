---
id: 010794bfff
question: How do I deploy my Streamlit app to the cloud and get the live URL for the
  Cloud Deployment bonus?
sort_order: 29
---

The +2 Cloud Deployment bonus requires a public URL reviewers can open. Because Streamlit is a long-running server, static landing hosts (Vercel, Netlify, GitHub Pages) can show a static page but cannot run `streamlit run` (so you also can’t rely on them to run Postgres/Grafana).

Working options:
1) GCP Cloud Run (serverless containers). This is also scriptable with Terraform.
2) Render. Connect your GitHub repo as a Blueprint (`render.yaml`); Render can build your Dockerfile automatically—typically the easiest.
3) Fly.io. Use `fly launch --no-deploy` and then `fly deploy`.

If you go with GCP Cloud Run + Terraform, the basic flow is:
- Login: `gcloud auth application-default login`
- Build/push an image: `gcloud builds submit --tag us-central1-docker.pkg.dev/<PROJECT>/complaintradar/app:latest .`
- Deploy: `cd terraform && terraform init && terraform apply`
- Read the service URL from `terraform output cloud_run_service_url`

The resulting URL will look like `https://<service>-<hash>-uc.a.run.app`.