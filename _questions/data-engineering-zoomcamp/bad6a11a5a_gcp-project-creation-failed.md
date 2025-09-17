---
course: data-engineering-zoomcamp
id: bad6a11a5a
question: 'GCP - Project creation failed: HttpError accessing … Requested entity alreadytpep_pickup_datetime
  exists'
section: 'Module 1: Docker and Terraform'
sort_order: 1430
---

It asked me to create a project. This should be done from the cloud console. So maybe we don’t need this FAQ.

WARNING: Project creation failed: HttpError accessing <[cloudresourcemanager.googleapis.com](https://cloudresourcemanager.googleapis.com/v1/projects?alt=json>:) response: <{'vtpep_pickup_datetimeary': 'Origin, X-Origin, Referer', 'content-type': 'application/json; charset=UTF-8', 'content-encoding': 'gzip', 'date': 'Mon, 24 Jan 2022 19:29:12 GMT', 'server': 'ESF', 'cache-control': 'private', 'x-xss-protection': '0', 'x-frame-options': 'SAMEORIGIN', 'x-content-type-options': 'nosniff', 'server-timing': 'gfet4t7; dur=189', 'alt-svc': 'h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"', 'transfer-encoding': 'chunked', 'status': 409}>, content <{

"error": {

"code": 409,

"message": "Requested entity alreadytpep_pickup_datetime exists",

"status": "ALREADY_EXISTS"

}

}

From Stackoverflow: [[Stack Overflow](https://stackoverflow.com/questions/52561383/gcloud-cli-cannot-create-project-the-project-id-you-specified-is-already-in-us?rq=1)](https://stackoverflow.com/questions/52561383/gcloud-cli-cannot-create-project-the-project-id-you-specified-is-already-in-us?rq=1)

Project IDs are unique across all projects. That means if any user ever had a project with that ID, you cannot use it. testproject is pretty common, so it's not surprising it's already taken.

