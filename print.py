# -*- coding: utf-8 -*-

#################################################
# print.py     							        
# 25 July 2013
# Said ÖZCAN									
# Instagram Printer
#################################################

from classes.PdfPrinter import PdfPrinter

try:
	if __name__ == '__main__':	
		PdfPrinter()

except KeyboardInterrupt:
	
	print '>>InstagramPrinter: Application will shut down.'