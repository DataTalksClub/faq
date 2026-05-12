---
id: cde1c48afc
question: Testing HTTP POST requests from command line using curl
sort_order: 39
---

I wanted to have a fast and simple way to check if the HTTP POST requests are working just by running a request from the command line. This can be done using `curl`. (Used with WSL2 on Windows; should also work on Linux and MacOS)

```bash
curl --json '<json data>' <url>
```

Piping the structure to the command:

```bash
cat <json file path> | curl --json @- <url>
echo '<json data>' | curl --json @- <url>
```

Example using piping:

```bash
echo '{"job": "retired", "duration": 445, "poutcome": "success"}' \
| curl --json @- http://localhost:9696/predict
```
