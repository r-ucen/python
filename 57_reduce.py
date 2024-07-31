# reduce() = apply a function to an iterable and reduce it to a single 
# cumulative value.
# performs function on first two elements and repeats
# this process until 1 value remains

# reduce(function, iterable)

import functools
'''
# lets say were playing a game named scrabble

# here we have all the letters we need to spell the word "hello"
letters = ["H", "E", "L", "L", "O"]

word = functools.reduce(lambda x, y: x + y, letters)
# our reduce function applies the lambda function to the first 2 elements of 
# the list, it performs the x + y expression
# so this first step will result in this: letters = ["HE", "L", "L", "O"]
# and then we do it again and after this second step the result will look
# like this: letters = ["HEL", "L", "O"]
# and we continue doing this until theres only one element in the list
# and that is letters = ["HELLO"]

print(word)
'''

# ok another example

factorial = [5, 4, 3, 2, 1]
print(functools.reduce(lambda x, y: x * y, factorial))

# on so in conclusion:
# the reduce() function applies a function of out choosing to the first 2 elements 
# of an iterable and repeats this process until only one element remains
