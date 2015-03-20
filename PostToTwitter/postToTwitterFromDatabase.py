import twitter, datetime
import re
import urllib
import urllib2
from random import randint
import sqlite3
import shutil

file = open("twitterAPICode.txt")
cred = file.readline().strip().split(',')
history = "/Users/cwoollon/Library/Application Support/Google/Chrome/Default/History"
h = open(history)
counter = 0
shutil.copyfile(history, "History")
historydb = "History"

console = sqlite3.connect(historydb)
cursor = console.cursor()

cursor.execute("SELECT * FROM urls ORDER BY visit_count DESC LIMIT 1;")

rows = cursor.fetchall()
for row in rows:
    print(rows[-1][2] + "------" + str(rows[-1][3]))

#viewCount = 0
#for row in rows: 
#    newViewCount = rows[counter][3]
#    
#    if(newViewCount > viewCount): 
#        viewCount = newViewCount
#        pageToPost = rows[counter][2]    
#    print(pageToPost)
#    counter+=1
#    
    
api = twitter.Api(consumer_key=cred[0], consumer_secret=cred[1], access_token_key=cred[2], access_token_secret=cred[3])

timestamp = datetime.datetime.utcnow()

texts  = ["I really like ", "I'm loving a bit of ", "There's something special about ", "I'm so down with "]

twitterResponse = api.PostUpdate(texts[randint(0,3)] + rows[-1][2])

print("Status updated to: " + twitterResponse.text)