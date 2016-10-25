#!/usr/bin python

############################################

#Created by: Sujay Premkumar
#Date : 18 Oct 2016
#Reviewer : Spandan
#Purpose : Analyse the tweets and create the analysis files in the Current Directory


########################################### 


#######  Libraries ########################
from __future__ import division
import os
import urllib
#import urlparse
import requests
import argparse
import time
from datetime import datetime,date,timedelta
from requests_oauthlib import OAuth1
import json
import csv
import re
import glob
import sys
reload(sys)

#######  Globals ########################
sys.setdefaultencoding('utf-8')

t1 =0;t2=0;t3=0;t4=0;t5=0;t6=0;t7=0;t8=0
t9=0;t10=0;t11=0

tweet_positive = 0; tweet_neutral = 0; tweet_negative = 0
tweet_anger = 0; tweet_anticipation = 0; tweet_disgust = 0
tweet_fear = 0; tweet_joy = 0; tweet_sadness = 0
tweet_suprise = 0; tweet_trust = 0

Total_Tweets = 0
Total_senti_Tweets = 0

positive_recur = 0; negative_recur = 0; neutral_recur = 0
csv_output = ""
ana2_output = ""
ana3_output = ""
ana4_output = ""
ana5_output = ""

Total_emotion_count = 0

_engagement_list_ = []
max_retweet_count = 0
_sentiment_list_ = []

####################################


####################################
def Parse_CommandLine(parser):
	
	parser.add_argument("Search_term", help="Search word to be analysed")
	parser.add_argument("--minday", help="minday to be searched")
	parser.add_argument("--maxday", help="maxday to be searched")

	args = parser.parse_args()
	return args

def validate_format(date_text):
    try:
        str_for = datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

def get_Daterange(minday,maxday,Cur_date):
	newpath = "./Output" + "/" + "2016-10-19"

	mn_day = newpath
	newpath = "./Output" + "/" + str(Cur_date)
	mx_day = newpath
	return mn_day, mx_day

def Load_tweetFolder(min_day, max_day):
	return ["./Output" + "/" + name for name in os.listdir("./Output") \
if os.path.isdir("./Output")]	

#######################################

#Func: Load_Files
#Description: Get all the jsons Files from the folder
#Inout: direc - folder name
#	srch_term - folders are created inthe format ./Output/Date/"Search_Term"/*.jsons,  provide serach term in this argument

########################################

def Load_Files(direc,srch_term):
	file_list = []
	
	path = direc + "/" + srch_term + "/*.json"
	
	#Get the list of files in the location specified
	file_list = glob.glob(path)
	
	return file_list


#######################################

#Func: create_sentiment_list()
#Description: Create the List of all sentiment values for a word
#Inout: None
########################################

def create_sentiment_list():
	_sentiment_list_ = []
	_fir_ = {'Word':"", 'Positive':0, 'Negative':0, 'Anger':0, 			'Anticipation':0, 'Disgust':0, 'Fear':0, 'Joy':0, 
		'Sadness':0, 'Surprise':0, 'Trust':0}
	_sentiment_file_ = open(r"./Sentiment.csv", 'r')

	_sentiment_string_ = _sentiment_file_.readline()
	while True:
	    if _sentiment_string_ == '': break
	    else:
		test_1 = _sentiment_string_.split(',')
		_fir_['Word'] =          test_1[0]
		_fir_['Positive'] =      int(test_1[1])
		_fir_['Negative'] =      int(test_1[2])
		_fir_['Anger'] =         int(test_1[3])
		_fir_['Anticipation'] =  int(test_1[4])
		_fir_['Disgust'] =       int(test_1[5])
		_fir_['Fear'] =          int(test_1[6])
		_fir_['Joy'] =           int(test_1[7])
		_fir_['Sadness'] =       int(test_1[8])
		_fir_['Surprise'] =      int(test_1[9])
		_fir_['Trust'] =         int(test_1[10].rstrip())
		_sentiment_list_.append(_fir_)
		_fir_ = {}
		
		#read entire Contents of file	
		_sentiment_string_ = _sentiment_file_.readline()  

	return _sentiment_list_


#######################################

#Func: calculate_rating()
#Description: For a single tweet, calcualate positiveness, negativeness, anger and other emotions, 
#Inout: tweet_list - tweet text
#	_sentiment_list_ - List of maps of a word and there sentimental rating
########################################


