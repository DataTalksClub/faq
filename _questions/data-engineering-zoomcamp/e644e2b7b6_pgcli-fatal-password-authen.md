---
id: e644e2b7b6
question: PGCLI - FATAL: password authentication failed for user "root" (You already have Postgres)
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 1080
---

For a more visual and detailed explanation, feel free to check the video

If you want to debug: the following can help (on a MacOS)

To find out if something is blocking your port (on a MacOS):

You can use the lsof command to find out which application is using a specific port on your local machine. `lsof -i :5432`wi

Or list the running postgres services on your local machine with launchctl

To unload the running service on your local machine (on a MacOS):

unload the launch agent for the PostgreSQL service, which will stop the service and free up the port  
`launchctl unload -w ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist`

this one to start it again
`launchctl load -w ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist`

Changing port from 5432:5432 to 5431:5432 helped me to avoid this error.

