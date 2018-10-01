import turtle
import random

line = turtle.Turtle()
window = turtle.Screen()
window.screensize(100, 100)

line.up()
line.goto(-50, 50)
line.down()
line.speed(0)
line.shape()

def where(x, y):
    print(x, y)
window.onclick(where)

i = 0

while (i < 1):
    line.fd(200)
    line.right(90)
    line.fd(1)
    line.right(90)
    line.fd(200)
    line.left(90)
    line.fd(1)
    line.left(90)
    i = i + 0.01
    line.color(0, i, 0)

line.up()
line.goto(-25, 25)
line.color(1, 1, 1)
line.write("CLOSE TO THE EDGE")
