# USING INDEXING
# [start:stop:step]

# the starting index includes the character and the stopping doesnt

name = "Bro Code"

print(name[0:3])
# is the same as:
print(name[:3])

print(name[4:8])
# same as:
print(name[4:])

print(name[0:8:2]) # every second character is displayed
# same as:
print(name[::2])

print(name[::-1]) # reverse a string

#USING slice()
# (start, stop, step)

website = "http://google.com"

slice = slice(7, -4) # so this will start from the 6th character and then it will leave every character until it steps upon the -4th character (last character has index -1, etc.) so this is universal website slicer (assuming the website address starts with http and ends with .com)

print(website[slice])