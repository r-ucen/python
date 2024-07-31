# Prevents user from creating an object of that class
# think of it like an idea of a class or a template or a ghost class

# plus it compels (donutí) a user to override abstract methods in a child class

# abstract class = a class that contains one or more abstract methods
# abstract method = a method that has a declaration but does not have an implementation

# the abstract Vehicle class is saying: if youre gonna inherit from me then you need to overwrite the absctract method and provide its own implementation

from abc import ABC, abstractmethod

class Vehicle(ABC): # we inherit from the ABC imported class

    @abstractmethod
    def go(self): # the abstract go method is important here, without it the user could create an instance of this class
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")

vehicle = Vehicle() # TypeError: Can't instantiate abstract class Vehicle with abstract method go
car = Car()
motorcycle = Motorcycle()

vehicle.go()
car.go()
motorcycle.go()



