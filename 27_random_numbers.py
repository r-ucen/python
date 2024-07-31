import random

# creating pseudo-random numbers

x = random.randint(1, 6) # random integer from 1 to 6
y = random.random()

print(x)
print(y)

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList) # will choose random item from the list

print(z)

cards = [1, 2, 3, 4, 5, 6, 7, 8 ,9, "J", "Q", "K", "A"]
random.shuffle(cards) # it shuffles the list
print(cards)