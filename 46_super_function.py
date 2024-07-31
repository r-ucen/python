# super() = function used to give access to the methods of a parents class.
#           Returns a temporary object of a parent class when used


# this is kinda repetitive bro, lets use the super() instead
'''
class Rectangle:
    pass

class Square(Rectangle):

    def __init__(self, length, width):
        self.length = length
        self.width = width

class Cube(Rectangle):

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.heigth = height

square = Square(3, 3)
cube = Cube(3, 3, 3)

'''

# using super():

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width

class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.heigth = height

    def volume(self):
        return self.length * self.width * self.heigth

square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())