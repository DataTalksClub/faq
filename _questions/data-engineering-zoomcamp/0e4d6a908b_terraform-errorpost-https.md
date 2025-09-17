---
course: data-engineering-zoomcamp
id: 0e4d6a908b
question: 'Terraform - Error:Post "https://storage.googleapis.com/storage/v1/b?alt=json&prettyPrint=false&project=coherent-ascent-379901":
  oauth2: cannot fetch token: Post "https://oauth2.googleapis.com/token": dial tcp
  172.217.163.42:443: i/o timeout'
section: 'Module 1: Docker and Terraform'
sort_order: 1620
---

The issue was with the network. Google is not accessible in my country, I am using a VPN. And The terminal program does not automatically follow the system proxy and requires separate proxy configuration settings.I opened a Enhanced Mode in Clash, which is a VPN app, and 'terraform apply' works! So if you encounter the same issue, you can ask help for your vpn provider.

