import turtle
import random

window = turtle.Screen()

square = turtle.Turtle()
square.speed(0)
square.hideturtle()

square.up()
square.goto(-200, 200)
square.down()

for i in range(4):
    square.forward(50)
    square.right(90)

square.up()
square.goto(-205, 205)
square.write("Change Color")

square.up()
square.goto(-100, 200)
square.down()

for i in range(4):
    square.forward(50)
    square.right(90)

square.up()
square.goto(-105, 205)
square.write("Stop being where I am")

pencil = turtle.Turtle()
pencil.shape("circle")
pencil.speed(0)

def drawing_controls(x, y):
    print(x, y)
    if (-200 <= x <= -150) and (150 <= y <= 200):
        red = random.random()
        green = random.random()
        blue = random.random()
        pencil.color(red, green, blue)
    if (-100 <= x <= -50) and (150 <= y <= 200):
        pencil.goto(random.randint(-475, 475), random.randint(-400, 400))        

window.onclick(drawing_controls)

pencil.onrelease(pencil.goto)
