import shutil

# copyfile() = copies contents of a file
# copy()     = copyfile() + permission mode + destination can be a directory
# copy2()    = copy() + copies metadata (files's creation and modification times and other data)

# (source, destination)
shutil.copyfile('assets\\31_writing_into_a_file.txt', 'assets\\31_copy.txt')

# the arguments for copy() or copy2() are the same


