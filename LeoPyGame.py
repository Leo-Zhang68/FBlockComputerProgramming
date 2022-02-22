
from random import randint
import re
from turtle import Turtle, setup

width, height = 500, 400
mouse = Turtle()
setup(1400, 1000)
s = mouse.getscreen()

speed = 1.1
cheeseDrawMan2 = Turtle()
cheeseDrawMan = Turtle()
rectT = Turtle()
mouse.penup()
mouse.speed(speed)
mouse.shapesize(10)
scoreMan = Turtle()
score = 0
scoreMan.pensize(3)

s.register_shape("Mouse.gif")
s.register_shape("MouseDown.gif")
s.register_shape("MouseLeft.gif")
s.register_shape("MouseRight.gif")

mouse.shape("Mouse.gif")



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
def drawCheese2():
    cheeseDrawMan2.pensize(3)
    cheeseDrawMan2.color("black", "#ffe817")
    cheeseDrawMan2.pendown()
    cheeseDrawMan2.seth(270)
    cheeseDrawMan2.fd(30)
    cheeseDrawMan2.right(135)
    cheeseDrawMan2.begin_fill()
    cheeseDrawMan2.fd(30)
    cheeseDrawMan2.bk(30)
    cheeseDrawMan2.right(45)
    cheeseDrawMan2.fd(30)
    cheeseDrawMan2.left(90)
    cheeseDrawMan2.circle(30, 45, None)
    cheeseDrawMan2.end_fill()
    cheeseDrawMan2.left(90)
    cheeseDrawMan2.forward(30)
    cheeseDrawMan2.shapesize(3)


def cheeseGenerationStart():
    global x, y, a, b
    x = randint(-width, width)
    y = randint(-height, height)
    a = randint(-width, width)
    b = randint(-height, height)
    cheeseDrawMan.hideturtle()
    cheeseDrawMan.speed(10000)
    cheeseDrawMan.penup()
    cheeseDrawMan.setpos(x, y)
    drawCheese()
    cheeseDrawMan2.hideturtle()
    cheeseDrawMan2.speed(10000)
    cheeseDrawMan2.penup()
    cheeseDrawMan2.setpos(a, b)
    drawCheese2()
cheeseGenerationStart()

def cheeseGenerationReset1():
    global x, y
    x = randint(-width, width)
    y = randint(-height, height)
    cheeseDrawMan.penup()
    cheeseDrawMan.setpos(x, y)
    drawCheese()
def cheeseGenerationReset2():
    global a, b
    a = randint(-width, width)
    b = randint(-height, height)
    cheeseDrawMan2.hideturtle()
    cheeseDrawMan2.speed(10000)
    cheeseDrawMan2.penup()
    cheeseDrawMan2.setpos(a, b)
    drawCheese2()






s.screensize(448, 252)
s.title("kitchen")

s.bgpic("floor.gif")
Upok = True
distance = 10

def mouseUp():
   
    mouse.shape("Mouse.gif")
    mouse.speed(1000)
    mouse.setheading(90)
    mouse.speed(1)
    
    

def mouseRight():

    mouse.shape("MouseRight.gif")
    mouse.speed(1000)  
    mouse.setheading(0)
    mouse.speed(1)
    

def mouseLeft():
    mouse.shape("MouseLeft.gif")
    mouse.speed(1000)
    mouse.setheading(180)
    mouse.speed(1)
   

def mouseDown():

    mouse.shape("MouseDown.gif")
    mouse.speed(1000)
    mouse.setheading(270)
    mouse.speed(1)
    

def makeBoundary():
    rectT.color("black")
    rectT.width(5)
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


    mouthX = mouse.xcor() - 0
    mouthY = mouse.ycor() + 0

    if abs(x-mouthX) < collisionDistance and abs(y-mouthY) < collisionDistance:
        score = score + 1
        print("your score is", score)
        resetScore = True
        cheeseDrawMan.clear()
        cheeseGenerationReset1()
    if abs(a-mouthX) < collisionDistance and abs(b-mouthY) < collisionDistance:
        score = score + 1
        print("your score is", score)
        resetScore = True
        cheeseDrawMan2.clear()
        cheeseGenerationReset2()
    if resetScore == True:
        scoreMan.clear()
        writeScore()


    s.update()

