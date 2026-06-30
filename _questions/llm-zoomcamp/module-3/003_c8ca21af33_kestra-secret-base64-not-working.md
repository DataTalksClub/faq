---
id: c8ca21af33
question: I set SECRET_GEMINI_API_KEY but my Kestra flow still fails with an invalid/missing
  key — what's wrong?
sort_order: 3
---

The most common cause is a corrupted base64 value. If you encode the key with a trailing space or newline, the decoded secret is wrong and authentication fails.

Use `echo -n` (which omits the trailing newline) and quote the value:

```bash
export SECRET_GEMINI_API_KEY=$(echo -n "$GEMINI_API_KEY" | base64)
```

Other things to check:

- You must **restart** Kestra after exporting, so the container picks up the new variables: `docker compose up -d` (or `docker compose down && docker compose up -d`).
- Reference the secret in flows **without** the `SECRET_` prefix: `{{ secret('GEMINI_API_KEY') }}`.
- Export the variables in the same shell session you start Kestra from.

A cleaner alternative is to put the keys in a `.env` file and pass it explicitly:

```bash
docker compose --env-file ./.env -f ./docker-compose.yml up -d
```
