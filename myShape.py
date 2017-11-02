def square( t, distance ):
    for times in range(4):
        t.forward(distance)
        t.left(90)

def triangle( t, distance ):
    for times in range(3):
        t.forward(distance)
        t.left(120)

def pentagon ( t, distance):
    angle=360/5
    for times in range(5):
        t.forward(distance)
        t.left(angle)

def polygon ( t, distance, side):
    angle=360/side
    t.begin_fill()
    for times in range(side):
        t.forward(distance)
        t.left(angle)
    t.end_fill()

def move ( t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def petal (t,distance):
    t.begin_fill()
    for times in range(4):
        t.forward(distance)
        t.left(40)
        t.forward(distance)
        t.left(140)
    t.end_fill()
    



        
