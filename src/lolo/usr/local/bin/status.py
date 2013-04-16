#!/usr/bin/python

import os
import sys
import time
import json
import subprocess

class LoloStatus():
	def __init__(self):
		self.PREFIX = "/var/www/"
		self.FILENAME = self.PREFIX + "lolo/json/status.json"

	def change_status(self, board=False):
		'''Toggles Labs open/closed'''

		# Pulls in previous Labs status (reads from JSON file)
		status = self.load_status()

		# Changes status between open & closed (Boolean).
		# Toggles symbolic link between open & closed image as current status image.
		if status['open'] is True:
			status['open'] = False
			status['status'] = "091 Labs is closed."
			subprocess.call(["ln", "-sf", self.PREFIX+"lolo/images/closed.png", self.PREFIX+"lolo/images/status.png"])
			if board:
				board.set_digital_outputs([0,1,0,0,0,0,0,0])
		else:
			status['open'] = True
			status['status'] = "091 Labs is open."
			subprocess.call(["ln", "-sf", self.PREFIX+"lolo/images/open.png", self.PREFIX+"lolo/images/status.png"])
			if board:
				board.set_digital_outputs([1,0,0,0,0,0,0,0])
		
		# Saves time and sends on the current Labs status (writes back to JSON file).
		status['lastchange'] = int(time.time())
		self.save_status(status)

	def load_status(self):
		'''Loads JSON data from FILENAME'''

		with open(self.FILENAME, "r") as FILE:
			data = FILE.read()		
		return json.loads(data)		# JSON-formatted data converted into Python object.
	
	def save_status(self, status):
		'''Writes JSON data to FILENAME'''

		with open(self.FILENAME, "w") as FILE:
			data = json.dumps(status)	# Python object converted into JSON-formatted data.
			FILE.write(data)
			
def main():
	lolo = LoloStatus()
	lolo.change_status()	

if __name__ == '__main__':
	main()
