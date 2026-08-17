---
id: 5b343ea5b3
question: Why did Render deploy the wrong service from my multi-stage Dockerfile?
sort_order: 16
---

When you build a multi-stage `Dockerfile`, Render effectively performs a target-less build (no `--target`), so the image it runs is whatever stage is declared last in the file.

If your `Dockerfile` has multiple stages (e.g., a `ui` stage and an `api` stage that share a base), ensure the service you actually want deployed is the last stage.

Key points:
- Keep the desired runtime stage (the one that should be deployed) as the last `FROM ... AS <stage>` in the `Dockerfile`.
- If you later append a new stage below it, Render may silently switch which stage gets built and shipped (build can still succeed, just with the wrong service).
- This discrepancy often only shows up on Render because `docker-compose` can set `target: ...` per service.
- Verify which service Render actually deployed by hitting a route that is unique to that service, not a shared endpoint like `/health` that both services might implement.

Quick local check before pushing:
```bash
docker build -t check .   # same as Render: no --target
docker run --rm -p 8010:8000 -e POSTGRES_URL=... check
curl -s localhost:8010/health
```

To prevent future edits from reintroducing the problem, you can add a comment above the intended last stage reminding not to append anything below it.