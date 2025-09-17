---
course: data-engineering-zoomcamp
id: eb759226aa
question: GCP - ssh public key error - multiple users / usernames
section: 'Module 1: Docker and Terraform'
sort_order: 1490
---

Initially, I could not ssh into my VM from my windows laptop. I thought at first it was because I did not follow along exactly with the tutorial. Instead of generating ssh key using the MINGW/git bash with the linux style command, I did it in command-prompt using the windows style command. I kept getting a public key error.

Permanent solution:

It turns out it wasn’t an issue with the keygen at all! It was silly, as with most “bugs.” I had given my ssh key a different username than what showed in my VM (my google account username). So I had been trying to log in with googleacctuser@[ipaddr] instead of mySSHuser@[ipaddr]. I figured this out by retracing my steps to double check that I had set up an ssh key in GCP console, where it showed the user and ssh key. I quickly changed the username to the correct one (googleacctuser) in my config file and it works!

Now, the catch is that I’ve created two users! I made all the installations, permissions granting, etc. on googleacctuser and it’s not accessible from liv. So there’s a couple avenues I could take, but since I set up googleacctuser and I don’t need mySSHuser, I’m just going to change the username at the end of the ssh key to mySSHuser from mySSHuser on local (open up public gcp ssh file in texteditor), and re-paste that into the GCP console. Then update the config file and use mySSHuser to log in.

Then delete mySSHuser account in the VM terminal just to keep things clean. (i skipped this because i am now a bit attached :) )

Temporary solution: Before i figured out my issue, I took a shortcut by ssh’ing into the VM in the browser (see screenshot), which actually worked nicely for a while. But eventually I wanted to use VScode.

![Image](images/data-engineering-zoomcamp/image_31ceb9bc.png)

