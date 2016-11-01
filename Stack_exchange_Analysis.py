#!/usr/bin python

############################################

#Created by: Sujay Premkumar
#Date : 26 Oct 2016
#Reviwer : Spandan
#Purpose : Get the question and answer details over the timeline and perform analysis about the topic

########################################### 

####:Libraries #############################
import argparse
import time
from datetime import datetime,date,timedelta
import os
import requests

import sys
reload(sys)
import json
import csv
import re
import glob



#######  Globals ########################
sys.setdefaultencoding('utf-8')

question_format = {"page":"" , "pagesize":"" , "fromdate":"", "todate":"", "order":"", "min":"" , "max":"" , "sort":"" , "tagged":"" }

question_format1 = {"page":"" , "pagesize":"" , "fromdate":"", "todate":"", "order":"", "min":"" , "max":"" , "sort":"" , "tagged":"" }

user_info = {"name":"", "user_id":"", "link":"", "badge_counts":{"gold":"","silver":"","bronze":""}}

#User_info_list = [{"name":"", "user_id":"", "link":"", "badge_counts":{"gold":"","silver":"","bronze":""}}]

User_info_list = [1]


Cur_day = 0;Cur_month = 0;Cur_date = 0;d0 = 0;Cur_time_st = 0

total_questions = 0; answer_count = 0; 
Max_question_id = 0; Question_text = ""

Analysis1_csv_output = ""
ana1_output = ""
ana2_output = ""
ana3_output = ""
ana4_output = ""
ana5_output = ""
ana3_writer = None
ana4_writer = None
ana2_writer = None
t1 =0;

Text_top = ""

#########################################################


#######################################

#Func: Parse_CommandLine()
#Description:  Create search term and File name argument for the command line
#Inout: parser - parser object which adds the argument
########################################

def Parse_CommandLine(parser):

	parser.add_argument("Topic", help="Topic to be queried " + \
		"to Stack Exchange API")
	parser.add_argument("File_Name", help="Provide the file name to be " + \
		"saved")
	
	args = parser.parse_args()
	print("The Topic to be analyzed is "+ args.Topic)
	return args

#######################################

#Func: Get_last_30_day_range()
#Description:  Get last 30th day from current day
#Inout: Cur_day - ACtual today
#	Cur_month - Current Month
########################################


def Get_last_30_day_range(Cur_day,Cur_month):

	if not Cur_day == 30:
		return Cur_day, Cur_month - 1
	else:
		return 1, Cur_month

#######################################

#Func: Get_last_7_day_range()
#Description:  Get last 7th day day from current day
#Inout: Cur_day - ACtual today
#	Cur_month - Current Month
########################################

def Get_last_7_day_range(Cur_day,Cur_month):

	if Cur_day == 7:
		return 1, Cur_month
	elif Cur_day < 7:
		return (30 - (7 - Cur_day)), Cur_month - 1
	else:
		return Cur_day - 7, Cur_month

#######################################

#Func: Create_URL()
#Description:  Get the final URL for the question request
#Inout: Base_URL  - Starting URL for the question request
#	Analysis_URL - Appended final url to be sent to the stack api
########################################


def Create_URL(Base_URL):
	Analysis_URL = Base_URL + "questions?key=1ki9ly)MhX2ibM3oiE7dLA((&site=stackoverflow"

	if not question_format["page"] == "":
		Analysis_URL += "&page=" + question_format["page"]
	
	if not question_format["pagesize"] == "":
		Analysis_URL += "&pagesize=" + question_format["pagesize"]

	if not question_format["fromdate"] == "":
		Analysis_URL += "&fromdate=" + question_format["fromdate"]

	if not question_format["todate"] == "":
		Analysis_URL += "&todate=" + question_format["todate"]

	if not question_format["order"] == "":
		Analysis_URL += "&order=" + question_format["order"]

	if not question_format["min"] == "":
		Analysis_URL += "&min=" + question_format["min"]

	if not question_format["max"] == "":
		Analysis_URL += "&max=" + question_format["max"]

	if not question_format["sort"] == "":
		Analysis_URL += "&sort=" + question_format["sort"]

	if not question_format["tagged"] == "":
		Analysis_URL += "&tagged=" + question_format["tagged"]

	return Analysis_URL

#######################################

