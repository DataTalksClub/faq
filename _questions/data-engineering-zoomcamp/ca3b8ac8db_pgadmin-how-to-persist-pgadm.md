---
id: ca3b8ac8db
question: pgAdmin - How to Persist pgAdmin Configurations
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 1280
---

Question: How can I keep pgAdmin settings after restarting the container?

Answer: Create a directory, map it to /var/lib/pgadmin, and fix permissions:

Create the directory for pgAdmin data:
# mkdir -p /path/to/pgadmin-data

Assign ownership to pgAdmin's user (ID 5050):
# sudo chown -R 5050:5050 /path/to/pgadmin-data

# sudo chmod -R 755 /path/to/pgadmin-data

