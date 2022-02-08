from turtle import Turtle

mouse = Turtle()
mouse.penup()
mouse.speed(1)
mouse.shapesize(5)

s = mouse.getscreen()

s.bgcolor("brown")


def mouseUp():
        
    mouse.speed(1000)
    mouse.setheading(90)
    mouse.speed(1)
    mouse.forward(1000)

def mouseRight():

    mouse.speed(1000)
    mouse.setheading(0)
    mouse.speed(1)
    mouse.forward(1000)

def mouseLeft():

    mouse.speed(1000)
    mouse.setheading(180)
    mouse.speed(1)
    mouse.forward(1000)

def mouseDown():

    mouse.speed(1000)
    mouse.setheading(270)
    mouse.speed(1)
    mouse.forward(1000)

s.listen()
s.onkeypress(mouseUp, "Up")
s.onkeypress(mouseRight, "Right")
s.onkeypress(mouseLeft, "Left")
s.onkeypress(mouseDown, "Down")


s.mainloop()