#Create_NOAnswer_URL
#Description:  Get the final URL for the No Answer request
#Inout: Base_URL  - Starting URL for the No ANSWER request
#	Analysis_URL - Appended final url to be sent to the stack api
########################################

	
def Create_NOAnswer_URL(Base_URL):
	Analysis_URL = Base_URL + "questions/no-answers?key=1ki9ly)MhX2ibM3oiE7dLA((&site=stackoverflow"

	if not question_format["page"] == "":
		Analysis_URL += "&page=" + question_format["page"]
	
	if not question_format["pagesize"] == "":
		Analysis_URL += "&pagesize=" + question_format["pagesize"]

	if not question_format["fromdate"] == "":
		Analysis_URL += "&fromdate=" + question_format["fromdate"]

	if not question_format["todate"] == "":
		Analysis_URL += "&todate=" + question_format["todate"]

	if not question_format["order"] == "":
		Analysis_URL += "&order=" + question_format["order"]

	if not question_format["min"] == "":
		Analysis_URL += "&min=" + question_format["min"]

	if not question_format["max"] == "":
		Analysis_URL += "&max=" + question_format["max"]

	if not question_format["sort"] == "":
		Analysis_URL += "&sort=" + question_format["sort"]

	if not question_format["tagged"] == "":
		Analysis_URL += "&tagged=" + question_format["tagged"]

	return Analysis_URL	



#######################################

#Createreset_question_format()
#Description:  Resets the questoin format 
########################################


def reset_question_format():
	global question_format

	question_format["page"] = ""
	question_format["pagesize"] = ""
	question_format["fromdate"] = ""
	question_format["todate"] = ""
	question_format["order"] = ""
	question_format["min"] = ""
	question_format["max"] = ""
	question_format["sort"] = ""
	question_format["tagged"] = ""


#######################################

#Createreset_question_format1()
#Description:  Resets the questoin format 1
########################################


def reset_question_format1():
	global question_format1

	question_format1["page"] = ""
	question_format1["pagesize"] = ""
	question_format1["fromdate"] = ""
	question_format1["todate"] = ""
	question_format1["order"] = ""
	question_format1["min"] = ""
	question_format1["max"] = ""
	question_format1["sort"] = ""
	question_format1["tagged"] = ""


def set_question_format(key, value):
	global question_format

	question_format[key] = str(value)

def set_question_format1(key, value):
	global question_format1

	question_format1[key] = str(value)


def print_question_format():
	print(question_format)



#######################################

#save_stack_details()
#Description:  Saves the json response in file
#	stack_json -  json to be saved
#	Analysis -  for which analysis the json is for
#	Topic - for which topic the json is received		 
########################################

def save_stack_details(stack_json,Analysis,Topic):

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

	newpath = newpath +"/" + Analysis

	if not os.path.exists(newpath):
		try:
			os.makedirs(newpath)
		except OSError as exception:
        		if exception.errno != errno.EEXIST:
				print("Error during creating Search Directory")

	newpath = newpath +"/" + Topic

	if not os.path.exists(newpath):
		try:
			os.makedirs(newpath)
		except OSError as exception:
        		if exception.errno != errno.EEXIST:
				print("Error during creating Search Directory")

	newpath = newpath +"/" + Topic + "_" + str(Cur_time_st.split(' ')[1]) + ".json"

	_json_file_ = open(newpath, 'w')
	_json_file_.write(str(stack_json.text))


def get_folder_list():
	l = ["./Output" + "/" + name for name in os.listdir("./Output") \
if os.path.isdir("./Output")]

	return sorted(l)	



def get_File_list(direc,srch_term):
	file_list = []
	
	path = direc + "/" + srch_term + "/*.json"
	
	#Get the list of files in the location specified
	file_list = glob.glob(path)
	
	return file_list


#######################################

#Analyze_Content()
#Description:  Get Answer count, total questions asked on that day, what is the actual question, 	 
#	d -  the json reponse in string
########################################


def Analyze_Content(d):

	global total_questions
	global answer_count
	global Max_question_id
	global Question_text

	temp_cnt = 0
	question_count = 0

	for file_itr in d["items"]:
		temp_cnt = file_itr["answer_count"]
		ques_id = file_itr["question_id"]

		question_count += 1

		if answer_count < temp_cnt:
			answer_count = temp_cnt
			Max_question_id = ques_id
			Question_text = file_itr["title"]
		

	total_questions += question_count



#######################################

#create_user_url()
#Description:  Create request URL for the user request
#	Base_URL -  Starting URL to send for user info request
########################################


