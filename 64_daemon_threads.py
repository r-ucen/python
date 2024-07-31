'''
daemon thread = a thread that runs in the background, 
                not important for program to run

                your program will NOT wait for daemon thread
                to complete before exiting

                non_daemon threads cannot normally be killed,
                stay alive until a task is complete

                example:
                background tasks, garbage collection, waiting for input, long running process
'''

import threading
import time

def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print(f"Logged in for: {count} seconds")

x = threading.Thread(target=timer, daemon=True)
x.start()

# x.setDaemon(True) # if your thread is currently running you cannot change it tho
print(x.daemon) # find out whether a thread is daemon


answer  = input("Do you wish to exit?")