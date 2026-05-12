---
id: 34d0aaa13e
question: 'Docker: Running out of storage after building many docker images'
sort_order: 15
---


Due to experimenting extensively, I ran out of storage on my 30-GB AWS instance. Removing empty directories did not resolve the issue as those primarily contained code, which did not occupy much space.


1. **Check Existing Images:**
   - Use the following command to list all Docker images:
     
     ```bash
     docker images
     ```
   
   - This showed over 20 GBs of superseded or duplicate models.

2. **Remove Unnecessary Images:**
   - Remove unwanted images using:
     
     ```bash
     docker rmi <image_id>
     ```
   
   - However, this did not free up space as anticipated.

3. **Free Up Space:**
   - To actually free up storage, execute:
     
     ```bash
     docker system prune
     ```


For more details on why this happens, see: [Stack Overflow Discussion](https://stackoverflow.com/questions/36799718/why-removing-docker-containers-and-images-does-not-free-up-storage-space-on-wind)