def create_user_url(Base_URL):
	Analysis_URL = Base_URL + "key=1ki9ly)MhX2ibM3oiE7dLA((&site=stackoverflow"

	if not question_format1["page"] == "":
		Analysis_URL += "&page=" + question_format1["page"]
	
	if not question_format1["pagesize"] == "":
		Analysis_URL += "&pagesize=" + question_format1["pagesize"]

	if not question_format1["fromdate"] == "":
		Analysis_URL += "&fromdate=" + question_format1["fromdate"]

	if not question_format1["todate"] == "":
		Analysis_URL += "&todate=" + question_format1["todate"]

	if not question_format1["order"] == "":
		Analysis_URL += "&order=" + question_format1["order"]

	if not question_format1["min"] == "":
		Analysis_URL += "&min=" + question_format1["min"]

	if not question_format1["max"] == "":
		Analysis_URL += "&max=" + question_format1["max"]

	if not question_format1["sort"] == "":
		Analysis_URL += "&sort=" + question_format1["sort"]

	if not question_format1["tagged"] == "":
		Analysis_URL += "&tagged=" + question_format1["tagged"]

	return Analysis_URL



#######################################

#create_user_url()
#Description:  Create request URL for the answer request
#	Base_URL -  Starting URL to send for user info request
########################################

def Create_answer_URL(Base_URL):
	Analysis_URL = Base_URL + "answers?key=1ki9ly)MhX2ibM3oiE7dLA((&site=stackoverflow"

	if not question_format["page"] == "":
		Analysis_URL += "&page=" + question_format["page"]
	
	if not question_format["pagesize"] == "":
		Analysis_URL += "&pagesize=" + question_format["pagesize"]

	if not question_format["fromdate"] == "":
		Analysis_URL += "&fromdate=" + question_format["fromdate"]

	if not question_format["todate"] == "":
		Analysis_URL += "&todate=" + question_format["todate"]

	if not question_format["order"] == "":
		Analysis_URL += "&order=" + question_format["order"]

	if not question_format["min"] == "":
		Analysis_URL += "&min=" + question_format["min"]

	if not question_format["max"] == "":
		Analysis_URL += "&max=" + question_format["max"]

	if not question_format["sort"] == "":
		Analysis_URL += "&sort=" + question_format["sort"]

	if not question_format["tagged"] == "":
		Analysis_URL += "&tagged=" + question_format["tagged"]

	return Analysis_URL
	

#######################################

#get_user_info()
#Description:  Get User info for the particular user_id
#	user_id -  user id for whom the user info need to be taken
########################################

	
def get_user_info(user_id):
	Base_url = "https://api.stackexchange.com/2.2/users/"
	
	new_url = Base_url + str(user_id) + "?"
	
	order = "desc"
	set_question_format1("order",order)

	sort = "reputation"
	set_question_format1("sort",sort)

	search_url = create_user_url(new_url)

	r = requests.get(search_url)


	d = json.loads(str(r.text))
	return d



#######################################

#get_answer_info()
#Description:  Get answer info for the particular answer id
#	answer_id -  answer id for which  the answer info need to be taken
########################################


def get_answer_info(answer_id):
	Base_url = "https://api.stackexchange.com/2.2/posts/"
	
	new_url = Base_url + str(answer_id) + "?"
	
	order = "desc"
	set_question_format1("order",order)

	sort = "votes"
	set_question_format1("sort",sort)

	search_url = create_user_url(new_url)

	r = requests.get(search_url)

	d = json.loads(str(r.text))
	if d["items"][0]:
		return d["items"][0]["link"]
	else:
		return ""

	
def Analyse_Content5(d):

	global ana5_output
	global ana5_writer

	cnt = 0
	for file_itr in d["items"]:
		Title = file_itr["title"]
		Link = file_itr["link"]
		View_count = file_itr["view_count"]
		ques_id = file_itr["question_id"]

		ana5_output += str(Title.replace(',',' ')) + "," + \
		str(Link) + "," + \
		str(View_count) + "," + \
		str(ques_id) + "\n"


		
def Analyse_Content2(d):

	global ana2_output
	global ana2_writer

	cnt = 0
	for file_itr in d["items"]:
		answer_id = file_itr["answer_id"]
		ques_id = file_itr["question_id"]
		score = file_itr["score"]

		answer_link = get_answer_info(answer_id)
		ana2_output += str(answer_id) + "," + \
		str(ques_id) + "," + \
		str(answer_link) + "," + \
		str(score) + "\n"

		
