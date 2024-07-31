import os
import shutil

path = 'assets\\for_moving_files\\31_copy_moved.txt'

try:
    os.remove(path)
    print(f"The file {path} has been removed")

    # to delete ONLY EMPTY directory we use:
    # os.rmdir(path)

    # to delete a directory that contains stuff we use the shutil module
    # shutil.rmtree(path) # careful with this one tho
except FileNotFoundError:
    print(f"The file {path} was not found")
except PermissionError: # os.remove cannot remove an empty directory
    print("You do not have a permission to delete this")
except OSError:
    print("You cannot delete that using that function")
