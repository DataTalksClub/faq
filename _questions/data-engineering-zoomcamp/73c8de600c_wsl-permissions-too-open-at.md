---
id: 73c8de600c
question: WSL - Permissions too open at Windows
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 1040
---

Issue when trying to run the GPC VM through SSH through WSL2,  probably because WSL2 isn’t looking for .ssh keys in the correct folder. My case I was trying to run this command in the terminal and getting an error

PC:/mnt/c/Users/User/.ssh$ ssh -i gpc [username]@[my external IP]

You can try to use sudo before the command

Sudo .ssh$ ssh -i gpc [username]@[my external IP]

You can also try to cd to your folder and change the permissions for the private key SSH file.

chmod 600 gpc

If that doesn’t work, create a .ssh folder in the home diretory of WSL2 and copy the content of windows .ssh folder to that new folder.

cd ~

mkdir .ssh

cp -r /mnt/c/Users/YourUsername/.ssh/* ~/.ssh/

You might need to adjust the permissions of the files and folders in the .ssh directory.

