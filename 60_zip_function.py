# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples
#                   for each element within the zip object

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p&ssword", "abc123", "guest")

users = list(zip(usernames, passwords)) # creates a list of tuples

for i in users:
    print(i)

'''
('Dude', 'p&ssword')
('Bro', 'abc123')
('Mister', 'guest')
'''

# we can also make it a dictionary
users = dict(zip(usernames, passwords))

for key, value in users.items():
    print(key + " : " + value)

# OK SO WHAT IF WE HAVE MORE THAN 2 ITERABLES?

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p&ssword", "abc123", "guest")
login_date = ["1.1.2024", "1.2.2024", "1.3.2024"]

users = list(zip(usernames, passwords, login_date))
for i in users:
    print(i)

'''
('Dude', 'p&ssword', '1.1.2024')
('Bro', 'abc123', '1.2.2024')
('Mister', 'guest', '1.3.2024')
'''