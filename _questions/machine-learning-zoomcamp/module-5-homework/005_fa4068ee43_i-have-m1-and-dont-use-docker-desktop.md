---
id: fa4068ee43
question: 'I have M1 and don''t use Docker Desktop.'
sort_order: 5
---


- If you replaced Docker Desktop with 'lima', you can create an instance of Lima using the [following template](https://gist.github.com/akrylysov/7c1ea3bac409da2758e525f2f82e6373). Follow the instructions listed on the page to create an instance using the supplied template.
- Switch your current Docker context to the context associated with this new (running) image.
- Use `svizor/zoomcamp-model:3.11.5-slim` as a base image and run your built image without issues.

Simple Solution:

- Specify the platform:

  ```bash
  docker run --platform linux/amd64 -it --rm -p 9696:9696 <your-docker-image-name>
  ```