def calculate_rating(tweet_list,_sentiment_list_):
	
	global tweet_positive
	global tweet_negative
	global tweet_neutral
	global tweet_anger
	global tweet_anticipation
	global tweet_disgust
	global tweet_fear
	global tweet_joy
	global tweet_sadness
	global tweet_suprise
	global tweet_trust

	global positive_recur 
	global negative_recur
	global neutral_recur
	global Total_emotion_count

	tweet_positive = 0; tweet_neutral = 0; tweet_negative = 0
	Total_emotion_count = 0

	for sentiment_itr in _sentiment_list_:
		if sentiment_itr['Word'] in tweet_list and sentiment_itr['Positive'] == 1:
			tweet_positive += tweet_list.count(sentiment_itr['Word'])
			positive_recur += 1


		if sentiment_itr['Word'] in tweet_list and sentiment_itr['Negative'] == 1:
			tweet_negative  += tweet_list.count(sentiment_itr['Word'])
			negative_recur += 1


		if sentiment_itr['Word'] in tweet_list and sentiment_itr['Positive'] == 0 and sentiment_itr['Negative'] == 0:
			tweet_neutral += tweet_list.count(sentiment_itr['Word'])
			neutral_recur += 1

		if sentiment_itr['Word'] in tweet_list and sentiment_itr['Anger'] == 1:
			tweet_anger += tweet_list.count(sentiment_itr['Word'])
			Total_emotion_count += 1

		if sentiment_itr['Word'] in tweet_list and sentiment_itr['Anticipation'] == 1:
			tweet_anticipation += tweet_list.count(sentiment_itr['Word'])
			Total_emotion_count += 1

		if sentiment_itr['Word'] in tweet_list and sentiment_itr['Disgust'] == 1:
			tweet_disgust += tweet_list.count(sentiment_itr['Word'])
			Total_emotion_count += 1


		if sentiment_itr['Word'] in tweet_list and sentiment_itr['Fear'] == 1:
			tweet_fear += tweet_list.count(sentiment_itr['Word'])
			Total_emotion_count += 1


		if sentiment_itr['Word'] in tweet_list and sentiment_itr['Joy'] == 1:
			tweet_joy += tweet_list.count(sentiment_itr['Word'])
			Total_emotion_count += 1


		if sentiment_itr['Word'] in tweet_list and sentiment_itr['Sadness'] == 1:
			tweet_sadness += tweet_list.count(sentiment_itr['Word'])


		if sentiment_itr['Word'] in tweet_list and sentiment_itr['Surprise'] == 1:
			tweet_suprise += tweet_list.count(sentiment_itr['Word'])
			Total_emotion_count += 1


		if sentiment_itr['Word'] in tweet_list and sentiment_itr['Trust'] == 1:
			tweet_trust += tweet_list.count(sentiment_itr['Word'])
			Total_emotion_count += 1

	return tweet_positive, tweet_negative, tweet_neutral


#######################################

#Func: create_engement_list()
#Description: Create a List of dictionaries, containing tweet and there retweeted Count
#Inout: file_itr - Dictionary of single Tweet File containing each 100 tweets with its details
#	Out - None
########################################


def create_engement_list(file_itr):
	global _engagement_list_
	global max_retweet_count
	_engagement_analysis_ = {'Most Retweeted Tweets':"" , 'Retweeted Count':""}
	retweet_count =	file_itr["retweet_count"]

	if(max_retweet_count < retweet_count):
		max_retweet_count = retweet_count
		_engagement_analysis_['Most Retweeted Tweets'] = file_itr["text"].replace('\n',' ').replace(',',' ')
		_engagement_analysis_['Retweeted Count'] = retweet_count
		_engagement_list_.insert(0,_engagement_analysis_)
	
	_engagement_analysis_ = {'Most Retweeted Tweets':"" , 'Retweeted Count':""}



#######################################

#Func: Analyze_Content()
#Description: List of the a single Tweet file, Perform Sentimental Analysis
#Inout: d - List of the a single Tweet file, consists of 100 tweets in statuses feild
#	Out - None
########################################


def Analyze_Content(d):

	global tweet_positive
	global tweet_negative
	global tweet_neutral
	global _sentiment_list_
	global Total_Tweets

	for file_itr in d["statuses"]:
		t1 = file_itr["text"].replace('\n',' ')
		tweet_list = t1.split(' ')
		
		Total_Tweets += len(tweet_list)
		tweet_positive, tweet_negative, tweet_neutral = calculate_rating(tweet_list,_sentiment_list_)

		if file_itr["user"]["location"].replace(',','') == "":
			loc_str = "Unknown Location of the User"
		else:
			loc_str = file_itr["user"]["location"].replace(',','')

		global csv_output 
		csv_output += \
		file_itr["created_at"].replace(',',' ').split('+')[0] + "," + \
		loc_str + "," + \
		str(tweet_positive) + "," + \
		str(tweet_negative) + "," + \
		str(tweet_neutral).strip() + "\n"

		create_engement_list(file_itr)


