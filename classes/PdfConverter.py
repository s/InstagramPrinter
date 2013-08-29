# -*- coding: utf-8 -*-

#################################################
# PdfConverter.py     		
# 22 July 2013
# Said ÖZCAN									
# Instagram Printer
#################################################

import os, sys, cgi, cStringIO, logging, subprocess, time, urllib

import xhtml2pdf.pisa as pisa

from datetime import date

# Shortcut for dumping all logs to the screen
pisa.showLogging()

def main(fileName):

    """
    Loading from an URL. We open a file like object for the URL by
    using 'urllib'. If there have to be loaded more data from the web,
    the pisaLinkLoader helper is passed as 'link_callback'. The
    pisaLinkLoader creates temporary files for everything it loads, because
    the Reportlab Toolkit needs real filenames for images and stuff. Then
    we also pass the url as 'path' for relative path calculations.
    """
    
    timestamp=str(date.today().strftime('%d_%m_%Y'))
    
    logging.basicConfig(format="%(asctime)s %(message)s",filename='outputs/logs/'+timestamp+'_log.txt',level=logging.DEBUG)

    pdf = pisa.CreatePDF(
        file(fileName+".html", "r"),
        file(fileName + ".pdf", "wb"),
        log_warn = 1,
        log_err = 1,
        path = os.path.join(os.getcwd(), fileName+".html")
    )
    
    log("Converted pdf "+fileName+".pdf")

def log(message):
	
		logging.debug(message)
		
		print '>>PDFConverter: ' + message


if __name__=="__main__":

    main(sys.argv[1])