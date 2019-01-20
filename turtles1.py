import turtle, math

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

def area(radius):
    b = math.pi * radius**2
    return b

def main():
    window = turtle.Screen()
    alex = turtle.Turtle()

    testarea = area(3)

    while True:
        alex.forward(200)
        alex.left(170)
        if abs(alex.pos()) < 1:
            break

    window.exitonclick()


if __name__ == "__main__":
    main()