def Analyze_Content3(d):

	global Text_top
	global Score_count
	global ana3_output
	global ana3_writer
	global ana4_output

	temp_scorecnt = 0
	question_count = 0
	cnt = 0

	#global user_info
	global User_info_list


	badge_counts = {"gold":"","silver":"","bronze":""}
	for file_itr in d["items"]:
		Text = file_itr["title"]
		ques_id = file_itr["question_id"]
		link = file_itr["link"]
		temp_scorecnt = file_itr["score"]
		user_id = file_itr["owner"]["user_id"]
			
		user = get_user_info(user_id)
		user_name = user["items"][0]["display_name"]
		
		user_info["name"] = user_name
		user_info["user_id"] = user_id
		user_info["link"] = user["items"][0]["link"]
		badge_counts["gold"] = user["items"][0]["badge_counts"]["gold"]
		badge_counts["silver"] = user["items"][0]["badge_counts"]["silver"]
		badge_counts["bronze"] = user["items"][0]["badge_counts"]["bronze"]
		user_info["badge_counts"] = badge_counts

		ana4_output += str(user_info["name"]) + "," + \
		str(user_info["user_id"]) + "," + \
		str(user_info["link"]) + "," + \
		str(badge_counts["gold"]) + "," + \
		str(badge_counts["silver"]) + "," + \
		str(badge_counts["bronze"]) + "\n"

		cnt += 1
		if cnt > 25: break
		
		ana3_output += str(Text) + "," + \
		str(ques_id) + "," + \
		str(link) + "," + \
		str(temp_scorecnt) + "," + \
		str(user_name) + "," + \
		str(user_id) + "\n"
		


def Analyze_Files(_file_list,_list_length,number):

	global ana3_output
	global ana4_output
	global User_info_list
	for cnt_itr in range(0,_list_length,1):
	#for cnt_itr in range(0,1,1): # test loop for analysing only few files
	    	print("File Processing is : ", _file_list[cnt_itr])
		_json_file_ = open(_file_list[cnt_itr], 'r')
		_json_string_ = _json_file_.read()

		if _json_string_ == "": continue

		d = json.loads(str(_json_string_))
		ana2_output = ""

		if number == 1:
			Analyze_Content(d)
		elif number == 3:
			ana3_output = ""
			ana4_output = ""
			Analyze_Content3(d)
		elif number == 2:
			Analyse_Content2(d)
		elif number == 5:
			Analyse_Content5(d)
			ana5_writer.writerow(ana5_output)



def analyze5(Topic):

	global ana5_writer
	global ana5_output
	#Get the list of folders in the ./Output folder
	folder_list = get_folder_list()
	cnt = 0
		
	#Create CSV Files
	ofile_ana5  = open(r"./Analysis_5.csv", "w")
	ana5_writer = csv.writer(ofile_ana5, delimiter='	', quotechar='', quoting=csv.QUOTE_NONE, escapechar=" ")

	Analysis5_Heading = "Title of the Unanswered Question " + "," + \
		"Link of Unanswered Question " + "," + \
		"People viewed question but no answer yet" + "," + \
		"question id  "


	ana5_writer.writerow(Analysis5_Heading)


	for direc in folder_list:
		cnt += 1
		direc += "/Analysis_5"
		File_list = get_File_list(direc,Topic)

		if len(File_list) > 0:
			Analyze_Files(File_list,len(File_list),5)
		else: continue
	
	
def analyze2(Topic):

	global ana3_writer
	global ana3_output
	#Get the list of folders in the ./Output folder
	folder_list = get_folder_list()
	cnt = 0

	#Create CSV Files
	ofile_ana2  = open(r"./Analysis_2.csv", "w")
	ana2_writer = csv.writer(ofile_ana2, delimiter='	', quotechar='', quoting=csv.QUOTE_NONE, escapechar=" ")

	Analysis2_Heading = "Top answer ID " + "," + \
		"Top Question ID " + "," + \
		"Link of the answer" + "," + \
		"Score of the answer "


	ana2_writer.writerow(Analysis2_Heading)


	for direc in folder_list:
		cnt += 1
		direc += "/Analysis_2"
		#if cnt == 1: continue
		#print("directory in is : ", direc)
		File_list = get_File_list(direc,Topic)

		if len(File_list) > 0:
			Analyze_Files(File_list,len(File_list),2)
		else: continue

	ana2_writer.writerow(ana2_output)
	

