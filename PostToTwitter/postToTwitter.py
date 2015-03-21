#import modules
import twitter, datetime
import re
import urllib
import urllib2
from random import randint

#open file containing twitter credentials and store them in an array
file = open("twitterAPICode.txt")
cred = file.readline().strip().split(',')

#open the Chrome history database
h = open("/Users/cwoollon/Library/Application Support/Google/Chrome/Default/Current Session")

#store the contents of history in a variable and close the file
data = h.read()
h.close()

#declare strings to use in searching through data for url, then user rfind to search for the last instance of "http" in data, then find the end of the url by finding the first binary character in data after the "http" string 
startindex = data.rfind("http")
endindex = data.find(chr(0),startindex)

url = data[startindex:endindex]

print(url)

#open the url that was found and store its html
response = urllib2.urlopen(url)
html = response.read()
print(str(html) + " " + str(url)) 

#find the title tags in the html and store the string between them
findPageTitle = html.find("<title>")
findPageTitleEnd = html.find("</title>")

title = html[findPageTitle:findPageTitleEnd]
title = title.replace("<title>", "")
print(title)

#specify twitter credentials to use with api   
api = twitter.Api(consumer_key=cred[0], consumer_secret=cred[1], access_token_key=cred[2], access_token_secret=cred[3])

#get current time
timestamp = datetime.datetime.utcnow()

#array of strings to select from randomly to avoid duplicate tweets
texts  = ["I really like ", "I'm loving a bit of ", "There's something special about ", "I'm so down with "]

#post tweet
twitterResponse = api.PostUpdate(texts[randint(0,3)] + title)

print("Status updated to: " + twitterResponse.text)