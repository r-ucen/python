'''
lambda function = function written in 1 line using lambda keyword
                  accepts any number of arguments, but only has one expression.
                  
                  (thisnk of it as a shortcut)
                  (useful if needed for a shorter period of time, throw-away)

lambda parameters:expression
'''


''' normal function '''
def double(x):
    return x * 2

print(double(5))

# now lets write the same thing using lambda function
''' lambda function'''
double  = lambda x: x * 2

print(double(5))

# OK ANOTHER EXAMPLE
multiply = lambda x, y: x * y
print(multiply(2, 3))

# AND ANOTHER EXAMPLE
add = lambda a, b, c: a + b +c
print(add(1, 2, 3))

# ANOTHER EXAMPLE
full_name = lambda first_name, last_name: first_name + " " + last_name
print(full_name("Bro", "Code"))

# ANOTHER EXAPLE
age_check = lambda age: True if age >= 18 else False
print(age_check(18))