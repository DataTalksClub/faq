---
id: 0dfba07ace
question: 'Notebook does not have secret access or 401 Client Error: Unauthorized
  for url: [api.notion.com](https://api.notion.com/v1/search)'
sort_order: 7
---

If you encounter this error, it typically indicates an authorization issue with the Notion API. Here’s how you can resolve it:

1. **Check API Key**: Ensure that you are using the correct API key with appropriate permissions.
2. **Verify API Endpoint**: Confirm that you are hitting the correct Notion API endpoint.
3. **Token Expiry**: Check if your token has expired and regenerate it if necessary.
4. **Configurations**: Double-check all access configurations in your application.

If the error persists, review the API documentation and make sure all necessary authentication steps are correctly implemented.