from turtle import *
color("red", "orange")
begin_fill()

for banana in range(4):

    for monkey in range(5):
        forward(100)
        right(144)

    right(90)
    penup()
    forward(100)
    pendown()
    end_fill()
    begin_fill()

left(45)
penup()
forward(150)
pensize(5)
pendown()
color("black", "white")
circle(50, None, None)
end_fill()

begin_fill()
penup()
left(45)
forward(20)
pendown()
circle(15, None, None)

penup()
left(75)
forward(60)
pendown()
circle(8, None, None)


done()

