age = int(input("How old are you?: "))

if age <= 0:
    print("You havent been born yet!!!")
elif age < 18:
    print("You do not have the permission to vote yet")
else:
    print("You can vote!")