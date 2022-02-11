from turtle import Turtle, onkeypress
from xmlrpc.client import boolean

mouse = Turtle()
rectT = Turtle()
mouse.penup()
mouse.speed(1)
mouse.shapesize(5)


width, height = 250, 250

s = mouse.getscreen()

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


s.listen()
s.onkeypress(mouseUp, "Up")
s.onkeypress(mouseRight, "Right")
s.onkeypress(mouseLeft, "Left")
s.onkeypress(mouseDown, "Down")


while True:
    
    if (mouse.ycor() < height and
        mouse.ycor() > -height and
        mouse.xcor() < width and
        mouse.xcor() > -width):
        mouse.forward(distance)

    s.update()

