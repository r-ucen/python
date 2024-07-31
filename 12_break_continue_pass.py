# break =       used to terminate the loop entirely
# continue      skips to the next iteration of the loop
# pass =        does nothing, acts as a placeholder

# BREAK
# this will keep on looping until the user types in a name
while True:
    name = input("Enter your name: ")
    if name != "":
        break

# CONTINUE
# this will print the number without the dashes (it will skip them cos of the continue)
phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="") # end="" so that theres no new line character

# PASS
# this will print every number from 1 to 20 but not 13, it will skip it
for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)

