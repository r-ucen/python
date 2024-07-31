# **kvargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments

# we will create a function that will accept a varying amount of arguments

# just like with *args you dont need the word kwargs, it can be any word, just make sure that there are the **
def hello(**kwargs):
    #print(f"Hello {kwargs['first']} {kwargs['last']}")
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello(title = "Mr.", first = "Bro", middle = "Dude", last = "Code")

