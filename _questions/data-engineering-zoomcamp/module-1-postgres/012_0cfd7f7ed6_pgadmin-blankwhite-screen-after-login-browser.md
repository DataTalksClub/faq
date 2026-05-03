---
id: 0cfd7f7ed6
question: 'pgAdmin: CSRF session token is missing error – how to fix in a Docker setup?'
sort_order: 12
---

The CSRF session token missing error usually indicates CSRF protection is out of sync between the client and server. If you’re running pgAdmin in Docker, you can fix this with a combination of quick browser steps and container configuration changes. 

Immediate browser fixes
- Refresh the page (F5, Ctrl+Shift+R, or Cmd+Shift+R) to regenerate cookies and obtain a new CSRF token.
- Clear the site's cookies/cache for pgAdmin in your browser settings.
- Try an Incognito/Private window to avoid cached credentials.

Docker configuration fixes (apply in your docker-compose.yaml or via environment vars, then restart the container)
- Add these environment variables to the pgAdmin service:
```
- PGADMIN_DEFAULT_EMAIL=admin@admin.com
- PGADMIN_DEFAULT_PASSWORD=root
- PGADMIN_CONFIG_ENHANCED_COOKIE_PROTECTION=False
- PGADMIN_CONFIG_WTF_CSRF_ENABLED=False
- PGADMIN_CONFIG_WTF_CSRF_CHECK_DEFAULT=False
- PGADMIN_CONFIG_SESSION_COOKIE_SAMESITE='Lax'
- PGADMIN_CONFIG_SESSION_COOKIE_SECURE=False
```
- Then recreate containers:
```
docker compose down -v
docker compose up -d --force-recreate
```

Notes
- Disabling CSRF protection reduces security; use these settings for development or debugging. When possible, fix the underlying cause and re-enable CSRF protections for production environments.
- If you already have a working setup, ensure that your environment variables are applied to the running container and that you’re reconnecting to the correct pgAdmin instance.
