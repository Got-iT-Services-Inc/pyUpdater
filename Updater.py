#############################################################
# Title: Python Updater Class		                    #
# Description: Wrapper For checking and updating a python   #
#              application				    #
# Version:                                                  #
#   * Version 1.0 12/18/2016 RC                             #
#                                                           #
# Author: Richard Cintorino (c) Richard Cintorino 2016      #
#############################################################

#################################################################
# Help: Python Config File Class	                    	#
#    Var = PConfig("Path-To-Config","Display-Debug-True-False") #
#								#
#    Var.get(self,"Config-Key-Name") returns "Value"		#
#################################################################

import sys
from Debug import pyDebugger

class pyUpdater:

    def __init__(self, ConfigFile, bDebug = True):
        self.Debugger = pyDebugger(self,bDebug,False)
        self.Config = pyConfig()

