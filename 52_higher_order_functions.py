'''
Higher order function = a function that either:
                        1. accepts a function as an argument
                            or
                        2. returns a function
                        (In Python, functions are also treated as objects)
'''
# 1.
'''
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(function):
    text = function("Hello")
    print(text)

hello(loud)

# so were calling the hello function, the argument is loud, 
# loud("Hello") -> this will return all uppercase and we are 
# assigning it to the text variable which we are printing

# we can do the same with the quiet function
hello(quiet)
'''
# 2.

# dividend  divisor  quotient
#   10    /   2    =    5

def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2) 
print(divide(10))

'''
WHATS HAPPENING HERE
divide = divisor(2) --> x will be 2 
were skipping the inner function bcs it hasnt been called yet:
def dividend(y):
        return y / x
were returning dividend and assigning it to the divide variable 
and we can call the variable because it has the memory address of 
the function
and in this line print(divide(10))
we are calling the inner function dividend and passing 10 as y

'''