# map() = applies a function to each item in an iterable (list, tuple, etc.)
# map(function, iterable)

# lets say we have an online store
store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

# we want to convert each price to euros from dollars

to_euros = lambda data: (data[0], data[1] * 0.82)
# so what we did here is that we are representing a tuple using() after the :
# and the name of the cloth is data[0] and then the converted price is data[1] * 0.82
# so the first column will be untouched and the second column will be modified

# store_in_euros = map(to_euros, store) # this will create a map object
# we can convert it to any iterable we want so for example a list
store_in_euros = list(map(to_euros, store))

# we can also make a conversion to dollars from euros
to_dollars = lambda data: (data[0], data[1] / 0.82)

# and
store_in_dollars = list(map(to_dollars, store))

# now we can display the converted store prices
for i in store_in_euros:
    print(i)

for i in store_in_dollars:
    print(i)