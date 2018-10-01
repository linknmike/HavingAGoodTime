import turtle
import random

window = turtle.Screen()
window.bgcolor("lightblue")
fool = turtle.Turtle()
fool.speed(0)
fool.up()
fool.goto(200, 200)
fool.down()

for i in range(4):
    fool.right(90)
    fool.fd(50)

hp = turtle.Turtle()
hp.shape("turtle")
hp.circle(25)
hp.color("white")

def handler(x, y):
    if (150<x) & (x<200) & (150<y) & (y<200):
        hp.circle(50)
        hp.fillcolor(random.random(), random.random(), random.random())
    print(x, y)


window.onclick(handler)
