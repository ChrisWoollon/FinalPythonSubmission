import urllib
import urllib2
import wikipedia
from BeautifulSoup import BeautifulSoup
from random import randint

file = open("StopWords.txt")
stopwords = file.readlines()

file = open("swearWords.txt")
swearWords = file.readlines()

file = open("positive-words.txt")
positiveWords = file.readlines()

file = open("negative-words.txt")
negativeWords = file.readlines()

botFeelings = ["good", "bad", "okay", "meh", "excellent", "amazing", "aweful"]
botIsFeeling = botFeelings[randint(0,6)]

def filterStopWords(output):
    for word in stopwords:
        if input.find(word.strip()) != -1:
            output = output.replace(" " + word.strip() + " ", " ")
    for word in swearWords:
        if input.find(word.strip()) != 1:
            output = output.replace(" " + word.strip() + " ", " <bleep> ")
    return output


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



while True:    
    input = raw_input("Hey! What's your name? ")
    filtered = (" " + input.lower() + " ")        
    
    filtered = filterStopWords(filtered)

    filtered = filtered.replace("name", " ")
    filtered = filtered.replace("called", " ")
    filtered = filtered.replace("<bleep>", "")
    filtered = " ".join(filtered.split())
    
    
    if filtered == "":
        print("Tell me your name!")
    else:        
        input = raw_input("Hi " + filtered + "! How are you today? ")
    feeling = (" " + input.lower() + " ")    
        
    
    feeling, feelingPositive = identifyPositiveWords(feeling)
    feeling = " ".join(feeling.split())
    
    if(feelingPositive == True):
        input = raw_input("I'm glad you're feeling " + feeling + " today! What are you thinking about? ")
    elif(feelingPositive == False):
        input = raw_input("I'm sorry to hear you're feeling " + feeling + " today :( What are you thinking about? ") 
        
        
    topic = (" " + input.lower() + " ")
    if (topic.strip() == "how are you?"):
        print("I am feeling forgetful today.")
    else:

        topic = filterStopWords(topic)
        topic = " ".join(topic.split())
    
        while (topic == ""):
            input = raw_input("There isn't really a discussion to be had there.. say something interesting already... ")
            topic = (" " + input.lower() + " ")    
            topic = filterStopWords(topic)
            topic = " ".join(topic.split())

        topic = wikipedia.WikipediaPage(topic)

    #    content = topic.summary
    #    print(content)

        print(wikipedia.summary(topic.title, sentences=1, chars=100, auto_suggest=True, redirect=True))
        while True:
            if topic != "":
                input = raw_input("what an interesting topic " + topic.title + " is. What else are you thinking about? ")
            else:
                input = raw_input("what else are you thinking about? ")
            topic = (" " + input.lower() + " ")  
            print(topic)
            if (topic.strip() == "how are you?"):
                print("I am feeling " + botIsFeeling + " today.")
                topic = ""
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
