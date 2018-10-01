import turtle


    
def screenAndTurtleSetup(screen, turtle):
    screen.bgcolor("lightblue")
    turtle.shape("turtle")
    turtle.penup()
    turtle.speed(0)
    turtle.goto(50, 50)
    turtle.pendown()

def main():
    turtle.setup(500, 500)
    fool = turtle.Turtle()
    screen = turtle.Screen()
    screenAndTurtleSetup(screen, fool)

main()
