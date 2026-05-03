---
id: a01ea88b00
question: REST API pagination should start at page 1 and stop when the API returns
  an empty list
sort_order: 15
---

Problem:
- Some REST APIs paginate results using a page parameter where valid pages start at 1. Using page=0 can return an empty list, leading to incomplete ingestion.

Best practice:
- Start from page=1
- Continuously request subsequent pages until the API returns an empty list
- Do not rely on page=0 to fetch data; always test the API behaviour manually before implementing pagination logic

Implementation example (Python):
```python
import requests

def fetch_all_pages(base_url, start_page=1, per_page=None):
    page = start_page
    all_items = []
    while True:
        params = {'page': page}
        if per_page is not None:
            params['per_page'] = per_page
        resp = requests.get(base_url, params=params)
        resp.raise_for_status()
        data = resp.json()
        if not data:
            break
        all_items.extend(data)
        page += 1
    return all_items
```

Manual testing steps:
- Call the endpoint with page=1 and verify that data is returned.
- Call the endpoint with page=0 and verify that it returns an empty list ([]).
- Increment the page number (2, 3, ...) until an empty list is returned, confirming ingestion completes when no more data is available.
- Add a note to adjust parameter names (e.g., per_page) if the API uses a different paging scheme.

Notes:
- If the API uses a different paging convention (e.g., cursor-based, or a different param name), adapt the logic accordingly while preserving the core rule: start at the initial page and stop when there is no data returned.
- Consider adding small unit/integration tests that mock API responses to verify this paging behavior in automated tests.
