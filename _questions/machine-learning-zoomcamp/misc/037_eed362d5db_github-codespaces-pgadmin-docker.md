---
id: eed362d5db
question: 'GitHub Codespaces: pgAdmin in Docker shows a blank screen after login'
sort_order: 37
---

Running pgAdmin in Docker behind GitHub Codespaces reverse proxy can result in a blank screen after logging in. This is typically due to session or proxy issues when running behind Codespaces’ reverse proxy. Resolve with two options:

Option 1: Set the following environment variables to configure the proxy handling:

- `PGADMIN_CONFIG_PROXY_X_HOST_COUNT`: 1
- `PGADMIN_CONFIG_PROXY_X_PREFIX_COUNT`: 1

This allows pgAdmin to work properly with Codespaces’ reverse proxy.

If the gray screen persists, you can try disabling enhanced cookie protection and CSRF checks, and adjusting cookie settings:

- `PGADMIN_CONFIG_ENHANCED_COOKIE_PROTECTION`: "False"
- `PGADMIN_CONFIG_WTF_CSRF_CHECK_DEFAULT`: "False"
- `PGADMIN_CONFIG_WTF_CSRF_ENABLED`: "False"
- `PGADMIN_CONFIG_SESSION_COOKIE_SAMESITE`: "'None'"
- `PGADMIN_CONFIG_SESSION_COOKIE_SECURE`: "True"

This configuration relaxes session and CSRF settings and is known to resolve rendering issues when using pgAdmin in Docker inside Codespaces.

- Option 1 is safer as it preserves CSRF protection.
- Option 2 should be used only if the blank screen persists after Option 1.

Always restart the pgAdmin container after changing environment variables.