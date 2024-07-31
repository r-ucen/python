# Car object
class Car:
    color = None

# Motorcycle object
class Motorcycle:
    color = None

# function that accepts object and its color as arguments
def change_color(vehicle, color):
    
    vehicle.color = color

# we crate instances of the Car object
car_1 = Car()
car_2 = Car()
car_3 = Car()

change_color(car_1, "red")
change_color(car_2, "white")
change_color(car_3, "blue")

print(car_1.color)
print(car_2.color)
print(car_3.color)

# doing the same for another object
bike_1 = Motorcycle()
change_color(bike_1, "black")
print(bike_1.color)