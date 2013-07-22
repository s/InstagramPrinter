# -*- coding: utf-8 -*-

#################################################
# api.py     		
# 22 July 2013
# Said ÖZCAN									
# Instagram Printer
#################################################

import httplib

import urllib

import json

import time

import Printer

class Api:

	# Instagram Api Url
	apiUrl = 'api.instagram.com'


	# Instagram Api Access Token
	accessToken = ''


	# Hashtag to search
	searchHashtag = 'istanbul'


	# Instagram Api Method Type
	method = 'GET'


	#Instagram Api path
	apiPath = '/v1/tags/{$hashTag}/media/recent?access_token={$accessToken}&max_id={$maxTagId}'
	

	#Instagram data min_tag_id 
	#minTagId

	#Instagram data max_tag_id
	#maxTagId


	##################
	# method __init__
	# the __init__ method
	# @param self
	# @return void
	##################

	def __init__(self):

		#replacing hashtag with the reserved string
		self.apiPath = self.apiPath.replace( '{$hashTag}' , self.searchHashtag  )


		#replacing access token with the reserved string
		self.apiPath = self.apiPath.replace( '{$accessToken}' , self.accessToken )


		#replacing access token with the reserved string
		#self.apiPath = self.apiPath.replace( '{$maxTagId}' , self.accessToken )

		while 1:

			self.connect2Api()

			time.sleep(30)


	##################
	# method connect2Api
	# this method connects to instagram api
	# @param self
	# @return void
	##################

	def connect2Api(self):

		print 'Connecting To Api'

		try:
		
			httpObject = httplib.HTTPSConnection( self.apiUrl )
			
			httpObject.request(self.method, self.apiPath)

			response = httpObject.getresponse()

			if not response.status is 200:

				print 'HTTP Request Code is not 200'

			else:

				responseJson = response.read()

				self.processData(responseJson)

		except:

			print 'An Exception Raised'

	##################
	# method processData
	# this method handles json object and creates semantic data
	# @param self
	# @return void
	##################

	def processData( self, responseJson ):
		pass
		#print responseJson
