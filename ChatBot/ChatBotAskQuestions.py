#import modules
import urllib
import urllib2
import wikipedia
from BeautifulSoup import BeautifulSoup
from random import randint

#Opens and stores lists of words
file = open("StopWords.txt")
stopwords = file.readlines()

file = open("swearWords.txt")
swearWords = file.readlines()

file = open("positive-words.txt")
positiveWords = file.readlines()

file = open("negative-words.txt")
negativeWords = file.readlines()

#produce array of possible chatbot sentiments and select one at random
botFeelings = ["good", "bad", "okay", "meh", "excellent", "amazing", "aweful"]
botIsFeeling = botFeelings[randint(0,6)]

#Function for filtering stopwords from input string
def filterStopWords(output):
    for word in stopwords:
        if input.find(word.strip()) != -1:
            output = output.replace(" " + word.strip() + " ", " ")
    for word in swearWords:
        if input.find(word.strip()) != 1:
            output = output.replace(" " + word.strip() + " ", " <bleep> ")
    return output

#function for filtering swearwords from input string
def identifyPositiveWords(output):
    for word in stopwords:
        if input.find(word.strip()) != -1:
            output = output.replace(" " + word.strip() + " ", " ")
    for word in swearWords:
        if input.find(word.strip()) != 1:
            output = output.replace(" " + word.strip() + " ", " ")
    output = " ".join(output.split())        
    for word in positiveWords:
        if output.find(word.strip()) >= 0:
            emotionGood = True
    for word in negativeWords:
        if output.find(word.strip()) >= 0:
            emotionGood = False    
    return(output, emotionGood)


#begin loop
while True:  
    #ask user their name and run it through functions to remove words other than their name  
    input = raw_input("Hey! What's your name? ")
    filtered = (" " + input.lower() + " ")        
    
    filtered = filterStopWords(filtered)

    filtered = filtered.replace("name", " ")
    filtered = filtered.replace("called", " ")
    filtered = filtered.replace("<bleep>", "")
    filtered = " ".join(filtered.split())
    
     #if the filtered string ends up blank, or the input was blank to begin with, then catch else carry on and ask the user how they are, running through the same functions to remove words and identify positive/negative sentiment
    if filtered == "":
        print("Tell me your name!")
    else:        
        input = raw_input("Hi " + filtered + "! How are you today? ")
    feeling = (" " + input.lower() + " ")    
        
    
    feeling, feelingPositive = identifyPositiveWords(feeling)
    feeling = " ".join(feeling.split())
    
     #seperate outputs depending on user sentiment. Ask the user what they're thinking about
    if(feelingPositive == True):
        input = raw_input("I'm glad you're feeling " + feeling + " today! What are you thinking about? ")
    elif(feelingPositive == False):
        input = raw_input("I'm sorry to hear you're feeling " + feeling + " today :( What are you thinking about? ") 
        
    #if the user asks the bot how they are at this stage, then the bot responds with "forgetful" and asks their name again, else carry on to wiki   
    topic = (" " + input.lower() + " ")
    if (topic.strip() == "how are you?"):
        print("I am feeling forgetful today.")
    else:
        #filter input again     
        topic = filterStopWords(topic)
        topic = " ".join(topic.split())
        
        #if input is blank after filtering, then catch and ask again
        while (topic == ""):
            input = raw_input("There isn't really a discussion to be had there.. say something interesting already... ")
            topic = (" " + input.lower() + " ")    
            topic = filterStopWords(topic)
            topic = " ".join(topic.split())

        #use wikipedia module to fetch corresponding wiki page to user's topic and print out the first sentence or 100 chars
        topic = wikipedia.WikipediaPage(topic)
        print(wikipedia.summary(topic.title, sentences=1, chars=100, auto_suggest=True, redirect=True))
        
        #introduce new loop to ensure the program doesn't start at the top again after question was ascked, and repeat asking questions and searching wiki
        while True:
            if topic != "":
                input = raw_input("what an interesting topic " + topic.title + " is. What else are you thinking about? ")
            else:
                input = raw_input("what else are you thinking about? ")
            
            #ask the bot how they are feeling and it responds with the randomly selected sentiment
            topic = (" " + input.lower() + " ")  
            if (topic.strip() == "how are you?"):
                print("I am feeling " + botIsFeeling + " today.")
                topic = ""
            #ask the bot what it is thinking about and it fetches a random wikipedia article    
            elif (topic.strip() == "what are you thinking about?"):
                myTopic = wikipedia.random(pages=1)
                print("I am thinking about " + myTopic)
                print(wikipedia.summary(myTopic, sentences = 1))
                topic = ""
            else:
                topic = filterStopWords(topic)
                topic = " ".join(topic.split())

                while (topic == ""):
                    input = raw_input("There isn't really a discussion to be had there... say something interesting already... ")
                    topic = (" " + input.lower() + " ")    
                    topic = filterStopWords(topic)
                    topic = " ".join(topic.split())


                topic = wikipedia.page(topic)
                print(wikipedia.summary(topic.title, sentences=1, auto_suggest=True, redirect=True))
        #    print(topic.content)
