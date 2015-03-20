import twitter, datetime
import re
import urllib
import urllib2
from random import randint

file = open("twitterAPICode.txt")
cred = file.readline().strip().split(',')
h = open("/Users/cwoollon/Library/Application Support/Google/Chrome/Default/Current Session")

data = h.read()
h.close()
#print(data)

startindex = data.rfind("http")
endindex = data.find(chr(0),startindex)

url = data[startindex:endindex]

print(url)

response = urllib2.urlopen(url)
html = response.read()
print(str(html) + " " + str(url)) 

findPageTitle = html.find("<title>")
findPageTitleEnd = html.find("</title>")

title = html[findPageTitle:findPageTitleEnd]
title = title.replace("<title>", "")
print(title)

api = twitter.Api(consumer_key=cred[0], consumer_secret=cred[1], access_token_key=cred[2], access_token_secret=cred[3])

timestamp = datetime.datetime.utcnow()

texts  = ["I really like ", "I'm loving a bit of ", "There's something special about ", "I'm so down with "]

twitterResponse = api.PostUpdate(texts[randint(0,3)] + title)

print("Status updated to: " + twitterResponse.text)