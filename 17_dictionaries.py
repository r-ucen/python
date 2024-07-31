# dictionary = a changable, unordered collection of unique key:value pairs
#              it is fast because they use hashing, allow us to access a value quickly

capitals = {
    "USA":"Washington DC",
    "India":"New Dehli", 
    "China":"Beijing",
    "Russia":"Moscow"
}

print(capitals["Russia"]) # this is not very good, bcs if the key is not in the dictionary then we encounter an error

print(capitals.get("Germany")) # if a key is not in the dictionary, the output will be None

print(capitals.keys()) # this prints only the keys
print(capitals.values()) # prints only the values
print(capitals.items()) # prints keys and values

a = list(capitals.items()) # we can assign the output of the .items method to a list and access the values using indexing
print(a[0][0]) # prints USA
print(a[0][1]) # prints Washington DC

# displaying the dictionary using for loop
for key, value in capitals.items():
    print(key + ": ", value)

capitals.update({"Germany":"Berlin"}) # add another key:value pair
capitals.update({"USA":"Las Vegas"}) # this will change the value of the key USA to Las Vegas from Washington DC

capitals.pop("China") # this will remove the "China":"Beijing" key:value pair
# del capitals["China"] # or delete it like this

print(capitals.popitem()) # removes the last pair but returns this pair as a key:value pair

capitals.clear() # this will remove all key:value pairs

print('China' in capitals) # returns True if China key is in the dict

print(len(capitals)) # prints the number of pairs

# if the KEY is a string you can write a dict in this foramt as well 
my_dict = dict(brand ='Skoda', model='Octavia', year=1998)

# this time we have to use the :
my_dict2 = {1:5, 2:8, 6:'c'}

# you can put dictionaries together using the update() method
my_dict = {
  "brand": "Skoda",
  "model": "Octavia",
  "year": 1998
}
my_dict2 = {
  "fuel": "petrol",
  "max_speed": 240
}
my_dict.update(my_dict2)
print(my_dict)
