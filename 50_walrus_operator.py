# walrus operator :=

# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

'''
happy = True
print(happy)
'''
# we can write the same thing using the walrus operator
print(happy := True)


# OK SO HERE IS A MORE PRACTICAL USE OF THE WALRUS OPERATOR
'''
foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)
'''
# lets write the same thing using the walrus operator
foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)