def analyze3(Topic):

	global ana2_writer
	global ana2_output
	#Get the list of folders in the ./Output folder
	folder_list = get_folder_list()
	cnt = 0

	#Create CSV Files
	ofile_ana3  = open(r"./Analysis_3.csv", "w")
	ana3_writer = csv.writer(ofile_ana3, delimiter='	', quotechar='', quoting=csv.QUOTE_NONE, escapechar=" ")

	Analysis3_Heading = "Top Questions asked " + "," + \
		"Question ID " + "," + \
		"Link of the question" + "," + \
		"Score of the question " + "," + \
		"who asked the question " + "," + \
		"User ID of user  "


	ana3_writer.writerow(Analysis3_Heading)

	for direc in folder_list:
		cnt += 1
		direc += "/Analysis_3"

		File_list = get_File_list(direc,Topic)

		if len(File_list) > 0:
			Analyze_Files(File_list,len(File_list),3)
		else: continue

	

	ana3_writer.writerow(ana3_output)	

def analyze1(Topic):
	
	global total_questions
	global answer_count
	global Max_question_id
	global Question_text
 	global ana1_output
	global t1


	#Create CSV Files
	ofile_ana1  = open(r"./Analysis_1.csv", "w")
	ana1_writer = csv.writer(ofile_ana1, delimiter='	', quotechar='', quoting=csv.QUOTE_NONE, escapechar=" ")

	Analysis1_Heading = "Over the Range of Dates " + "," + \
		"% change in Number of Questions from previous " + "," + \
		"Total Number of questions for a day" + "," + \
		"Which is the top question asked " + "," + \
		"NUmber of Answers for top question " + "," + \
		"Top Voted question ID "


	ana1_writer.writerow(Analysis1_Heading)


	#Get the list of folders in the ./Output folder
	folder_list = get_folder_list()
	cnt = 0
	for direc in folder_list:
		cnt += 1
		
		direc += "/Analysis_1"

		File_list = get_File_list(direc,Topic)


		if len(File_list) > 0:
			Analyze_Files(File_list,len(File_list),1)
		else: continue

		ana1_output += str(direc.split('./Output/')[1].split('/')[0]) + "," + \
		str((total_questions - t1)/total_questions) + "," + \
		str(total_questions) + "," + \
		str(Question_text.replace(',',' ')) + "," + \
		str(answer_count) + "," + \
		str(Max_question_id) + "\n"
		
		t1 = total_questions
		ana1_writer.writerow(ana1_output)
	
		answer_count = 0;Max_question_id = 0;Question_text = ""
		total_questions = 0; ana1_output = ""


		#test for one folde, change cnt == 2 for two folders
		#if cnt == 2:
			#break
	
	ofile_ana1.close()

def Do_Analysis2(Base_URL,start_day, start_month,Topic):

	set_question_format("pagesize",100)

	pattern ='%Y-%m-%d'

	order = "desc"
	set_question_format("order",order)

	sort_by = "votes"
	set_question_format("sort",sort_by)

	print_question_format()

	Search_url_analysis2 = Create_answer_URL(Base_URL)

	r = requests.get(Search_url_analysis2)

	if r.status_code == 200:
		save_stack_details(r,"Analysis_2",Topic)
		analyze2(Topic)
	else:	
		print("Error happned during GET request, may be due to throttling")
	
	
def Do_Analysis3(Base_URL,start_day, start_month,Topic):

	set_question_format("pagesize",100)

	pattern ='%Y-%m-%d'
	
	order = "desc"
	set_question_format("order",order)

	min_sort = 5
	set_question_format("min",min_sort)

	sort_by = "votes"
	set_question_format("sort",sort_by)

	tag = Topic
	set_question_format("tagged",tag)

	print_question_format()

	Search_url_analysis3 = Create_URL(Base_URL)

	r = requests.get(Search_url_analysis3)

	if r.status_code == 200:
		save_stack_details(r,"Analysis_3",Topic)
		analyze3(Topic)
	else:	
		print("Error happned during GET request, may be due to throttling")


