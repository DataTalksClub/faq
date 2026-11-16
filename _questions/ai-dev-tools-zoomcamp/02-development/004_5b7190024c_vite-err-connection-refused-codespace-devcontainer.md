---
id: 5b7190024c
question: My Vite dev server answers curl inside my Codespace or dev container, but
  the browser on my own machine shows ERR_CONNECTION_REFUSED. Why?
sort_order: 4
---

When you work in a dev container (VS Code Dev Containers or a GitHub Codespace), your editor and terminal run inside the container. The port forward lets your browser on your machine reach the dev server inside the container.

That creates two different connection paths:
- `curl` *inside* the container connects directly to the server.
- your browser connection goes through port forwarding and typically reaches it via IPv4 (`127.0.0.1`).

If Vite is only listening on the IPv6 loopback address (`[::1]`), `curl http://localhost:5173` may work inside the container, but the forwarded IPv4 connection is refused. This can happen if Vite’s default `host` behavior resolves `localhost` to IPv6 first.

First, confirm the server is really running (and the port is forwarded) by checking the editor’s Ports tab. Then diagnose from inside the container (adjust the port if it isn’t `5173`):

```bash
curl http://127.0.0.1:5173     # should fail with connection refused if this is the IPv6-only problem
curl "http://[::1]:5173"       # should return 200 OK
ss -ltn | grep 5173            # shows which address/port the server is bound to
```

Fix: force Vite to bind to IPv4 loopback in `vite.config.ts`:

```ts
import { defineConfig } from 'vite'

export default defineConfig({
  server: {
    host: '127.0.0.1',
  },
})
```

Restart the dev server, and open `http://127.0.0.1:5173` in your browser (not `http://localhost:5173`, which may try IPv6 first).

As an alternative, you can set `host: '0.0.0.0'` (listens on all interfaces). Use this only if you need broader reachability, since it exposes the service on all container interfaces (within the limits of port forwarding). 

See Vite’s `server.host` option: https://vite.dev/config/server-options.html#server-host