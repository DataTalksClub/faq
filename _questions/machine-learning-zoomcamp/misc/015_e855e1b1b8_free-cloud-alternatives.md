---
id: e855e1b1b8
question: 'Free / cheap cloud alternatives for deploying my Docker image'
sort_order: 15
---

If a small free-tier host like Render gives you `SIGTERM` errors, the container is most likely getting OOM-killed — 512 MB of RAM isn't enough for many ML images.

Cheaper / better-spec options:

- AWS — free-tier micro instances for the first 12 months, plus broader free quotas across services.
- GCP — similar free-tier micro instance, plus a one-time signup credit you can use for higher-spec instances.
- Fly.io / Railway / Hugging Face Spaces — small free tiers; Spaces is convenient if you only need to demo a model.
- Google Colab — runs the model in a notebook for free (not a deployment, but useful for sharing demos).

For Docker images, watch the memory footprint: shipping `tensorflow-cpu` instead of full `tensorflow`, or pruning unused dependencies from `requirements.txt`, often gets the image under the free-tier RAM limits.
