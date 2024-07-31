name = ""
print(len(name)) # we can see that the length of the name is 0 so the while loop starts

while (len(name) == 0):
    name = input("Enter your name:") # then it assigns the user input to the name variable and if the condition of the loop becomes False (meaning the name variable is not empty anymore), it exits the loop 

print(f"hello {name}")