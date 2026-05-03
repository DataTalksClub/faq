---
id: 3d24f7796d
question: 'GitHub Codespaces: Running pgadmin in Docker'
sort_order: 12
---

Running pgAdmin in Docker behind GitHub Codespaces reverse proxy can result in a blank screen after logging in. This is typically due to session or proxy issues when running behind Codespaces' reverse proxy. Resolve with two options:

**Option 1**: Set the following environment variables to configure the proxy handling:

```plaintext
PGADMIN_CONFIG_PROXY_X_HOST_COUNT: 1
PGADMIN_CONFIG_PROXY_X_PREFIX_COUNT: 1
```

This allows pgAdmin to work properly with Codespaces' reverse proxy.

**Option 2** (if the gray screen persists): Try disabling enhanced cookie protection and CSRF checks, and adjusting cookie settings:

```plaintext
PGADMIN_CONFIG_ENHANCED_COOKIE_PROTECTION: "False"
PGADMIN_CONFIG_WTF_CSRF_CHECK_DEFAULT: "False"
PGADMIN_CONFIG_WTF_CSRF_ENABLED: "False"
PGADMIN_CONFIG_SESSION_COOKIE_SAMESITE: "'None'"
PGADMIN_CONFIG_SESSION_COOKIE_SECURE: "True"
```

This configuration relaxes session and CSRF settings and is known to resolve rendering issues when using pgAdmin in Docker inside Codespaces.

**Notes**:
- Option 1 is safer as it preserves CSRF protection.
- Option 2 should be used only if the blank screen persists after Option 1.
- Always restart the pgAdmin container after changing environment variables.
