---
course: mlops-zoomcamp
id: 28676cfdf9
question: What version of Evidently AI is used in the course?
section: 'Module 5: Monitoring'
sort_order: 2190
---

In the video (current cohort: 2025) the Evidently used is 0.4.17, but any version up to 0.6.7 will be able to run the code in the video and the repo.

The newer versions have changed the APIs so the code in the video will not run.

Added by Thanh Trung Mai

Failed to create provisioner error when running docker-compose up –build

Error: ✗ Failed to create provisioner: Failed to read dashboards config: could not parse provisioning config file: dashboards.yaml error: read /etc/grafana/provisioning/dashboards/dashboards.yaml: is a directory

The docker-compose.yml file needs to be updated in grafana -> volumes from a YML file to a directory because docker-compose expects a directory but is instead given a file like in the example error above. Change /etc/grafana/provisioning/dashboards/dashboards.yaml to /etc/grafana/provisioning/dashboards/dashboards and do that for all other file names in grafana -> volumes.

