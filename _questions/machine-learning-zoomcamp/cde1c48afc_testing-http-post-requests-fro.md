---
id: cde1c48afc
question: Testing HTTP POST requests from command line using curl
section: 5. Deploying Machine Learning Models
course: machine-learning-zoomcamp
sort_order: 2200
---

I wanted to have a fast and simple way to check if the HTTP POST requests are working just running a request from command line. This can be done running ‘curl’. 
(Used with WSL2 on Windows, should also work on Linux and MacOS)

curl --json '<json data>' <url>

# piping the structure to the command

cat <json file path> | curl --json @- <url>

echo '<json data>' | curl --json @- <url>

# example using piping

echo '{"job": "retired", "duration": 445, "poutcome": "success"}'\

| curl --json @- http://localhost:9696/predict

Added by Sylvia Schmitt

