# sort() method = used with lists
# sort() function = used with iterables like tuple etc. (i guess you can also use it with list)
# the sort() function generates a new list without chaning the original one
students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]

# sort() method
'''
students.sort()
# students.sort(reverse = True)

for student in students:
    print(student)
'''
# sort() function
'''
sorted_students = sorted(students)
# sorted_students = sorted(students, reverse=True)


for student in sorted_students:
    print(student)
'''

# lets have a list of tuples
'''
students = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78)]

# so how do we sort this list by either the students name, grade or their age?
students.sort() # sorting by the first column

grade = lambda grades: grades[1] # this is a function object via the lambda function
students.sort(key = grade, reverse=True) #  can be also reversed

age = lambda ages: ages[2] # sorted by the 3rd column (youngest to oldest)
students.sort(key = age)

for i in students:
    print(i)
'''
# lets have a tuple of tuples
students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78))

age = lambda ages: ages[2]
sorted_students = sorted(students, key = age)

for student in sorted_students:
    print(student)