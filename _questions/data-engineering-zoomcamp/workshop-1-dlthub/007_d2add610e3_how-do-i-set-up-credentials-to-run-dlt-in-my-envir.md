---
id: d2add610e3
question: How do I set up credentials to run dlt in my environment (not Google Colab)?
sort_order: 7
---

You can set up credentials for `dlt` in several ways. Here are the two most common methods:

### Environment Variables (Easiest)

Set credentials via environment variables. For example, to configure Google Cloud credentials. This method avoids hardcoding secrets in your code and works seamlessly with most environments.

### Configuration Files (Recommended for Local Use)

- Use `.dlt/secrets.toml` for sensitive credentials and `.dlt/config.toml` for non-sensitive configurations.
- Example for Google Cloud in `secrets.toml`:

```toml
[google_cloud]
service_account_key = "YOUR_SERVICE_ACCOUNT_KEY"
```

- Place these files in the `.dlt` folder of your project.

### Additional Notes:

- Never commit `secrets.toml` to version control (add it to `.gitignore`).
- Credentials can also be loaded via vaults, AWS Parameter Store, or custom setups.

For additional methods and detailed information, refer to the [official dlt documentation](https://dlthub.com/docs/general-usage/credentials/)