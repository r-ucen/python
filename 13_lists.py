food = ["pizza", "hamburger", "hotdog"]

print(food[0])

# overwrite an element
food[0] = "sushi"
print(food[0])

# print all elements in the list 
for item in food:
    print(item, end=" ") # the end=" " is potional

# get the number of elements in a list
print(len(food))

print(food[::-1]) # reverse the list
food.reverse() # or reverse it like this

# add a new item to the end of the list
food.append("ice cream")

# insert a value at a certain index
food.insert(1, "cake") # (index, value)

# remove a certain value
food.remove("hotdog")

# removes the last element
food.pop()

# get the index of an element
print(food.index("hamburger"))

# sort the list alphabetically
food.sort()

# removes all elements in the list
food.clear()

# removes elements on index 0 up to 2 (i mean up to index 3 but not including the index 3)
my_list6 = ["a", "b", "c", "d", "e", "f", "g"]
del my_list6[0:3]
print(my_list6)


# you can also unpack a small list
my_list = [4, "hi", True]
a, b, c = my_list
print(b)

# an element of a list can be another list
my_list2 = ["ahoj", 1.0, [2 , True]]
print(my_list2[2])

# an element of a list can also be a name of a function

def function_hello():
    print("Hello")

my_list3 = ["hi", 4, function_hello]
print(my_list3[2]()) # note that we have to call the function with ()

# the output of this would be Hello
#                             none
# because the function's return value is None

# this will output [1, 2, 3, 1, 2, 3, 1, 2, 3]
my_list4 = 3 * [1, 2, 3]
print(my_list4)

my_list = [0,1,2,3,4,5,6,7,8,9]
print(my_list[:3]) # elements with index 0, 1, 2
print(my_list[-3:]) # elements starting with third from the end
print(my_list[::2]) # every second element


my_list5 = ["a", "b", "c", "d", "e", "f", "g"] # creates a list
my_list5[2:5] = []  # it slices the list from c to g but assigns them to an empty list effectively removing them from the list
print(my_list5) # prints the modified list which is ['a', 'b', 'f', 'g']

# find out whether a list contains certain item 
my_list7 = ['Python','C+','C#', 'Java']
print('C+' in my_list7)

# or using the count method
print(my_list7.count('PHP')) # output 0 bcs the list doesnt contain PHP

# or uing the index method
print(my_list7.index('PHP')) # ValueError: 'PHP' is not in list

any([True, False, False, False]) # returns True if at least one of the items is True (True == 1)
all([0,1,0,0])  # returns True if all of the items are True (True == 1)

