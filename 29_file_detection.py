import os

path = "C:\\Users\\rucen\\Documents\\code_subjects\\Python_tut\\assets\\29_file_detection.txt"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("THAT LOCATION DOES NOT EXIST")