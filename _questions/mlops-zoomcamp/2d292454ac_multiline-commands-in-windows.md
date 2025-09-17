---
course: mlops-zoomcamp
id: 2d292454ac
question: Multiline commands in Windows Powershell
section: 'Module 4: Deployment'
sort_order: 1550
---

Use ` at the end of each line except the last. Note that multiline string does not need `.

Escape “ to “\ .

Use $env: to create env vars (non-persistent). E.g.:

$env:KINESIS_STREAM_INPUT="ride_events"

aws kinesis put-record --cli-binary-format raw-in-base64-out `

--stream-name $env:KINESIS_STREAM_INPUT `

--partition-key 1 `

--data '{

\"ride\": {

\"PULocationID\": 130,

\"DOLocationID\": 205,

\"trip_distance\": 3.66

},

\"ride_id\": 156

}'

Added by MarcosMJD

