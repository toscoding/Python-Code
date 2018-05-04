from vpython import *
#import turtle

import time
#turtle.fillcolor("black")
#turtle.speed(10)
#turtle.ht()

h=95
u=0
g=100
m=0
width=20
s=1/500000000
x = 0
y = 0
z = 0
ma= atan(1/sqrt(2))
lenght=30
o=scene.camera.pos
print (o)

def stick() :
    global h
    turtle.color("red", "red")
    turtle.begin_fill()
    turtle.fd(h)
    turtle.left(90)
    turtle.fd(15)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    turtle.end_fill()
    turtle.home()
    turtle.left(90)
    turtle.clear()
def d() :
    global h, y,z, width, lenght

    y=-5
    z=0
    m=0
    po = vector(0, -5, 0)
    b = box(pos=po, length=lenght, height=h, width=width, color=color.blue)
    b.visible = True
    time.sleep(s)
    b.visible = False
    for ma in range (5) :
        z=z+lenght + 2
        y=-5
        for m in range (10) :
            po = vector(z, -5, y)
            bm = b.clone(pos=po)
            bm.visible = True
            time.sleep(s)
            bm.visible = False
            del bm

            y = y + width + 2

    del b

while True :

    while (h != g) :
        h=h+5

        #box(pos=po, length=40, height=h, width=30, color=color.blue)
        #stick()
        d()
        print (h)
        if (h > (g+2)) :
            h=19

    while (h != 5) :
        #scene.delete()
        #scene = canvas(width=500, height=500)
        u=u+1
        h=h-5
        #box(pos=po, length=40, height=h, width=30, color=color.blue)
        #stick()
        d()
        print (h)
        if (h < 5):
            h=5

