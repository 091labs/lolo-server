===========
lolo-server
===========

The goal of LoLo is to track when 091 Labs is open.

Downloads
=========

Driver: http://libk8055.sourceforge.net/
Python: http://sourceforge.net/projects/python-k8055/

How this works
==============

In advance of installing lolo-server itself, you need to install and setup a few other areas so the board can be detected and controlled by Ubuntu.

libk8055
--------

This is for setting up a Velleman k8055 prototyping board to work with Ubuntu

Make sure you have build-essential and libusb first::

	sudo apt-get install build-essential libusb-dev

Download from site and go to extracted driver folder::

	vim Makefile and remove the '?' from line 7: "PREFIX = ?/usr/local"

	make all
	sudo make install

udev
----

The usb device permissions can be set in udev.

Plug in the device and then run::

	lsusb
	
Check for the idVendor (before ':') and idProduct (after ':') values in the ID section. They may be the same as below.::

	cd /etc/udev/rules.d

	sudo echo SUBSYSTEM=="usb", ATTR{idVendor}=="10cf", ATTR{idProduct}=="5500", MODE="0666" >/etc/udev/rules.d/k8055.rules

!!
!!  need to change the k8055.rules to include command to run upstart job
!!

Plug out the device and reboot udev::

	service udev restart

Run::

	k8055

in command line to test

python-k8055
------------

Extract the folder and install program::

	cd <extracted folder>

	python setup.py build
	sudo python setup.py install

upstart
-------

New-age cronjob!::

	cd /etc/init/
	vim lolo.conf

Insert::
	
	# lolo - Labs On ; Labs Off
	#
	# Status updater for 091 Labs
	#

	author "author name <author@email>"
	description "091 Labs status updater"

	start on startup

	# run Lolo
	exec python /usr/local/lib/python2.7/dist-packages/lolo/lolo.pyc

	respawn
	respawn limit 10 90

lolo
----

Installing LoLo to Ubuntu::

	sudo easy_install lolo<version>.tgz
	locate lolo

Select the one that starts with /usr/local/lib, /usr/lib, or something similar probably also mentioning Python. 


==========================
Changing headers for CORS:
==========================

For the SpaceAPI json file.
Into your Apache server httpd.conf (or your .htaccess file of choice)::

	<Directory /var/www/lolo/json>
		    <Files "status.json">
		            Header set Access-Control-Allow-Origin "*"
		            Header set Cache-Control "no-cache"
		    </Files>
	</Directory>

==================================
Changing desktop for boredom sake:
==================================

This was done at MakerFaire simply to make the change more visible to people passing the stall.

Add the each of the following::

	subprocess.call(["gsettings","set","org.gnome.desktop.background","picture-uri","'file://"+self.PREFIX+"lolo/images/closed.png'"])

	subprocess.call(["gsettings","set","org.gnome.desktop.background","picture-uri","'file://"+self.PREFIX+"lolo/images/open.png'"])

... to the appropriate side of the if...else within the change_status() function in status.py
