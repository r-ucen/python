# set = a collection which is unordered, inundexed and has no duplicate values

utensils = {"fork", "spoon", "knife"}

for x in utensils:
    print(x)

# when we run this it might be displayed in different order each time
# sets are faster than lists, so thats good if you need to know whether an item is in a set
    

# this will still print only one knife
utensils = {"fork", "spoon", "knife", "knife", "knife", "knife", "knife"}
for x in utensils:
    print(x)

utensils.add("napkin")
utensils.remove("fork")
utensils.clear()

dishes = {"bowl", "plate", "cup"}

dinner_table = utensils.union(dishes) # this will create a new set containing all items from these two sets

utensils.update(dishes) # this will add dishes into the utensils set

for x in utensils:
    print(x)

# we can check for similarities in the sets
set_a = {"fork", "spoon", "knife"}
set_b = {"bowl", "plate", "cup", "knife"}

print(set_a.difference(set_b)) # this will print what set_a has and set_b doesnt
print(set_a.intersection(set_b)) # will print what they have in common
