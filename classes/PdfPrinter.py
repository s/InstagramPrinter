# -*- coding: utf-8 -*-

#################################################
# PdfPrinter.py     		
# 22 July 2013
# Said ÖZCAN									
# Instagram Printer
#################################################

import os, sys, cgi, cStringIO, fnmatch, time, logging, subprocess

from datetime import date

class PdfPrinter:

	outputDirectory = 'outputs/'

	def __init__(self):
		self.main()

	def findFiles (self,path, filter):
		for root, dirs, files in os.walk(path):
			for file in fnmatch.filter(files, filter):
				yield file

	def main(self):

		timestamp=str(date.today().strftime('%d_%m_%Y'))

		logging.basicConfig(format="%(asctime)s %(message)s",filename=self.outputDirectory+'logs/'+timestamp+'_log.txt',level=logging.DEBUG)

		src=os.getcwd()+self.outputDirectory + "views/"

		dst=os.getcwd()+self.outputDirectory + "printed/"

		for tfile in self.findFiles(src, '*.pdf'):

			subprocess.Popen(['lp', '-o', 'media=Custom.100x150mm', '-o', 'fit-to-page', src+tfile])

			self.log(tfile + " sent to print queue")

			time.sleep(0.5)

			os.system ("mv"+ " " + src + tfile + " " + dst + tfile)

			self.log(tfile + " moved to printed folder")

		time.sleep(3.0)

		self.log('restarting...')

		self.restart_program()

	def log(self, message):

		logging.debug(message)

		print '>>PDFPrinter: ' + message

	def restart_program(self):

		python = sys.executable

		os.execl(python, python, * sys.argv)