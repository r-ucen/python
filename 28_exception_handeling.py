# exception = event during execution that interrupts the flow of a program

# for example if we wanted to divide by 0

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))

    result = numerator / denominator
except ValueError as e: # first we catch specific exceptions
    print(e) # we can also display the error
    print("Enter only numbers pls")
except ZeroDivisionError as e:
    print(e)
    print("You cannot divide by zero! lol")
except Exception as e:
    print(e)
    print("something went wrong")
else:
    print(result) # if no exceptions occur
finally: # whether or not we cause an exception we will always execute the block of code which it in the finally part
    print("This will always execute")