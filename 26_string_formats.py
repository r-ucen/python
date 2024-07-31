name = "Bro"
print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))

#Hello, my name is Bro       . Nice to meet you
#Hello, my name is        Bro. Nice to meet you
#Hello, my name is    Bro    . Nice to meet you

# NUMBER FORMAT

number = 3.14159
number2 = 1000000000

print("The number is {:.2f}".format(number)) # 3.14
print("The number is {:,}".format(number2))  # 1,000,000,000
print("The number is {:b}".format(number2))  # display the number in binary
print("The number is {:o}".format(number2))  # display in octal numberal system
print("The number is {:X}".format(number2))  # display in hexadecimal
print("The number is {:E}".format(number2))  # in scientific notation

