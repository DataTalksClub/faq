---
course: machine-learning-zoomcamp
id: 7e7931bff6
question: Errors with istio during installation
section: Projects (Midterm and Capstone)
sort_order: 3690
---

Problem description:

Running this:

curl -s "https://raw.githubusercontent.com/kserve/kserve/release-0.9/hack/quick_install.sh" | bash

Fails with errors because of istio failing to update resources, and you are on kubectl > 1.25.0.

Check kubectl version with kubectl version

Solution description

Edit the file “quick_install.bash” by downloading it with curl without running bash. Edit the versions of Istio and Knative as per the matrix on the .

Run the bash script now.

Added by Andrew Katoch

