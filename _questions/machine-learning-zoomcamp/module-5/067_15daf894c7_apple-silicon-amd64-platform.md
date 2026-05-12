---
id: 15daf894c7
question: 'Apple Silicon (M1/M2/M3): docker run says ''requested image''s platform (linux/amd64) does not match'' or container fails with executable not found'
sort_order: 67
---

The base image is built for amd64, but your Mac is arm64. Force the platform on both build and run:

```bash
docker build --platform linux/amd64 -t my-image .
docker run --platform linux/amd64 -p 9696:9696 my-image
```

Or set `--platform=linux/amd64` in the `FROM` line of your Dockerfile so it's always applied.

If the image still won't run after that, GitHub Codespaces (which is amd64 native) is the simplest workaround.
