#import modules
import twitter, datetime
import re
import urllib
import urllib2
from random import randint
import sqlite3
import shutil

#open file containing twitter credentials and store them in an array
file = open("twitterAPICode.txt")
cred = file.readline().strip().split(',')

#open the Chrome history database
history = "/Users/cwoollon/Library/Application Support/Google/Chrome/Default/History"
h = open(history)

#Copy history database into working directory
shutil.copyfile(history, "History")
historydb = "History"

#connect to new database and read all entries from 'urls' table ordered by visit count in descending order and select just the row at the top of the table with largest visit count
console = sqlite3.connect(historydb)
cursor = console.cursor()
cursor.execute("SELECT * FROM urls ORDER BY visit_count DESC LIMIT 1;")

#store the row in a variable and print out the page title and the view count
rows = cursor.fetchall()
for row in rows:
    print(rows[-1][2] + "------" + str(rows[-1][3]))

#older code to increment through the whole table to find the largest view count
# counter = 0
#viewCount = 0
#for row in rows: 
#    newViewCount = rows[counter][3]#    
#    if(newViewCount > viewCount): 
#        viewCount = newViewCount
#        pageToPost = rows[counter][2]    
#    print(pageToPost)
#    counter+=1
    
#specify twitter credentials to use with api   
api = twitter.Api(consumer_key=cred[0], consumer_secret=cred[1], access_token_key=cred[2], access_token_secret=cred[3])

#get current timestamp
timestamp = datetime.datetime.utcnow()

#array of strings to select from randomly to avoid duplicate tweets
texts  = ["I really like ", "I'm loving a bit of ", "There's something special about ", "I'm so down with "]

#post tweet
twitterResponse = api.PostUpdate(texts[randint(0,3)] + rows[-1][2])

print("Status updated to: " + twitterResponse.text)