'''
if __name__ == '__main__'
'''

'''
import module_two_61
# Python interpreter sets "special variables", one of which is __name__
# Python will assign the __name__ variable a value of '__main__' if its
# the initial module being run


# we can also check it
print(__name__)
# since this is the  initial module being run the output is __main__


print(module_two_61.__name__)
# so when we import a module, the __name__ variable will be assigned the
# name of the module in this case module_two_61
'''

''' comment out all of the text in the other module when running this one'''

#if __name__ == '__main__':
#    print("Running this module directly")
#else:
#    print("Running other module indirectly")

# ---------------------------------

def hello():
    print("Hello")

if __name__ == '__main__':
    hello()

# you can also use this:
def main():
    print("Hello")

if __name__ == '__main__':
    main()