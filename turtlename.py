
from turtle import *


color("pink", "pink")
pendown()
begin_fill()
end_fill()
color("orange", "yellow")
speed(10)


def L():
    penup()
    left(180)
    forward(500)

    begin_fill()
    pendown()
    pensize(5)
    right(90)
    forward(150)
    right(90)
    forward(30)
    right(90)
    forward(125)
    left(90)
    forward(75)
    right(90)
    forward(25)
    right(90)
    forward(105)
    end_fill()

L()


def e():
    right(180)
    penup()
    forward(225)
    left(90)
    forward(75)
    right(90)
    pendown()

    penup()
    right(90)
    forward(15)
    left(90)
    pendown()
    begin_fill()
    forward(100)
    left(90)
    circle(65, 315, None)
    left(90)
    forward(20)
    left(90)
    circle(-40, 135, None)
    end_fill()
    penup()
    color("orange", "white")
    begin_fill()
    forward(15)
    right(90)
    pendown()
    forward(75)
    left(90)
    circle(37.5, 180, None)
    end_fill()
    color("orange", "yellow")

e()


def o():
    penup()
    forward(15)
    left(90)
    forward(200)

    begin_fill()
    right(90)
    pendown()
    circle(65, None, None)
    end_fill()
    color("orange", "white")
    left(90)
    penup()
    forward(25)
    begin_fill()
    pendown()
    right(90)
    circle(40, None, None)
    end_fill()

o()


done()