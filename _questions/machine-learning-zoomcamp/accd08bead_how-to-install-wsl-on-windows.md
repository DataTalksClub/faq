---
id: accd08bead
question: How to install WSL on Windows 10 and 11 ?
section: 5. Deploying Machine Learning Models
course: machine-learning-zoomcamp
sort_order: 1800
---

Windows 10:

Open PowerShell as Admin.

Run: wsl --install

Restart your computer.

Set up your Linux distribution (e.g., Ubuntu).

Windows 11:

Open Windows Terminal as Admin.

Run: wsl --install

Restart if prompted.

Set up your Linux distribution.

Note: To install a specific distribution, use wsl --install -d <DistributionName>.

For updates, run: wsl --update.

It is quite simple, and you can follow these instructions here:

Make sure that you have “Virtual Machine Platform” feature activated in your Windows “Features”. To do that, search “features” in the research bar and see if the checkbox is selected. You also need to make sure that your system (in the bios) is able to virtualize. This is usually the case.

In the Microsoft Store: look for ‘Ubuntu’ or ‘Debian’ (or any linux distribution you want) and install it

Once it is downloaded, open the app and choose a username and a password (secured one). When you type your password, nothing will show in the window, which is normal: the writing is invisible.

You are now inside of your linux system. You can test some commands such as “pwd”. You are not in your Windows system.

To go to your windows system: you need to go back two times with cd ../.. And then go to the “mnt” directory with cd mnt. If you list here your files, you will see your disks. You can move to the desired folder, for example here I moved to the ML_Zoomcamp folder:

![Image](images/machine-learning-zoomcamp/image_b74116cb.png)

Python should be already installed but you can check it by running sudo apt install python3 command.

You can make your actual folder your default folder when you open your Ubuntu terminal with this command : echo "cd ../../mnt/your/folder/path" >> ~/.bashrc

You can disable bell sounds (when you type something that does not exist for example) by modifying the inputrc file with this command: sudo vim /etc/inputrc

You have to uncomment the set bell-style none line -> to do that, press the “i” keyboard letter (for insert) and go with your keyboard to this line. Delete the # and then press the Escape keyboard touch and finally press “:wq” to write (it saves your modifications) then quit.

You can check that your modifications are taken into account by opening a new terminal (you can pin it to your task bar so you do not have to go to the Microsoft app each time).

You will need to install pip by running this command sudo apt install python3-pip

NB: I had this error message when trying to install pipenv ():

/sbin/ldconfig.real: Can't link /usr/lib/wsl/lib/libnvoptix_loader.so.1 to libnvoptix.so.1

/sbin/ldconfig.real: /usr/lib/wsl/lib/libcuda.so.1 is not a symbolic link

So I had to create the following symbolic link:

sudo ln -s /usr/lib/wsl/lib/libcuda.so.1 /usr/lib64/libcuda.so

(Mélanie Fouesnard)

