---
id: 0d6d4dbe6c
question: Why do I get 502 Bad Gateway for /api after restarting the backend container
  in Docker Compose (nginx proxy)?
sort_order: 5
---

This usually happens because nginx resolves a plain upstream hostname (like `backend`) only once when the nginx worker starts, and then keeps using the old IP. If Docker Compose recreates the backend container, it can get a new IP, so nginx keeps proxying to the dead address and returns `502`.

To fix it, make nginx re-resolve the backend name at request time.

1. Add a `resolver` to your nginx config:
- Use Docker's embedded DNS by adding a `resolver ${NGINX_LOCAL_RESOLVERS} valid=10s ipv6=off;` line (or equivalent).

2. Make `proxy_pass` use a variable so nginx doesn't treat it as a static upstream:
- For example: `set $backend_upstream "${BACKEND_URL}";` then `proxy_pass $backend_upstream;`

3. Use the nginx image's entrypoint template variables (template-based config) so the resolver environment variable is available at startup:
- Set `NGINX_ENTRYPOINT_LOCAL_RESOLVERS=1` in the Dockerfile and put your config in `/etc/nginx/templates/default.conf.template`.

Two common gotchas:
- Trailing slash behavior: with `proxy_pass` using a variable and no path after the host, nginx won't automatically strip the `/api/` prefix the way `proxy_pass http://backend:8000/;` used to. If your backend routes expect a different path, add a `rewrite` or adjust backend routes.
- Cloud URLs with TLS: if `BACKEND_URL` is an `https://...` URL (e.g., Cloud Run), keep `proxy_ssl_server_name on` and set `Host $proxy_host` so TLS/SNI and routing work.

Quick check:
- Restart only the backend (`docker compose restart backend`). Call the API through nginx (e.g. `curl -s localhost:8080/api/health`). After the resolver change, it should recover within ~10 seconds without restarting the frontend.
