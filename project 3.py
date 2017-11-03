import turtle
from myShape import *
from random import randint
turtle.bgcolor("black")
turtle.colormode(255)

bob=turtle.Turtle()
bob.speed(0)
turtle.tracer(0)

for times in range(2000):
    x = randint( -800, 900)
    y = randint(-800, 900)
    bob.color(255,255,255)
    move(bob,x,y)
    bob.begin_fill()
    bob.circle(1)
    bob.end_fill()

move(bob,0,0)
for times in range(200):
    bob.color(255-times,0,55+times)
    bob.circle(100)
    bob.left(5)
    
for times in range(500):
    bob.width(5)
    bob.circle(3000000)
    bob.left(10)

for times in range(500):
    bob.color(148,0,211)
    bob.width(3)
    bob.circle(3000000)
    bob.left(8)

for times in range(500):
    bob.width(1)
    bob.color(255,255,255)
    petal(bob,100)
    bob.left(5)

bob.color(0,0,0)
move(bob,-178,30)
bob.begin_fill()
bob.circle(180)
bob.end_fill()