#################################
#Func: Analyze_Files()
#Description : Take the File list, get the content of each file , analyse the tweets
#InOut _file_list - List of all the files in the FOlder
#      _list_length  - Number of Files in the _file_list
#################################


def Analyze_Files(_file_list,_list_length):

	for cnt_itr in range(0,_list_length,1):
	#for cnt_itr in range(0,1,1): # test loop for analysing only few files
	    	print("File Processing is : ", _file_list[cnt_itr])
		_json_file_ = open(_file_list[cnt_itr], 'r')
		_json_string_ = _json_file_.read()

		d = json.loads(str(_json_string_))

		Analyze_Content(d)
	
	
#####################################

#Main ()
#Description: Start of the Analysis Script
#Input : None
#Output : None

####################################

def Main():

	global ana2_output
	global ana3_output
	global ana4_output
	global ana5_output
	global tweet_anger
	global tweet_anticipation
	global tweet_disgust
	global tweet_fear
	global tweet_joy
	global tweet_sadness
	global tweet_suprise
	global tweet_trust

	global tweet_positive
	global tweet_negative
	global tweet_neutral

	global positive_recur 
	global negative_recur
	global neutral_recur
	global max_retweet_count
	global t1
	global t2
	global t3
	global t4
	global t5
	global t6
	global t7
	global t8
	global t9
	global t10
	global t11
	global _sentiment_list_
	global Total_emotion_count
	global Total_Tweets
	global Total_senti_Tweets

	#Parse the Twitter tweets
	parser = argparse.ArgumentParser()
	parse_result = Parse_CommandLine(parser)

	#get Current Date to create folders based on Time
	d0 = datetime.now()
	cur_time = str(d0.time())
	Cur_date = str(d0.date())

	#Validate the Entered Date format is valid
	validate_format(parse_result.minday)
	validate_format(parse_result.maxday)

	#Get the Valid Range of teh dates to be analyzed
	min_day, max_day = get_Daterange(parse_result.minday,parse_result.maxday,Cur_date)

#############################  Analysis 1  [start] ######################
	ofile  = open(r"./Analysis_1.csv", "wb")
	ana1_writer = csv.writer(ofile, delimiter='	', quotechar='', quoting=csv.QUOTE_NONE, escapechar=" ")

	Analysis1_Heading = " Emotion Expressed during these time " + "," + \
	"Which all region's user does comment on the " + \
	parse_result.Search_term + "," + \
	"At this time Tweet is towards " + parse_result.Search_term + \
	" ??/ Positive??(1-5)" + "," + \
	"Are they too harsh/Negative on the " + \
	parse_result.Search_term + "??(1-5)" + "," + \
	"Is this a Neutral tweet(1-5)"

	ana1_writer.writerow(Analysis1_Heading)
###############################  Analysis 1 [End] ######################

	cnt = 0 # To test Single Folder

	#Get the list of folders in the ./Output folder
	folder_list = Load_tweetFolder(min_day, max_day)
	
	File_list = []

	_sentiment_list_ = create_sentiment_list()

	for direc in folder_list:
		cnt += 1
		File_list = Load_Files(direc,parse_result.Search_term)
		
		if len(File_list) > 0:
			Analyze_Files(File_list,len(File_list))
		else: continue

###########################################################
#Analysis 3 [Start]
		ofile_ana3  = open(r"./Analysis_3.csv", "w")
		ana3_writer = csv.writer(ofile_ana3, delimiter='	', quotechar='', quoting=csv.QUOTE_NONE, escapechar=" ")

		Analysis3_Heading = "OVer the Range of Dates " + "," + \
		"% change in Anger " + "," + \
		"% change in Anticipation" + "," + \
		"% change in Disgust" + "," + \
		"% change in Fear" + "," + \
		"% change in Joy" + "," + \
		"% change in Sadness" + "," + \
		"% change in Suprise" + "," + \
		"% change in Trust" + "," + \
		"Total Number of Emotions"

		ana3_writer.writerow(Analysis3_Heading)
		
		if Total_emotion_count == 0:
			Total_emotion_count = 1
		
		ana3_output += str(direc.split('./Output/')[1]) + "," + \
			str((tweet_anger - t1)/Total_emotion_count) + "," + \
			str((tweet_anticipation - t2)/Total_emotion_count) + \
			"," + \
			str((tweet_disgust - t3)/Total_emotion_count) + "," + \
			str((tweet_fear - t4)/Total_emotion_count) + "," + \
			str((tweet_joy - t5)/Total_emotion_count) + "," + \
			str((tweet_sadness - t6)/Total_emotion_count) + "," + \
			str((tweet_suprise - t7)/Total_emotion_count) + "," + \
			str((tweet_trust - t8)/Total_emotion_count) + "," + \
			str(Total_emotion_count) + "\n"
		
		t1 = tweet_anger
		t2 = tweet_anticipation
		t3 = tweet_disgust
		t4 = tweet_fear
		t5 = tweet_joy
		t6 = tweet_sadness
		t7 = tweet_suprise
		t8 = tweet_trust
		ana3_writer.writerow(ana3_output)

		
