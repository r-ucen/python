'''
thread = a flow of execution. Like a separate order of instructions.
                However each thread takes a turn running to achieve concurrency
                GIL = (global interpreter lock)
                allows only one thread to hold control of the Python interpreter at any one time

                
cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
            it is better to use multiprocessing for tasks that are cpu bound

io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
           its better to use multithreading for such a tasks
'''

import threading
import time

print(threading.active_count()) # get active cound of threads running in our program

print(threading.enumerate()) # list of threads that are running

'''
an example of multithreading is when you have a quiz game and you're waiting for 
the user to type in their answer and you have a countdown timer that tells the user how 
many seconds they have to answer the question

so one thread would be in charge of the countdown 
timer and another thread would be in charge
of waiting for the user to answer
'''

# ok now lets create something
''' lets say we're late for school or work and we have 3 tasks to do in the morning before we can leave '''

def eat_breakfast():
    time.sleep(3)
    print("You finish eating")

def drink_coffee():
    time.sleep(4)
    print("You drank coffee")

def study():
    time.sleep(5)
    print("You finish studying")

# ok so lets run these 3 tasks on our main thread
#eat_breakfast()
#drink_coffee()
#study()
# ok so we did these tasks sequentially, we waited for the previous task to be completed before starting another task
# but irl we would be drinking coffee while eating and we would also be studying while eating and drinking the coffee
# and thats the same concept like multithreading

# so we can create 3 threads each doing it's task

def eat_breakfast():
    time.sleep(3)
    print("You finish eating")

def drink_coffee():
    time.sleep(4)
    print("You drank coffee")

def study():
    time.sleep(5)
    print("You finish studying")



x = threading.Thread(target=eat_breakfast) # (if you have arguments of the function which you are targetting you pass them in in a tuple (args = (x, y, z)))
x.start() # init the thread

y = threading.Thread(target=drink_coffee) 
y.start()

z = threading.Thread(target=study) 
z.start()

x.join()
y.join()
z.join()
# now the main thread has to wait for these threads to synchronize (finish), and only then it can print the other stuff
# so now we only have one thread bcs the other ones joined the main one

print(threading.active_count())
print(threading.enumerate())

# so this time it took significantly shorter period of time 
# to be exact  about 5 seconds bcs the study function takes 5 seconds

print(time.perf_counter()) # how long it took the main thread to complete it's tasks



