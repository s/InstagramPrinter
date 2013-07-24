# -*- coding: utf-8 -*-

#################################################
# app.py     							        
# 22 July 2013
# Said ÖZCAN									
# Instagram Printer
#################################################

from classes.Api import *

try:
	if __name__ == '__main__':	
		Api()
		
except KeyboardInterrupt:
	print '>>InstagramPrinter: Application will shut down.'