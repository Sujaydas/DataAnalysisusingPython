#!/usr/bin python

############################################

#Created by: Sujay Premkumar
#Date : 18 Oct 2016
#Reviwer : Spandan
#Purpose : Analyse the tweets and create the analysis files in the Current Directory


########################################### 

import os
import urllib
import requests
import argparse
import time
from datetime import datetime,date,timedelta
from requests_oauthlib import OAuth1

#######################################

#Func: Parse_CommandLine()
#Description:  Create search term and File name argument for the command line
#Inout: parser - parser object which adds the argument
########################################

def Parse_CommandLine(parser):

	parser.add_argument("Search_term", help="Search word to be queried " + \
		"to twitter API")
	parser.add_argument("File_Name", help="Provide the file name to be " + \
		"saved")
	
	args = parser.parse_args()
	print("The query to be searched is "+ args.Search_term)
	return args


#######################################

#Func: Authenticate_User()
#Description:  Authenticate the user trying to acccess is valid with authenticate access token and credentials
#Inout: Auth - authenticate object to be passed to get request for authentication 
########################################


def Authenticate_User(auth):

	#Authenticate the User
	url = 'https://api.twitter.com/1.1/account/verify_credentials.json'

	res = requests.get(url, auth=auth)
	return res


#######################################

#Func: Create_encode_query()
#Description:  Create final URL to be sent for GET request by encoding the term 
#Inout: Base_URL -  https://api.twitter.com/1.1/search/tweets.json
#	Search_Term - add this search term to the URL 
#	search_url - final search URl to be passed to GET reuesr
########################################



def Create_encode_query(Base_URL,Search_term):
	
	search_url = Base_URL + "?result_type=mixed" + "&count=400"
	search_url = search_url + "&q="

	res = urllib.quote(Search_term)
	search_url = search_url + res
	return search_url


#######################################

#Func: Create_Request_URL()
#Description:  Use the Search Term to create the Search URL to be passed for GET Request
#Inout: Search_term -  To be searched in the twitter search Bar
#	auth  - Authenticate Object to be passed to the search request
########################################


def Create_Request_URL(Search_term,auth):
	#Create a Search Request

	Base_URL = "https://api.twitter.com/1.1/search/tweets.json"

	#Create a encoded Query
	search_url = Create_encode_query(Base_URL,Search_term)

	return search_url

#######################################

#Func: get_tweets()
#Description:  Use Request API to get the query the Twitter API for tweets
#Inout: search_url - query URL
#	auth - authernticate object
#	r - list of 100 tweets for the search term asked
########################################


def get_tweets(search_url,auth):
	r = requests.get(search_url,auth=auth)
	return r

#######################################

#Func: save_tweets()
#Description:  Take the tweets, save it an file, under the Search_term folder
#Inout: search_term -  name folder to be created under the current date,
#	tweets_json - json string to be saved in the file
#	File_Name  - File name of the contents of the tweets to be saved.

########################################


def save_tweets(search_term,tweets_json,File_Name):
	
	d0 = datetime.now()
	cur_time = str(d0.time())
	Cur_date = str(d0.date())
	Cur_time_st = datetime.now().strftime("%H:%M:%S")

	#1. Create Folder with Current Date
	#2. Create Folder with Search Term
	#3. Create file of json response in that folder with user provided name and time_stamp name

	newpath = "./Output"
	if not os.path.exists(newpath):
		try:
			os.makedirs(newpath)
		except OSError as exception:
        		if exception.errno != errno.EEXIST:
				print("Error during creating Output Directory")
	
	newpath = newpath +"/" + Cur_date

	if not os.path.exists(newpath):
		try:
			os.makedirs(newpath)
		except OSError as exception:
        		if exception.errno != errno.EEXIST:
				print("Error during creating Date Directory")

	newpath = newpath +"/" + search_term

	if not os.path.exists(newpath):
		try:
			os.makedirs(newpath)
		except OSError as exception:
        		if exception.errno != errno.EEXIST:
				print("Error during creating Search Directory")

	if File_Name == None or File_Name == "":
		File_Name = search_term 

	newpath = newpath +"/" + File_Name + "_" + Cur_time_st + ".json"

	print("Tweets are saved at the location: " + newpath)
	bIspath_Exists = os.path.isfile(newpath)

	if bIspath_Exists:
		print("The file name: " + newpath + " ,already present" + \
			"Please provide other File name")
		return

	_json_file_ = open(newpath, 'w')
	_json_file_.write(tweets_json.text)


#######################################

#Func: Main()
#Description: Start of the Script, Parses the command line arguments, Authenticate USer,  create a request URL, and save the tweets,   
#Inout: None 
########################################


def Main():

	#Parse the Twitter search term
	parser = argparse.ArgumentParser()
	parse_result = Parse_CommandLine(parser)
	
	if "." in parse_result.File_Name:
		print("File name entered : " + parse_result.File_Name + \
		" has \" . \". Please enter file name without \" . \" ")
		return

	auth = OAuth1('EKwc7yj7uqm2k71N5hGFQqrxd', 		'gYQC8HgieVSE50v0uelFUdTa8nqXZDR3DqhYc7F0lK1OY6biFA',
                  '196464957-UhsygQ19Pfw3dPiAwkBxtlHLVPdRafMHECIjcsVT', 	'5aO82FMTF58G2hnB49rd7hmMiX5MqqQ7HlIWWbzjY0adY')

	res = Authenticate_User(auth)

	#Check if the Authentication was successfull
	if res.status_code == 200:
		url = Create_Request_URL(parse_result.Search_term,auth)

		print("URL is "+ url)
		tweets = get_tweets(url,auth)

		#Break at max limit reached
		save_tweets(parse_result.Search_term,tweets,parse_result.File_Name)

#Trigger Main()
if __name__ == "__main__":
	Main()

