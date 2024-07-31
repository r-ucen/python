
'''
# this will open the file, read it and automatically close it
with open('assets\\30_reading_a_file.txt') as file:
    print(file.read())

# we can find out whether a file is closed or not
print(file.closed)

'''

# this is a better solution so that we can handle errors
try:
    with open('assets\\30_reading_a_file.txt') as file:
        content = file.read()
        print(content) # print the content of the file to the console
        print(len(content)) # get the number of characters in the file
        
        file.seek(0)  # seek back to the beginning of the file

        lines = file.readlines() # returns list of the lines
        print(lines)

        position = file.tell() # this tells us where exactly is Python (cursor) positioned in the file
        print(position)
except FileNotFoundError:
    print("That file was not found")


