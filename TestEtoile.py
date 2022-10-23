from turtle import *
from random import randint


def etoile(x=0.0, y=0.0, rotation=0, longueur=100, nombrebranche=5):
    setpos(x, y)
    pendown()
    color('red', 'black')
    angle = 2 * 360 / nombrebranche
    begin_fill()
    left(rotation)
    for i in range(0, 5):
        forward(longueur)
        left(angle)
    end_fill()
    penup()


penup()
for i in range(0, 3):
    x=randint(-100,100)
    y=randint(-200,200)
    angle=randint(0,360)
    etoile(x, y, angle)
done()
