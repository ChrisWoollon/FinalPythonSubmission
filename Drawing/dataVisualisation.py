from graphics import *
from random import randint


window = GraphWin("Visualisation", 1000, 1000)
    
def bubbleSort(nums):
    for passnum in range(len(nums)-1,0,-1):
        for i in range(passnum):
            if nums[i]>nums[i+1]:
                temp = nums[i]
                nums[i] = nums [i+1]
                nums[i+1] = temp
    return nums    

def draw():
    data = []
    counter = 0
    datafile = open("data.txt","r")
    for line in datafile:
        val = float(line)       
        data.append(val)
    data = bubbleSort(data)
#    for i in reversed(data):
#        print(i)
    for item in reversed(data):
        posX = randint(50,950)
        posY = randint(50,950)
        print(item)
        counter+=1
        drawing = Circle(Point(posX,posY),item)
        drawing.setFill(color_rgb(255-(item*2.55), 255-(item*2.55), 255-(item*2.55)))
        drawing.draw(window)

while True:
    background = Rectangle(Point(0,0),Point(1000,1000))
    background.setFill(color_rgb(255,255,255))
    background.draw(window)
    draw()
    window.getMouse()
    
    
    
    
    
#while True:
#    
#    data = []
#    datafile = open("data.txt","r")
#    for line in datafile:
#        val = float(line)       
#        data.append(val)
#    data = bubbleSort(data)
#    counter = 0;
#    
#        print(data)
#
#    for item in data:
#        posX = randint(50,950)
#        posY = randint(50,950)
#        print(item)
#        counter+=1
#        drawing = Circle(Point(posX,posY),item)
#        drawing.setFill(color_rgb(255-(item*2.55), 255-(item*2.55), 255-(item*2.55)))
#        drawing.draw(window)
