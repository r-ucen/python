'''
multiprocessing = running tasks in parallel on different cpu cores,
                  bypass GIL used for threading

                  multiprocessing = better for cpu bound tasks (heavy cpu usage)
                  multithreading = better for io bound tasks (waiting around)
'''

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    
    a = Process(target=counter, args=(1000,)) # in the args we have to add , to differenciate it from an expression
    b = Process(target=counter, args=(1000,))
    c = Process(target=counter, args=(1000,))
    d = Process(target=counter, args=(1000,))
    
    a.start()
    b.start()
    c.start()
    d.start()

    a.join() # the main mrocess will wait for the a process to finish before continuing
    b.join()
    c.join()
    d.join()

    print(f"finished in {time.perf_counter()} seconds")

if __name__ == '__main__':
    main()