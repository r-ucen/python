# scope = the region inside which a variable is recognized

name = "global"

def display_name():
    name = "local"    # local variable
    print(name)

print(name) # this will use the global variable
display_name() # this will use the local variable


'''
btw Python first uses this:
    L = local       
        then:
    E = Enclosing
        then:
    G = Global
        then:
    B = Built-in
'''