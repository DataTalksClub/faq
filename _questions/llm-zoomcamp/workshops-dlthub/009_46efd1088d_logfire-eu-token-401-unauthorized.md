---
id: 46efd1088d
question: "Why does my EU-region Logfire token return 401 Unauthorized?"
sort_order: 9
---

Current Logfire SDK versions normally infer the region from the write token, so
an EU token should work with `logfire.configure()` without a manually configured
base URL. A `401 Unauthorized` usually means the process loaded the wrong token
or did not load the intended `.env` value.

Check the configuration in this order:

1. Call `load_dotenv()` before `logfire.configure()`.
2. Make sure `LOGFIRE_TOKEN` is a **write token** from the intended project;
   `LOGFIRE_READ_TOKEN` is only for reading traces.
3. Check for an older `LOGFIRE_TOKEN` already exported by the shell. By default,
   `load_dotenv()` does not replace an existing environment variable. Use
   `load_dotenv(override=True)` when the local `.env` should take precedence.
4. Upgrade the SDK with `uv add --upgrade logfire` so token-based region
   detection is current.

If an older client still sends an EU token to the wrong region, explicitly
setting `LOGFIRE_BASE_URL=https://logfire-eu.pydantic.dev` can be used as a
fallback. The token and endpoint must belong to the same region, but this manual
setting should not be necessary with the current SDK.

See Logfire's documentation for
[SDK configuration](https://logfire.pydantic.dev/docs/reference/configuration/)
and [data-region URLs](https://logfire.pydantic.dev/docs/reference/data-regions/).
