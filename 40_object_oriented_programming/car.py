class Car:

    wheels = 4 # class variable (it is a default value for every instance of this object)

    def __init__(self, make, model, year, color):
        self.make = make    # instance variable
        self.model = model  # instance variable
        self.year = year    # instance variable
        self.color = color  # instance variable

    def drive(self):
        print(f"This {self.model} is driving")

    def stop(self):
        print(f"This {self.model} is stopped")