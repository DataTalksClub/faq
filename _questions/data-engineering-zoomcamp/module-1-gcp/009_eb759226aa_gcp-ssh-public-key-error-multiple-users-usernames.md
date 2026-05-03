---
id: eb759226aa
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_31ceb9bc.png
question: 'GCP: SSH public key error - multiple users / usernames'
sort_order: 9
---

Initially, I could not SSH into my VM from my Windows laptop. I thought it was because I did not follow the tutorial exactly. Instead of generating the SSH key using MINGW/git bash with the Linux-style command, I did it in Command Prompt using the Windows-style command. I kept getting a public key error.

**Permanent Solution:**

It turns out it wasn’t an issue with the key generation at all! The problem was with the username. I had given my SSH key a different username than what appeared in my VM (my Google account username). So, I had been trying to log in with `googleacctuser@[ipaddr]` instead of `mySSHuser@[ipaddr]`. Here's how I resolved it:

1. Retraced my steps to check the SSH key setup in the GCP console, where it showed the user and SSH key.
2. Changed the username to the correct one (googleacctuser) in my config file.
3. Updated the config file and used `mySSHuser` to log in.

Now, the issue was that I had created two users. I made all the installations and permissions on `googleacctuser`, not accessible from `mySSHuser`. Since I didn't need `mySSHuser`, I edited the SSH key to change the username at the end and updated the GCP console and config file accordingly.

Then, I planned to delete the `mySSHuser` account in the VM terminal to keep things clean (though I got a bit attached, so I skipped this).

**Temporary Solution:**

Before figuring out my issue, I used a shortcut by SSH'ing into the VM in the browser, which worked nicely for a while. But eventually, I needed to use VSCode.

<{IMAGE:image_1}>
