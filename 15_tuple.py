# tuple = collection which is ordered just like list 
#         but its unchangeable (immutable) - neměnitelý

student = ("Bro", 21, "male")

print(student.count("Bro")) # how many times a value appears in the tuple
print(student.index("Bro")) # find the index of a value

# display all values within the tuple
for item in student:
    print(item)

# ------------------------------
if "Bro" in student:
    print("Bro is in the tuple")

# we can use len(), sum(), min() and max() as well