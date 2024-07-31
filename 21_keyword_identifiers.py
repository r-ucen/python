# the order of arguments DOES NOT matter but we need to precede the argument with an identifier

def alphabet(first, second, third):
    print(f"in the alphabet the first is {first}, second is {second} and third is {third}")

alphabet(third = "c", first = "a", second = "b")