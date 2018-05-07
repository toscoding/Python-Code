import turtle
import random
import cmath
c = 0  # total dans le cercle
r = 52
pim = cmath.pi
p = 0

turtle.pu()
turtle.home()
turtle.color("black")
turtle.setheading(90)
turtle.fd(58)
turtle.right(90)
turtle.pd()
total = 0  # total
turtle.speed(10)


def cercle():
    global r
    m = turtle.ycor()
    for x in range(180):
        turtle.forward(4)
        turtle.right(1)
    j = turtle.ycor()
    r = (m - j) / 2
    turtle.ycor()
    for x in range(180):
        turtle.forward(4)
        turtle.right(1)


def sq():
    global r
    turtle.forward(r)
    turtle.right(90)
    for x in range(3):
        turtle.forward(r * 2)
        turtle.right(90)
    turtle.forward(r)


cercle()
sq()
while (p != pim):
    total = total + 1
    turtle.pu()
    x = random.randrange(-r, r)

    y = random.randrange(-r, r)
    turtle.setx(x)
    turtle.sety(y)
    d = ((y * y) + (x * x))
    if ((r * r) >= d):
        turtle.color("green")
        c = c + 1
    else:
        turtle.color("blue")
    co = total - c
    p = (4 * (c / total))
    print(p)
    turtle.dot()