def Do_Analysis1(Base_URL,start_day, start_month,Topic):

	set_question_format("pagesize",100)
	pattern ='%Y-%m-%d'
	fromdate = "2016-" + str(start_month) + "-" + str(start_day)

	epoch = int(time.mktime(time.strptime(fromdate,pattern)))
	set_question_format("fromdate",epoch)
	epoch = int(time.mktime(time.strptime(Cur_date,pattern)))

	set_question_format("todate",epoch)
	
	order = "desc"
	set_question_format("order",order)

	min_sort = 5
	set_question_format("min",min_sort)

	sort_by = "creation"
	set_question_format("sort",sort_by)

	tag = Topic
	set_question_format("tagged",tag)

	print_question_format()

	Search_url_analysis1 = Create_URL(Base_URL)
	
	r = requests.get(Search_url_analysis1)

	if r.status_code == 200:
		save_stack_details(r,"Analysis_1",Topic)
		analyze1(Topic)
	else:	
		print("Error happned during GET request, may be due to throttling")


def Do_Analysis5(Base_URL,start_day, start_month,Topic):

	set_question_format("pagesize",100)
	
	order = "desc"
	set_question_format("order",order)

	sort_by = "creation"
	set_question_format("sort",sort_by)

	tag = Topic
	set_question_format("tagged",tag)

	print_question_format()

	Search_url_analysis5 = Create_NOAnswer_URL(Base_URL)

	r = requests.get(Search_url_analysis5)

	if r.status_code == 200:
		save_stack_details(r,"Analysis_5",Topic)

		analyze5(Topic)
	else:	
		print("Error happned during GET request, may be due to throttling")
	

#######################################

#DoAnalysis4()
#Description:  Create Analysis 4 csv file with the string value seprated by ,

########################################
	
def DoAnalysis4():

	#Create CSV Files
	ofile_ana4 = open(r"./Analysis_4.csv", "w")
	ana4_writer = csv.writer(ofile_ana4, delimiter='	', quotechar='', quoting=csv.QUOTE_NONE, escapechar=" ")

	Analysis4_Heading = "User of the MOst voted question " + "," + \
		"usr_id" + "," + \
		"Link of the User" + "," + \
		"Hard earned Gold Badges by the user  " + "," + \
		"silver badges earned by user " + "," + \
		"Bronze badges earned by the user "

	ana4_writer.writerow(Analysis4_Heading)

	ana4_writer.writerow(ana4_output)


#######################################

#Func: Create_Request_URL()
#Description:  Use the Search Term to create the Search URL to be passed for GET Request
#Inout: Search_term -  To be searched in the Stackoverflow search Bar
########################################


def Create_Request_URL(Topic):
	global question_format
	global Cur_day,Cur_month,Cur_date,d0,Cur_time_st

	#Create a Topic Search Request
	Base_URL = "https://api.stackexchange.com/2.2/"

	d0 = datetime.now()
	cur_time = str(d0.time())
	Cur_date = str(d0.date())
	Cur_time_st = d0.strftime("%Y-%m-%d %H:%M:%S")

	Cur_day = d0.day
	Cur_month = d0.month
	day_start30 = 0;month_start30 = 0
	day_start7 = 0;month_start7 = 0
	
	day_start30, month_start30 = Get_last_30_day_range(Cur_day,Cur_month)

	day_start7, month_start7 = Get_last_7_day_range(Cur_day,Cur_month)

######################################################
#Create Analysis 1 URL and do analysis 1

	reset_question_format()

	Do_Analysis1(Base_URL,day_start7, month_start7,Topic)
	

######################################################
######################################################
#Create Analysis 3

	reset_question_format()

	Do_Analysis3(Base_URL,day_start7, month_start7,Topic)
	

######################################################
#Create Analysis 2

	reset_question_format()
	reset_question_format1()
	
	Do_Analysis2(Base_URL,day_start7, month_start7,Topic)
	

######################################################

	DoAnalysis4()

	
	reset_question_format()
	reset_question_format1()
	
	Do_Analysis5(Base_URL,day_start7, month_start7,Topic)
	

#######################################

#Func: Main()
#Description: Start of the Script, Parses the command line arguments, Authenticate USer,  create a request URL, and save the stack details,   
#Inout: None 
########################################

def Main():

	#Parse the Stack Exchange topic
	parser = argparse.ArgumentParser()
	parse_result = Parse_CommandLine(parser)

	url = Create_Request_URL(parse_result.Topic)

#Trigger Main()
if __name__ == "__main__":
	Main()

