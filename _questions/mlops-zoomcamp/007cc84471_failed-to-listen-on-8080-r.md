---
id: 007cc84471
question: Failed to listen on :::8080 (reason: php_network_getaddresses: getaddrinfo failed: Address family for hostname not supported)
section: Module 5: Monitoring
course: mlops-zoomcamp
sort_order: 2040
---

Problem: when run docker-compose up –build, you may see this error. To solve, add `command: php -S 0.0.0.0:8080 -t /var/www/html` in adminer block in yml file like:

adminer:

command: php -S 0.0.0.0:8080 -t /var/www/html

image: adminer
…

Ilnaz Salimov

