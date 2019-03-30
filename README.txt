MovieTime Installation 

Setup NFS Server
install nfs-kernel-server
edit /etc/exports 
sudo systemctl daemon-reload
sudo systemctl start nfs-server
sudo systemctl status nfs-server

Setup Pi

install raspbian
additional packages needed
	nfs-common
	mongodb
	python3-pymongo
	omxplayer (if not already installed)
	omxplayer-wrapper (use sudo pip3 install omxplayer-wrapper)
	
since pip3 dosent install to a global location we need to move it 
	from: /usr/local/<python version>/dist-packages
	to: /usr/lib/python3/dist-packages

from the desktop open pi preferences and check "wait for network" option

or sudo raspi-config select "Boot Options" select "wait for network"

move movietime.service into /lib/systemd/system
	sudo systemctl daemon-reload
	sudo systemctl start movietime.service
	
now set up /etc/fstab using the example provided
	