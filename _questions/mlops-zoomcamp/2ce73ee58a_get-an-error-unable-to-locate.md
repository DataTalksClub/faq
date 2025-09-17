---
course: mlops-zoomcamp
id: 2ce73ee58a
question: Get an error ‘Unable to locate credentials’ after running localstack with
  kinesis
section: 'Module 6: Best practices'
sort_order: 2220
---

You may get an error ‘{'errorMessage': 'Unable to locate credentials', …’ from the print statement in test_docker.py after running localstack with kinesis.

To fix this, in the docker-compose.yaml file, in addition to the environment variables like AWS_DEFAULT_REGION, add two other variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. Their value is not important; anything like abc will suffice

Added by M

Other possibility is just to run

aws --endpoint-url http://localhost:4566 configure

And providing random values for AWS Access Key ID , AWS Secret Access Key, Default region name, and Default output format.

Added by M.A. Monjas

