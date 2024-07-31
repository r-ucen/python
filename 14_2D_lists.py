# 2D list = a list of lists

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog", "sushi"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

print(food)

# output:
# [['coffee', 'soda', 'tea'], ['pizza', 'hamburger', 'hotdog', 'sushi'], ['cake', 'ice cream']]

print(food[0]) # prints the first item of the food list which is the drinks list

print(food[0][2]) # prints the 3rd item of the first list (tea)
print(food[2][1]) # prints the 2nd item of the 3rd list (ice cream)