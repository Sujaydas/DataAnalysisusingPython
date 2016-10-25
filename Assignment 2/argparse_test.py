#!/usr/bin python

#import sentiment_mod as s

'''
import argparse
parser = argparse.ArgumentParser()
parser.parse_args()
'''

'''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)

'''

'''
import argparse
parser = argparse.ArgumentParser(description='This is a PyMOTW sample program')
print(parser)

'''

'''
import urlparse
import argparse
import os
import datetime
import date
'''

'''
def fib(n):
	a,b = 0,1
	for i in range(n):
		a, b = b, a+b
	return a

#def Main():
parser = argparse.ArgumentParser()
parser.add_argument("num", help="Fibonacci number need to ne" + \
	"calculate", type = int)
parser.add_argument("-o","--options", help="Output the " + \
	"result ",action="store_true")
args = parser.parse_args()

result = fib(args.num)
print("The "+str(args.num)+"th fibo is "+str(result))
	
if args.options:
	f = open("das.txt","a")
	f.write(str(result) + '\n')


newpath = r'./sujay_test/' 
if not os.path.exists(newpath):
    os.makedirs(newpath)


day_time = datetime.today()
print(day_time)
'''

word = " das "

string = " asdklfaslidnf sadfhasuidasdfnakjsd nfuaidfasdf das dasfasdf asdfasdf"

count = string.count(word)

print(count)

Analysis1_Heading = " Emotion Expressed during these time " + "," + \
	"Which all region's user does comment on the " + \
	str(3312) + "," + \
	"At this time Tweet is towards " + str(12312332) + \
	" ??/ Positive??(1-5)" + "," + \
	"Are they too harsh/Negative on the " + \
	str(123123) + "??(1-5)" + "," + \
	"Is this a Neutral tweet(1-5)"
print(Analysis1_Heading)

'''
print(s.sentiment("This movie was awesome! The acting was great, plot was wonderful, and there were pythons...so yea!"))
print(s.sentiment("This movie was utter junk. There were absolutely 0 pythons. I don't see what the point was at all. Horrible movie, 0/10"))
'''

#d = open("./sujay_test/das.txt","w")
#d.write("success" + '\n')

#if __name__ == '__main':
#	Main()

