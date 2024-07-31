# method chaining = calling multiple methods sequentially
#                 = each call performs an action on the same object
#                    and returns self

# we need to put "return self" at the end of each method to use chaining


class Car:

    def turn_on(self):
        print("You started the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self
    
car = Car()

car.turn_on().drive()


# if you have a long chain, a more readable style of writing it would be like this:
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
