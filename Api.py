# -*- coding: utf-8 -*-

#################################################
# api.py     		
# 22 July 2013
# Said ÖZCAN									
# Instagram Printer
#################################################

import httplib

import urllib2

import json

import time

import sys

import shutil

import os

import Printer









class Api:

	# Instagram Api Url
	apiUrl = 'api.instagram.com'


	# Instagram Api Access Token
	accessToken = ''


	# Hashtag to search
	searchHashtag = 'saidozcansaid'


	# Instagram Api Method Type
	method = 'GET'


	#Instagram Api path
	apiPath = '/v1/tags/{$hashTag}/media/recent?access_token={$accessToken}&max_id={$maxTagId}'
	

	#Instagram data min_tag_id 
	#minTagId

	
	#Instagram data max_tag_id
	#maxTagId


	#Api connection flag
	#if methods below can't finish it's job within delay time, this flag will prevent send second request
	apiConnectionFlag = 0


	#Api connection delay time
	delayTime = 30


	#Output directory
	outputDirectory = 'output/'

	







	##################
	# method __init__
	# the __init__ method
	# @param self
	# @return void
	##################

	def __init__(self):

		print '>>InstagramPrinter: Initializing'
		
		#replacing hashtag with the reserved string
		self.apiPath = self.apiPath.replace( '{$hashTag}' , self.searchHashtag  )


		#replacing access token with the reserved string
		self.apiPath = self.apiPath.replace( '{$accessToken}' , self.accessToken )


		#replacing access token with the reserved string
		#self.apiPath = self.apiPath.replace( '{$maxTagId}' , self.accessToken )		

		while self.apiConnectionFlag is 0:

			self.connect2Api()

			time.sleep( self.delayTime )


	






	##################
	# method connect2Api
	# this method connects to instagram api
	# @param self
	# @return void
	##################

	def connect2Api(self):

		print '>>InstagramPrinter: Connecting To Api'

		self.apiConnectionFlag = 1

		try:
		
			httpObject = httplib.HTTPSConnection( self.apiUrl )
			
			httpObject.request(self.method, self.apiPath)

			response = httpObject.getresponse()			
			
			if not response.status is 200:

				print '>>InstagramPrinter: HTTP Response Code is not 200'

				pass

			else:

				responseJson = response.read()

				self.processData( responseJson )

		except Exception as exc:

			print '>>InstagramPrinter: An Exception Raised During Connecting To Api:' + str(exc)

			sys.exit(0)

	







	##################
	# method processData
	# this method handles json object and creates semantic data
	# @param self
	# @return void
	##################

	def processData( self, responseJson ):
		
		print '>>InstagramPrinter: Processing Data'		
		
		try:

			data = json.loads( responseJson )['data']

			if len(data):

				for d in data:

					self.saveDataAsHtml( d )

			else: 
				
				print '>>InstagramPrinter: No photos fetched'

		except Exception as exc:

			print '>>InstagramPrinter: An Exception Raised During processData:' + str(exc)

			sys.exit(0)
	

	






	##################
	# method processData
	# this method saves data as html
	# @param self
	# @return void
	##################

	def saveDataAsHtml(self, data):
		
		#user data
		user = data['user']

		#comments
		comments = data['comments']

		#likes
		likes = data['likes']

		#image array for standart resolution
		standartResolutionImage =  data['images']['standard_resolution']

		#print data['created_time']

		fileName = str(data['created_time']) + '.html'

		source = self.outputDirectory + 'templates/main.html'
		
		destination = self.outputDirectory + 'views/'

		try:
						
			shutil.copy( source, destination )

			os.rename( destination + 'main.html' , destination + fileName )

		except Exception as exc:

			print '>>InstagramPrinter: An Exception Raised During generating view:' + str(exc)

			sys.exit(0)

		fileObject = open( destination + fileName , 'wb+')

		fileContents = fileObject.read()

		fileContents = fileContents.replace( '{$title}', user['username'] + '\'s photo' )

		#fileObject.write('%s'%fileContents)

		#fileObject.close()

		print fileContents