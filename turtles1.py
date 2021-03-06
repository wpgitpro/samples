#***********************************
# Program: turtles1.py
# Author:  Mark Rogers
#
# Usage:   For the fun of it
#***********************************

import turtle, math, json

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y


class ComplexNumber: 
    """ 
    This is a class for mathematical operations on complex numbers. 
      
    Attributes: 
        real (int): The real part of complex number. 
        imag (int): The imaginary part of complex number. 
    """
  
    def __init__(self, real, imag): 
        """ 
        The constructor for ComplexNumber class. 
  
        Parameters: 
           real (int): The real part of complex number. 
           imag (int): The imaginary part of complex number.    
        """
  
    def add(self, num): 
        """ 
        The function to add two Complex Numbers. 
  
        Parameters: 
            num (ComplexNumber): The complex number to be added. 
          
        Returns: 
            ComplexNumber: A complex number which contains the sum. 
        """
  
        re = self.real + num.real 
        im = self.imag + num.imag 
  
        return ComplexNumber(re, im)


class Dog:
    """ Dog class """
    
    #class attribute
    species = 'mammal'
    
    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Greyhound(Dog):
    pass


class Shark:
    """ all about Sharks """
    
    def __init__(self, name):
        self.name = name

    def swim(self):
        print(self.name + " is swimming.")

    def be_awesome(self):
        print(self.name + " is being awesome.")


class Link:
    pass


def area(radius):
    """ area function """
    
    b = math.pi * radius**2
    return b


def main():
    """ Main program for my sample python program """
    
    window = turtle.Screen()
    window.bgcolor('green')
    print(window.screensize())
    # window.screensize(canvwidth=2000, canvheight=1600, bg='yellow')
    
    alex = turtle.Turtle()
    # alex.shape('square')
    alex.penup()

    testarea = area(3)
    p = Point(1,1)
    # print(p.__doc__, main.__doc__, alex.__doc__)
    
    print(json.dumps({"name":"John", "age":30}))
    
    my_dictionary = {"one":1, "two":2, "three":3}
       
    my_tuple = ("one", "two", "three")
    
    my_list = ["Robbo","Steve","John","Gary"]
    my_list.append("Dave")
    my_list.pop()
    del my_list[0]
    
    current_angle = 0
    current_length = 200
    print(alex.pos())

    while True:

        # current_rads = math.radians(current_angle)
        # print(current_rads)
        
        alex.forward(current_length)
        # print(alex.pos()[0])
        alex.stamp()
        # alex.left(-current_angle)
        alex.goto(0,0)
        # alex.left(current_angle + 30)
        alex.left(30)
        
        # print(alex.heading())
        
        current_angle += 30
        if current_angle >= 360:
            break

    for n in my_tuple:
        if n.startswith("t"):
            print(n)
    
    my_list = ["test", "members"]
    n = my_list.pop()
    if not my_list:
        print('List is empty!')
    else:
        print(n)

    with open('../../Downloads/data.txt') as f:
        for line in f:
            print(line)

        
    window.exitonclick()


if __name__ == "__main__":
    main()