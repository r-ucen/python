# filter() = creates a collection of elemets from 
# an iterable for which a function returns true

# filter(function, iterable)

friends = [("Rachel", 19),
           ("Monica", 18), 
           ("Phoebe", 17),
           ("Joey", 16),
           ("Chandler", 21),
           ("Ross", 20)]

# we want to createa  separate list with people that are 18 yo or older
age = lambda data:data[1] >= 18

# filter(age, friends) # its gonna return a filter object so we should cast it to a list
allowed_to_drink = list(filter(age, friends))

for i in allowed_to_drink:
    print(i)