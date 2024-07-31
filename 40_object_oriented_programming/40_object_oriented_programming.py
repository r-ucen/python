from car import Car

car_1 = Car("Chevrollet", "Corvette", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2022, "red")

print(f"car_1: the make is {car_1.make}, model is {car_1.model}, year is {car_1.year} and color is {car_1.color}")
car_1.drive()
car_1.stop()

print(f"car_2: the make is {car_2.make}, model is {car_2.model}, year is {car_2.year} and color is {car_2.color}")
car_2.drive()
car_2.stop()

# **********************************************************
# CLASS VARIABLE

# you can change the class variable
car_1.wheels = 2
print(car_1.wheels)

# or you can change it without creating an instance 
# we can change the class variable like this:
Car.wheels = 2
# it will change the variable for every instance of the class

