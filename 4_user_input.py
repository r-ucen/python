name = input("What is your name?: ")

print(f"hello {name}")

# when we accept user input its always string

# so we do this if we want a number:
age = int(input("How old are you?: "))
print(f"the age variable is of type: {type(age)}")

height = float(input("How tall are you?: "))
print(f"the height variable is of type: {type(height)}")

