#rows  = int(input("Enter the number of rows: "))
#columns = int(input("Enter the number of columns: "))
#symbol = input("Enter the symbol you want the shape to consist of: ")

rows = 4
columns = 4
symbol = "@"

for i in range(rows):
    for j in range(columns):
        print(symbol, end="") # we have to put end="" to prevent a new line character
    print() # after the inner loop finishes we actaully want to print a new line character

# pyramid
floors = 4
star = "*"
space = " "

for i in range(floors):
    print(space * (floors - i) + star * (i + i + 1))

'''

   *
  ***
 *****
*******

'''


