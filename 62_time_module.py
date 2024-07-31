import time

print(time.ctime(0)) # this will convert a time expressed in seconds since epoch and convert it to a readable string
# the output is Thu Jan  1 01:00:00 1970 for me (it can be different for someone else)
# this is called the epoch, basically a starting point lets say

print(time.ctime(100000)) # so this will return a time 100000 seconds after the epoch

print(time.time()) # return current seconds since epoch

# get current time
print(time.ctime(time.time())) # the inner returns number of seconds since epoch and the outer will convert it to a readable format

# another way to get the current time (creates a time object)
time_object = time.localtime()
time_object_UTC = time.gmtime() # for UTC time (it aint adjusted for daylight saving)
print(time_object)
# time.struct_time(tm_year=2024, tm_mon=3, tm_mday=29, tm_hour=22, tm_min=36, tm_sec=37, tm_wday=4, tm_yday=89, tm_isdst=0)
# we can format this mess
''' time.strftime(format, time_object) '''
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)

''' https://docs.python.org/3/library/time.html '''

time_string = "20 April, 2024"
time_object = time.strptime(time_string, "%d %B, %Y") # it takes a string and parses it to a time object
print(time_object)


time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple) # takes a tuple representation of time and converts to string
print(time_string) # Mon Apr 20 04:20:00 2020

time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple) # takes a tuple representation, converts to seconds since epoch
print(time_string)

