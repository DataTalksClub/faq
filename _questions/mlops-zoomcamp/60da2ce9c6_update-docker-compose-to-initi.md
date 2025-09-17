---
id: 60da2ce9c6
question: Update docker-compose to initiate Mage
section: Module 3: Orchestration
course: mlops-zoomcamp
sort_order: 1310
---

When running ./scripts/start.sh - it returns below error

ERROR: The Compose file './docker-compose.yml' is invalid because:

Unsupported config option for networks: 'app-network'

Unsupported config option for services: 'magic-platform'

Solution description

# Download the latest version of Docker Compose

sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Apply executable permissions to the binary

sudo chmod +x /usr/local/bin/docker-compose

(optional) Artur G

