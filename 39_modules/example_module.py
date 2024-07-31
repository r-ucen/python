def hello():
    print("Hello from the module!")

# This block will only run if the module is run directly
if __name__ == "__main__":
    print("This code is executed when the module is run directly.")
    hello()  # call the hello function

'''
IF WE RUN THIS MODULE FILE DIRECTLY THE OUTPUT WILL BE:

This code is executed when the module is run directly.
Hello from the module!
'''