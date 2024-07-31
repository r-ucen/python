name = "bro Code"

# checks whether the character at index 0 is lower case, if yes, it capitalizes it
if (name[0].islower()):
    name = name.capitalize()
print(name)

# characters from index 0 to 3 and makes them uppercase
first_name = name[:3].upper() 
print(first_name)

last_name = name[-4:].lower()
print(last_name)

name = "bro Code!"

# prints the !
last_character = name[-1]
print(last_character)