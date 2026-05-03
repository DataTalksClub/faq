---
id: bad6a11a5a
question: 'GCP: Project creation failed: HttpError accessing … Requested entity already
  exists'
sort_order: 3
---

When creating a project in GCP, you may encounter the following error:

```json
WARNING: Project creation failed: HttpError accessing cloudresourcemanager.googleapis.com: response: {
  'content-type': 'application/json; charset=UTF-8',
  'status': 409
}, content {
  "error": {
    "code": 409,
    "message": "Requested entity already exists",
    "status": "ALREADY_EXISTS"
  }
}
```

### Explanation

This error occurs when the project ID you are trying to use is already taken. Project IDs are unique across all GCP projects. If any user ever had a project with that ID, you cannot use it.

### Solution

- Choose a different, more unique project ID. Avoid common names like `testproject` as they are likely to be already in use.

For more details, refer to the discussion: [Stack Overflow](https://stackoverflow.com/questions/52561383/gcloud-cli-cannot-create-project-the-project-id-you-specified-is-already-in-us?rq=1)