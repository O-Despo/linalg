from importlib import import_module
import random
import numpy as np
import turtle

h = turtle.window_height()
w = turtle.window_width()

pos = (0,0)

turtle.tracer(False)
wn = turtle.Screen()

turtle.setworldcoordinates(0,0,w,h)
turt = turtle.Turtle()
turt.speed(0)
cpos  = [(0,0),(w/2,h),(w,0)]
turt.pd()
for pos in cpos:
    turt.goto(pos)
    
turt.goto((0,0))
turt.pu()

turt.goto(w/2, h/2)

wp = random.randint(0, w)
hp = random.randint(0,int(wp/2))
point = (wp,hp)
turt.goto(point)

for i in range(0,10000):
    corner = random.choice(cpos)
    turt.seth(turt.towards(corner))
    turt.fd(turt.distance(corner)/2)
    turt.dot(3)

    if i%5 == 0: turtle.update()

turtle.done()
turtle