---
id: 5d92a0583a
question: 'When configuring the profiles.yml file for dbt-postgres with jinja templates
  with environment variables, I''m getting "Credentials in profile \"PROFILE_NAME\",
  target: ''dev'', invalid: ''5432'' is not of type ''integer''"'
sort_order: 58
---

Make sure that the port number is set as an integer in your `profiles.yml` file. Environment variables are usually strings, so you need to explicitly convert them to integers in Jinja. Update the line that sets the port with something like:

```yaml
port: {{ env_var('DB_PORT') | int }}
```

This will ensure that the value is treated as an integer.