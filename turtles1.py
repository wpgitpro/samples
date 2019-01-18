import turtle

window = turtle.Screen()
alex = turtle.Turtle()

while True:
    alex.forward(200)
    alex.left(170)
    if abs(alex.pos()) < 1:
        break

window.exitonclick()