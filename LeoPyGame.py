
from turtle import Turtle, setup
width, height = 500, 400

setup(1400, 1000)

mouse = Turtle()
cheeseDrawMan = Turtle()
rectT = Turtle()
mouse.penup()
mouse.speed(1)
mouse.shapesize(3)


def drawCheese():
    cheeseDrawMan.hideturtle()


def cheeseGeneration():
    print("hey future leo do the code haha suffer")
cheeseGeneration()




s = mouse.getscreen()
s.screensize(448, 252)
s.title("kitchen")

s.bgcolor("#d6be54")
Upok = True
distance = 10

def mouseUp():
   
    mouse.speed(50)
    mouse.setheading(90)
    mouse.speed(1)

def mouseRight():

    mouse.speed(50)  
    mouse.setheading(0)
    mouse.speed(1)
    

def mouseLeft():

    mouse.speed(1000)
    mouse.setheading(180)
    mouse.speed(1)
   

def mouseDown():

    mouse.speed(1000)
    mouse.setheading(270)
    mouse.speed(1)
    

def makeBoundary():
    rectT.speed(100)
    rectT.penup()
    rectT.forward(width)
    rectT.left(90) 
    rectT.pendown()
    rectT.forward(height)
    rectT.left(90)
    rectT.forward(width*2)
    rectT.left(90)
    rectT.forward(height*2)
    rectT.left(90)
    rectT.forward(width*2)
    rectT.left(90)
    rectT.forward(height)
    rectT.hideturtle()
makeBoundary()




s.listen()
s.onkeypress(mouseUp, "Up")
s.onkeypress(mouseRight, "Right")
s.onkeypress(mouseLeft, "Left")
s.onkeypress(mouseDown, "Down")


while True:
    allowedForward = True
    # if (mouse.ycor() < height and
    #     mouse.ycor() > -height and
    #     mouse.xcor() < width and
    #     mouse.xcor() > -width):
    if mouse.ycor() >= height and mouse.heading() == 90:
        allowedForward = False
    elif mouse.ycor() <= -height and mouse.heading() == 270:
        allowedForward = False
    elif mouse.xcor() >= width and mouse.heading() == 0:
        allowedForward = False
    elif mouse.xcor() <= -width and mouse.heading() == 180:
        allowedForward = False    

    if allowedForward:
        mouse.forward(distance)

    s.update()

