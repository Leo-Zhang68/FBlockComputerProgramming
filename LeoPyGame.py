
from random import randint
from turtle import Turtle, setup

width, height = 500, 400
mouse = Turtle()
setup(1400, 1000)
s = mouse.getscreen()


cheeseDrawMan = Turtle()
rectT = Turtle()
mouse.penup()
mouse.speed(1)
mouse.shapesize(10)
scoreMan = Turtle()
score = 0
scoreMan.pensize(3)

s.register_shape("mouseUp.gif")
s.register_shape("mouseDown.gif")
s.register_shape("mouseLeft.gif")
s.register_shape("mouseRight.gif")

mouse.shape("mouseUp.gif")



def writeScore():
    scoreMan.hideturtle()
    scoreMan.penup()
    scoreMan.setposition(0, height-100)
    scoreMan.write(score, False, "center", ("Arial", 50, "bold"))
writeScore()


def drawCheese():
    cheeseDrawMan.pensize(3)
    cheeseDrawMan.color("black", "#ffe817")
    cheeseDrawMan.pendown()
    cheeseDrawMan.seth(270)
    cheeseDrawMan.fd(30)
    cheeseDrawMan.right(135)
    cheeseDrawMan.begin_fill()
    cheeseDrawMan.fd(30)
    cheeseDrawMan.bk(30)
    cheeseDrawMan.right(45)
    cheeseDrawMan.fd(30)
    cheeseDrawMan.left(90)
    cheeseDrawMan.circle(30, 45, None)
    cheeseDrawMan.end_fill()
    cheeseDrawMan.left(90)
    cheeseDrawMan.forward(30)
    cheeseDrawMan.shapesize(3)


def cheeseGeneration():
    global x, y
    x = randint(-width, width)
    y = randint(-height, height)
    cheeseDrawMan.hideturtle()
    cheeseDrawMan.speed(10000)
    cheeseDrawMan.penup()
    cheeseDrawMan.setpos(x, y)
    drawCheese()
cheeseGeneration()





s.screensize(448, 252)
s.title("kitchen")

s.bgcolor("#a65837")
Upok = True
distance = 10

def mouseUp():
   
    mouse.speed(1000)
    mouse.setheading(90)
    mouse.speed(1)
    
    

def mouseRight():

    mouse.speed(1000)  
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

collisionDistance = 40

while True:

   
    resetScore = False
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


    mouthX = mouse.xcor() - 25
    mouthY = mouse.ycor() + 50

    if abs(x-mouthX) < collisionDistance and abs(y-mouthY) < collisionDistance:
        score = score + 1
        print("your score is", score)
        resetScore = True
        cheeseDrawMan.clear()
        cheeseGeneration()
    if resetScore == True:
        scoreMan.clear()
        writeScore()


    s.update()

