MovieTime was written for the Raspberry Pi to take advantage of OMXPlayers 
superior video playback as compared to browser playback.  With limited storage
space on the Raspberry Pi a NFS server will be needed to server up the video
files to the Pi.

Setup

From the desktop open pi preferences and check "wait for network" option
or sudo raspi-config select "Boot Options" select "wait for network". This
will tell systemctl not to bring up movietime until the network is available.

Open a terminal and install mongodb if it is not already installed
    sudo apt install mongodb

You will also need Omxplayer, which comes pre installed on raspbian,
however if it is not 
    sudo apt install omxplayer

Setup your python virtual enviroment and these additional packages will be
needed
    omxplayer-wrapper (omxplayer python bindings)
    pymongo (db bindings)
    tornado (webserver)
    PIL or pillow (image processing)

Now move movietime into your virtual enviroment

Make the needed adjustments to /etc/fstab, please see /boot/fstab.example

Then run sudo mount -a this will mount all of your NFS mounts.
Your nfs mounts should be automatic on restarts.

If you would like movietime to start automatically on boot then 
move movietime.service into /lib/systemd/system and then preform these
commands
	sudo systemctl daemon-reload
	sudo systemctl start movietime.service
	
The paths to movie and poster art will need to be edited as they have been
hard coded into the app.  As this is a personal project and I did not see a
need for a configuration or an authintication system at this time.

BE WARNED DO NO USE THIS IS THE WILD, USE IT ON YOUR HOME NETWORK ONLY.
THERE IS NO AUTHINTICATION/SECURITY SYSTEM IT IS MEANT FOR PERSONAL 
USE ONLY