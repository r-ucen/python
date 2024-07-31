import time

# from 1 to 10

for i in range(10):
    print(i + 1)

# from 50 to 100 but every 2nd

for i in range(50, 101, 2): # (start, stop, step) start includes the number, stop doesnt
    print(i)

# print each character of a string on a new line

for i in "Bro Code":
    print(i)

# countdown program
    
for seconds in range(10, 0, -1): # from 10 to 1 (cos 0 is not included) and it decreases by -1
    print(seconds)
    time.sleep(1) # suspends execution by 1 second
print("Happy New Year!!!!")
