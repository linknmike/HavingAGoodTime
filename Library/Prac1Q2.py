import turtle

def imprint(turt, x, y, color):
    turt.up()
    turt.goto(x, y)
    turt.color(color)
    turt.stamp()
fool = turtle.Turtle()
fool.shape("turtle")
fool.hideturtle()
imprint(fool, 0, 0, "red")
imprint(fool, 100, -50, "blue")
imprint(fool, -75, -25, "purple")
