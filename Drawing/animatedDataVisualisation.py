#import modules
from graphics import *
from random import randint

#initialise window and declare variables and lists
window = GraphWin("Visualisation", 1000, 1000)
datafile = open("data.txt","r")
posX = []
posY = []
data = []
circles = []

#function for bubble sorting the data entries
def bubbleSort(nums):
    for passnum in range(len(nums)-1,0,-1):
        for i in range(passnum):
            if nums[i]>nums[i+1]:
                temp = nums[i]
                nums[i] = nums [i+1]
                nums[i+1] = temp
    return nums    



#function to draw initial circles
def draw():
    global data
    global circles
    #create new array to store data and open data from file, storing it line-by-line in the array and then bubble sorting the whole array
    for line in datafile:
        val = float(line)       
        data.append(val)
    data = bubbleSort(data)

    #loop backwards through the array from largest to smallest value and draw a circle on the screen with size and shade corresponding to the data value
    for item in reversed(data):
        posX = randint(50,950)
        posY = randint(50,950)
        drawing = Circle(Point(posX,posY),item)
        drawing.setFill(color_rgb(255-(item*2.55), 255-(item*2.55), 255-(item*2.55)))
        drawing.draw(window)
        #store each circle object in a list
        circles.append(drawing)

#function to animate circles
def animate():
    global data
    global circles
    animateCounter = 0    
    #loop through list of circles objects and move them randomly with more possible movement for circles the larger they get
    for drawing in circles:
        circles[animateCounter].move(randint((-1*(100-int(data[animateCounter])))/10,(1*(100-int(data[animateCounter])))/10),randint((-1*(100-int(data[animateCounter])))/10,(1*(100-int(data[animateCounter])))/10))
        animateCounter+=1
    
    
#loop to allow user to click and redraw the array as much as they like without restarting the program   
background = Rectangle(Point(0,0),Point(1000,1000))
background.setFill(color_rgb(255,255,255))
background.draw(window) 
draw()

while True:
    animate()
#    window.getMouse()