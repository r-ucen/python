'''
num = input(("Enter a whole positive number: "))
mun = float(num)
num = abs(mun)
num = round(num)
print(num)

'''

# we can write this using nested function calls:

# we start with the most inner function, it continues with the second most inner function etc.

print(round(abs(float(input(("Enter a whole positive number: "))))))

