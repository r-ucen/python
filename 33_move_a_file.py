import os

source = "assets\\31_copy.txt"
destination = "assets\\for_moving_files\\31_copy_moved.txt"

try:
    if os.path.exists(destination):
        print("There is already a file named like this")
    else:
        os.replace(source, destination)
        print(f"The {source} has been successfully moved")
except FileNotFoundError:
    print(f"{source} was not found")

# you can also move a directory with the same process

# you can also use the shutil library
import shutil
shutil.move() # (source, destination)