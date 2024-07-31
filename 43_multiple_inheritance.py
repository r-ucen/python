class Prey:

    def flee(self):
        print("This animal is fleeing")



class Predator:

    def hunt(self):
        print("This animal is hunting")



class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()


rabbit.flee()
hawk.hunt()

# note that fish class inherits from both Predator and Prey classes
fish.hunt()
fish.flee()