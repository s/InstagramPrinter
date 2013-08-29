# -*- coding: utf-8 -*-

#################################################
# Api.py     		
# 22 July 2013
# Said ÖZCAN									
# Instagram Printer
#################################################

import httplib, urllib2, json, time, sys, shutil, os, stat, re, datetime, yaml, logging

from datetime import date


class Api:


	############ static members ############
	
	# Instagram Api Url
	apiUrl = 'api.instagram.com'


	# Instagram Api Method Type
	method = 'GET'


	#Instagram Api path
	apiPath = '/v1/tags/{$hashTag}/media/recent?access_token={$accessToken}'


	#Api connection flag
	#if methods below can't finish it's job within delay time, this flag will prevent send second request
	apiConnectionFlag = 0


	#Output directory
	outputDirectory = 'outputs/'

	
	############ dynamic members from config.yaml ############

	# Instagram Api Access Token
	accessToken = ''


	# Hashtag to search
	searchHashtag = ''

	#Api connection delay time
	delayTime = 0


	#Html file page title
	pageTitle = ''
	
	minTagId=''
	
	footerImage= ''
	

	##################
	# method __init__
	# the __init__ method
	# @param self
	# @return void
	##################

	def __init__(self):
	
		timestamp= str(date.today().strftime('%d_%m_%Y'))
		
		logging.basicConfig(format="%(asctime)s %(message)s",filename=self.outputDirectory+'logs/'+timestamp+'_log.txt',level=logging.DEBUG)
		
		self.log('InstagramPrinter: Initializing')
		
		self.get_configurations()
		
		#replacing hashtag with the reserved string
		self.apiPath = self.apiPath.replace( '{$hashTag}' , self.searchHashtag  )


		#replacing access token with the reserved string
		self.apiPath = self.apiPath.replace( '{$accessToken}' , self.accessToken )
		
		
		if self.minTagId != '':
			self.apiPath+='&min_id=' + self.minTagId

		if True is self.check_network():

				while self.apiConnectionFlag is 1:
					pass

				self.connect_to_api()

		else:

			self.log('No network connection')


	##################
	# method connect_to_api
	# this method connects to instagram api
	# @param self
	# @return void
	##################

	def connect_to_api(self):

		self.log('Connecting To Api')
		
		self.apiConnectionFlag = 1
		#check network connection
		try:
		
			httpsObject = httplib.HTTPSConnection( self.apiUrl )
			
			httpsObject.request(self.method, self.apiPath)
			
			#print self.apiPath

			response = httpsObject.getresponse()
			
			
			
			if not response.status is 200:
			
				self.log('HTTP Response Code is not 200')

				pass

			else:

				responseJson = response.read()

				self.process_data( responseJson )

		except Exception as exc:

			self.log("An Exception Raised During Connecting To Api:" + str(exc))

			sys.exit(0)


	##################
	# method process_data
	# this method handles json object and creates semantic data
	# @param self
	# @return void
	##################

	def process_data( self, responseJson ):
	
		self.log("Processing Data")
		
		try:

			response = json.loads( responseJson )
			
			data = response['data']
			
			if len(data):

				for d in data:
						
					self.save_data_as_html( d )
					
				
				if 'next_min_id' in response['pagination']:
					
					tagFile = open('minTagId.yaml','w')
			
					tagFile.write(response['pagination']['next_min_id'])
				
					tagFile.close()
				
				else:
					self.log("Nothing new to print")
				
				
			else: 
				self.log("No photos fetched")
				
	
			self.log('Sleep time before restart ' + str(self.delayTime) + ' seconds.')
							
			time.sleep( float(self.delayTime) )
			
			self.log('Quiting, byee...')
				
			self.restart_program()

		except Exception as exc:
			
			self.log('An Exception Raised During process_data:' + str(exc))
			
			sys.exit(0)
	

	##################
	# method process_data
	# this method saves data as html
	# @param self
	# @return void
	##################

	def save_data_as_html(self, data):
		
		#print '>>InstagramPrinter: Will Generate HTML if not exists before'	

		self.apiConnectionFlag = 0

		fileName = str(data['id']) + '.html'

		source = self.outputDirectory + 'templates/' + self.templateFileName
		
		destination = self.outputDirectory + 'views/'

		if not os.path.exists( destination ):
			os.makedirs( destination )
			os.chmod( destination, 0777)
		
		#user data
		user = data['user']

		#comments
		comments = data['comments']

		#likes
		likes = data['likes']

		#image array for standart resolution
		standartResolutionImage =  data['images']['standard_resolution']
		
		
		#print destination + fileName
		
		if True == os.path.exists( destination + fileName):
			self.log('File ' + fileName + ' already exists. Will pass this time.')
			
			return 
		else:
			
			try:
				
				with open( source ) as file:

					template = file.read()

			except Exception as exc:
			
				self.log('An Exception Raised During generating view:' + str(exc))

				sys.exit(0)
			
			
			import urllib
			
			
			self.log('Downloading photo: ' + standartResolutionImage['url'])
			urllib.urlretrieve(standartResolutionImage['url'],  "outputs/assets/img/"+ str(data['id'])+".jpg")
			
			self.log('Downloading avatar: ' + user['profile_picture'])
			urllib.urlretrieve(user['profile_picture'],  "outputs/assets/img/"+ str(user['id'])+".jpg")
			
			
			template = template.replace( '{$title}', self.pageTitle )

			template = template.replace( '{$postOwner}', user['username'])

			template = template.replace( '{$postOwnerAvatar}', str(user['id'])+".jpg")

			template = template.replace( '{$postDate}', datetime.datetime.fromtimestamp(int(data['created_time'])).strftime('%d.%m.%Y'))

			template = template.replace( '{$photoUrl}', str(data['id'])+".jpg" )

			template = template.replace( '{$photoWidth}', str(standartResolutionImage['width']) )

			template = template.replace( '{$photoHeight}', str(standartResolutionImage['height']) )
			
			template = template.replace( '{$footerImage}', self.footerImage )

			likeCount = len(likes['data'])

			if likeCount > 0:

				if likeCount > 2:
					
					likeSentence = likes['data'][0]['username'] + ', ' +  likes['data'][1]['username'] + ' ve ' + str(likeCount-2) + ' kisi begendi.'

				elif likeCount is 2:

					likeSentence = likes['data'][0]['username'] + ', ' +  likes['data'][1]['username'] + ' begendi.'

				else:

					likeSentence = likes['data'][0]['username'] + ' begendi.'

			else:
				
				likeSentence = 'Henuz kimse begenmedi'
				

			template = template.replace( '{$likes}', likeSentence )

			startOfComments = template.index( '{$comments}' ) + len( '{$comments}' )

			endOfComments = template.index( '{/$comments}', startOfComments )

			commentsBlockWithData = ''

			if comments['count'] > 0:
				
				for comment in comments['data']:
					
					commentsBlock = template[startOfComments:endOfComments]

					commentsBlock = commentsBlock.replace( '{$commentOwner}', comment['from']['username'] )

					commentsBlock = commentsBlock.replace( '{$commentOwnerAvatar}', comment['from']['profile_picture'] )

					commentsBlock = commentsBlock.replace( '{$commentText}', comment['text'] )
					
					commentsBlockWithData += commentsBlock

				template = template.replace( '{$comments}' + template[startOfComments:endOfComments] + '{/$comments}', commentsBlockWithData )
				
			else:
			
				template = template.replace( '{$comments}' + template[startOfComments:endOfComments] + '{/$comments}', '' )
				
			fileName=  data['id']

			newFilePath = destination+fileName + '.html'
			
			if True == os.path.exists(newFilePath):
				os.remove(newFilePath)
				
			
			newFile = open( newFilePath, 'w+' )
			
			newFile.write( template.encode('utf8') )
			
			newFile.close()
			
			self.log(fileName + '.html has been generated.' )
			
			self.convert_pdf( destination+fileName )

	
	##################
	# method convert_to_pdf
	# this method
	# @param self
	# @return void
	##################
	
	def convert_pdf(self, fileName):
		
		import subprocess
		
		subprocess.call(["python "+os.getcwd()+"/classes/PdfConverter.py " + fileName], shell=True)
		
		self.log(fileName + '.pdf has been generated.' )	    
			

	##################
	# method check_network
	# this method checks network connection
	# @param self
	# @return void
	##################

	def check_network(self):

		try:

			response=urllib2.urlopen('http://google.com',timeout=100)

			return True

		except:
			return False

	##################
	# method get_configurations
	# this method gets the configurations of application from config.yaml
	# @param self
	# @return void
	##################
	def get_configurations(self):		
		
		try:
		
			configurations = open('config.yaml')
		
			data = yaml.safe_load(configurations)

			self.accessToken = data['accessToken']

			self.searchHashtag = data['searchHashtag']

			self.delayTime = data['delayTime']

			self.pageTitle = data['pageTitle']

			self.templateFileName = data['templateFileName']
			
			self.footerImage=data['footerImage']
			
			configurations.close()
						
			tagFile=open("minTagId.yaml")
			
			self.minTagId = tagFile.readline()
			
			tagFile.close()
			
			
		
		except KeyError as exc:
			
			self.log('Validation error. Check credientals')	  

			sys.exit(0)
			
			
			
			
	def restart_program(self):
	    """Restarts the current program.
	    Note: this function does not return. Any cleanup action (like
	    saving data) must be done before calling this function."""
	    python = sys.executable
	    os.execl(python, python, * sys.argv)
	    
	    
	def log(self,message):
	
		logging.debug(message)
		
		print '>>InstagramPrinter: ' + message		