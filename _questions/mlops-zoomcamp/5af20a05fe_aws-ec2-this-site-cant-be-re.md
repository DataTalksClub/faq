---
course: mlops-zoomcamp
id: 5af20a05fe
question: 'AWS EC2: this site can’t be reached'
section: 'Module 1: Introduction'
sort_order: 380
---

When I click an open IP-address in an AWS EC2 instance I get an error: “This site can’t be reached”. What should I do?

This ip-address is not required to be open in a browser. It is needed to connect to the running EC2 instance via terminal from your local machine or via terminal from a remote server with such command, for example if:

ip-address is 11.111.11.111

downloaded key name is razer.pem (the key should be moved to a hidden folder .ssh)

your user name is user_name

ssh -i /Users/user_name/.ssh/razer.pem ubuntu@11.111.11.111

