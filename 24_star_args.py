# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments


# *args (only the * is important, the word args can be replaced with any word)
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
    
print(add(1, 1, 1, 1, 1, 1, 1))