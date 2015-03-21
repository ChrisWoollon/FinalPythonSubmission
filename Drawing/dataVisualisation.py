#import modules
from graphics import *
from random import randint

#initialise window
window = GraphWin("Visualisation", 1000, 1000)

#function for bubble sorting the data entries
def bubbleSort(nums):
    for passnum in range(len(nums)-1,0,-1):
        for i in range(passnum):
            if nums[i]>nums[i+1]:
                temp = nums[i]
                nums[i] = nums [i+1]
                nums[i+1] = temp
    return nums    

#function to draw visualisation
def draw():
    #create new array to store data and open data from file, storing it line-by-line in the array and then bubble sorting the whole array
    data = []
    counter = 0
    datafile = open("data.txt","r")
    for line in datafile:
        val = float(line)       
        data.append(val)
    data = bubbleSort(data)

    #loop backwards through the array from largest to smallest value and draw a circle on the screen with size and shade corresponding to the data value
    for item in reversed(data):
        posX = randint(50,950)
        posY = randint(50,950)
        print(item)
        counter+=1
        drawing = Circle(Point(posX,posY),item)
        drawing.setFill(color_rgb(255-(item*2.55), 255-(item*2.55), 255-(item*2.55)))
        drawing.draw(window)

#loop to allow user to click and redraw the array as much as they like without restarting the program        
while True:
    background = Rectangle(Point(0,0),Point(1000,1000))
    background.setFill(color_rgb(255,255,255))
    background.draw(window)
    draw()
    window.getMouse()