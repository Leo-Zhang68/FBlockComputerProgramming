from turtle import Turtle


monkey = Turtle()
frog = Turtle()
monkey.pencolor("yellow")
frog.pencolor("yellow")
monkey.shape("turtle")
frog.shape("turtle")


s = monkey.getscreen()



for turtle in [monkey, frog]:
    turtle.left(45)
    turtle.pensize(10)
    turtle.penup()
    turtle.forward(200)
    turtle.right(180)
    turtle.pendown()


def mcdonaldsFryBecauseBananaIsHard():
    monkey.left(45)
    monkey.circle(-375, 90, None)
    frog.right(90)
    frog.forward(75)
    frog.left(135)
    frog.circle(-375, 90, None)

    frog.left(135)
    frog.forward(75)
    frog.back(75)
    frog.left(90)
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

for bodacious in [monkey, frog]:

    bodacious.penup()
    bodacious.goto(0,400)



s.mainloop()

