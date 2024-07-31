# note that we have the 'w' there, thats mode for writing into a file

with open('assets\\31_writing_into_a_file.txt', 'w') as file:
    file.write("Hiiiiiiiiii\nThis is some text\n")

# if we left the 'w' mode here the previous text would be overwritten
# so we use the 'a' mode which stands for append
with open('assets\\31_writing_into_a_file.txt', 'a') as file:
    file.write("I have added this text")