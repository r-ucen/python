'''
def hello():
    print("Hello")

print(hello) # this prints the address of the function (where its located in memory)

hi = hello
print(hi) # this will print the same address
# so lets assign the function name to a variable hi
hi = hello
# and lets call hi()
hi()
# so this will result in the same output as
hello()
'''

say = print

# so now we can use either print() or say() to display something on the console

say("hey there!")
print("yooo")
