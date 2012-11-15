=====
Lolo
=====

The goal of Lolo is to track when 091 Labs is open.

Downloads
=========

Driver: http://libk8055.sourceforge.net/
Python: http://sourceforge.net/projects/python-k8055/

How this works:
===============

In advance of installing lolo itself, you need to install and set a few other areas...

Further down, I've areas marked with <code></code> - the stuff inside those tags is what should be entered... or something close to it depending on your settings.

~~~~~~~~~
libk8055:
~~~~~~~~~

sudo apt-get install build-essential libusb-dev

download from site and go to extracted driver folder

vim Makefile and remove the '?' from line 7: "PREFIX = ?/usr/local"

make all
sudo make install

~~~~~
udev:
~~~~~

The usb device permissions can be set in udev:

Plug in the device and then run 'lsusb' 
Check for the idVendor (before ':') and idProduct (after ':') values in the ID section. They may be the same as below.

cd /etc/udev/rules.d

<code>
sudo echo SUBSYSTEM=="usb", ATTR{idVendor}=="10cf", ATTR{idProduct}=="5500", MODE="0666" >/etc/udev/rules.d/k8055.rules
</code>

!!
!!  need to change the k8055.rules to include command to run upstart job
!!

Plug out the device and reboot udev - 'service udev restart'

'k8055' in command line to test

~~~~~~~~~~~~~
python-k8055:
~~~~~~~~~~~~~

cd <extracted folder>

python setup.py build
sudo python setup.py install

~~~~~~~~
upstart: ---- is upstart needed? Can run the file straight from udev...
~~~~~~~~

New-age cronjob!

cd /etc/init/
vim lolo.conf

<code>
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
</code>

~~~~~
lolo:
~~~~~

sudo easy_install lolo<version>.tgz
'locate lolo'
Select the one that starts with /usr/local/lib, /usr/lib, or something similar probably also mentioning Python. 


==========================
Changing headers for CORS:
==========================

into your Apache server httpd.conf (or your .htaccess file of choice)

<code>
<Directory (your full pathname)>
	<Files ##################################### <- UNFINISHED!!!>
        Header set Access-Control-Allow-Origin "*"
        Header set Cache-Control "no-cache"
	</Files>
</Directory>
</code>

==================================
Changing desktop for boredom sake:
==================================

<code>
subprocess.call(["gsettings","set","org.gnome.desktop.background","picture-uri","'file://"+self.PREFIX+"lolo/images/closed.png'"])
</code>
