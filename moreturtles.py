from calendar import c
from turtle import Turtle


monkey = Turtle()
frog = Turtle()



s = monkey.getscreen()
monkey.color("#ffe600", "orange")
frog.color("#ffe600", "green")
s.bgcolor("#f27cdb")



for turtle in [monkey, frog]:
    turtle.shape("turtle")
    turtle.left(45)
    turtle.pensize(10)
    turtle.penup()
    turtle.forward(200)
    turtle.right(180)
    turtle.pendown()

def mcdonaldsM():
    for chunkymonky in [monkey, frog]:
        chunkymonky.penup()
        chunkymonky.goto(-300,200)
        chunkymonky.right(40)
        chunkymonky.forward(100)
        chunkymonky.pendown()
    monkey.right(90)
    frog.left(90)
    frog.forward(50)
    monkey.forward(50)
    monkey.circle(-50, 180, None)
    frog.circle(50, 180, None)
    frog.forward(50)
    frog.hideturtle()
    monkey.hideturtle()


def mcdonaldsFryBecauseBananaIsHard():
    monkey.left(45)
    monkey.circle(-375, 90, None)
    frog.right(90)
    frog.forward(75)
    frog.left(135)
    frog.circle(-375, 90, None)

    frog.right(135)
    monkey.right(45)
    monkey.forward(75)
    monkey.left(45)
    frog.forward(50)
    frog.right(45)
    frog.circle(375, 40, None)
    

    monkey.penup()
    monkey.goto(90, 200)
    monkey.right(135)
    monkey.pendown()
    
    
    monkey.forward(50)
    monkey.right(90)
    monkey.forward(80)
    monkey.right(90)
    monkey.forward(50)
    monkey.back(50)
    monkey.left(45)

    monkey.circle(-375, 50, None)


    


mcdonaldsFryBecauseBananaIsHard()
mcdonaldsM()



    



s.mainloop()

