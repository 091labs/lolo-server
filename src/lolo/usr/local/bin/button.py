#!/usr/bin/python

"""
Button sensor & status updater
"""

import time
import k8055
import status

class ButtonBoard(k8055.Board):
    def __init__(self, address=0):
        k8055.Board.__init__(self, address)
    
    def waiting(self):
        if board.digital_inputs[0]:
            print "script success!"
            lolo = status.LoloStatus()
            lolo.change_status(board)
            time.sleep(5)

    def run(self):
        while True:
        	self.read()
        	self.read()
	        board.waiting()
	        
def main():
	board = ButtonBoard()
	board.run()

if __name__ == '__main__':
	main()
