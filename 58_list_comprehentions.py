# list comprehention = a way to create a new list with less syntax
#                      can mimic certain lambda functions, easier to read
#                      1) list = [expression for item in iterable]
#                      2) list = [expression for item in iterable if conditional]
#                      3) list = [expression (if/else) for item in iterable]

# 1)
squares = []                # creates an empty list
for i in range(1, 11):      # create a for loop
    squares.append(i * i)   # define what each loop iteration should do
print(squares)

# ok so this is the same using list comprehention
squares2 = [i * i for i in range(1, 11)]
print(squares2)

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 2)
# ok and this is how we can mimic certain lambda functions

#* so this is how we write it using the lambda function
students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = list(filter(lambda x: x >=60, students))
print(passed_students)

# and this is how we write it using list comprehention
passed_students2 = [i for i in students if i >= 60]
print(passed_students2)

# [100, 90, 80, 70, 60]

# 3)
passed_students3 = [i if i >= 60 else "FAILED" for i in students]
print(passed_students3)

# [100, 90, 80, 70, 60, 'FAILED', 'FAILED', 'FAILED', 'FAILED']