#Analysis 3 [End]
###########################################################

###########################################################
#Analysis 4 [Start]
		ofile_ana4  = open(r"./Analysis_4.csv", "w")
		ana4_writer = csv.writer(ofile_ana4, delimiter='	', quotechar='', quoting=csv.QUOTE_NONE, escapechar=" ")

		Analysis4_Heading = "Date " + "," + \
		"Change in Positive comments " + "," + \
		"Change in Harsh comments" + "," + \
		"People changing being neutral" + "," + \
		"Sentimental Tweet count for the day"

		ana4_writer.writerow(Analysis4_Heading)
		
		Total_senti_Tweets = (positive_recur - t9) + (negative_recur - t10) + (neutral_recur - t11)

		ana4_output += str(direc.split('./Output/')[1]) + "," + \
			str((positive_recur - t9)/Total_senti_Tweets) + "," + \
			str((negative_recur - t10)/Total_senti_Tweets) + "," + \
			str((neutral_recur - t11)/Total_senti_Tweets) + "," + \
			str(Total_senti_Tweets) + "\n"
		
		t9 = positive_recur
		t10 = negative_recur
		t11 = neutral_recur
		ana4_writer.writerow(ana4_output)
		Total_Tweets = 0
		Total_senti_Tweets = 0
		
#Analysis 4 [End]
#######################################################

#######################################################
#Analysis 5 [Start]
		ofile_ana5  = open(r"./Analysis_5.csv", "w")
		ana5_writer = csv.writer(ofile_ana5, delimiter='	', quotechar='', quoting=csv.QUOTE_NONE, escapechar=" ")

		Analysis5_Heading = "Date " + "," + \
		"Most Tweeted Tweet of the day " + "," + \
		"Retweeted Count"


		ana5_writer.writerow(Analysis5_Heading)

		
		_engagement_analysis_ = {'Most Retweeted Tweets':"" , 'Retweeted Count':""}
		
		ana5_output += str(direc.split('./Output/')[1]) + "," + \
		str(_engagement_list_[0]['Most Retweeted Tweets']) + "," + \
		str(_engagement_list_[0]['Retweeted Count']) + "\n"

		ana5_writer.writerow(ana5_output)


		max_retweet_count = 0

#Analysis 5 [End]
########################################################
		#test for one folde, change cnt == 2 for two folders
		#if cnt == 1:
			#break


################################################################
#Analysis 2 [Start]

	ofile_ana2  = open(r"./Analysis_2.csv", "w")
	ana2_writer = csv.writer(ofile_ana2, delimiter='	', quotechar='', quoting=csv.QUOTE_NONE, escapechar=" ")

	Analysis2_Heading = "Anger towards " + parse_result.Search_term + \
	"," + "Anticipating on " + parse_result.Search_term + "," + \
	"Disgusting tweets on " + parse_result.Search_term + "," + \
	"Fear of " + parse_result.Search_term + "," + \
	"Joy/Happy about " + parse_result.Search_term + "," + \
	"Being Sad on " + parse_result.Search_term + "," + \
	parse_result.Search_term + " being Suprise!! " + "," + \
	" In " + parse_result.Search_term + " We Trust!!!"

	ana2_writer.writerow(Analysis2_Heading)

	ana2_output += \
		str(tweet_anger) + "," + \
		str(tweet_anticipation) + "," + \
		str(tweet_disgust) + "," + \
		str(tweet_fear) + "," + \
		str(tweet_joy) + "," + \
		str(tweet_sadness) + "," + \
		str(tweet_suprise) + "," + \
		str(tweet_trust) + "\n"

	ana2_writer.writerow(ana2_output)

	ofile_ana2.close()

#Analysis 2 [End]
#################################################################
	
#########################################################
#Analysis 1 [Start]

	#print("\n row output : ", csv_output)
	ana1_writer.writerow(str(csv_output))
	ofile.close()	

#Analysis 1 [End]
#####################################################
	

	ofile_ana3.close()
	ofile_ana4.close()
	ofile_ana5.close()

#Trigger Main()
if __name__ == "__main__":
	Main()

