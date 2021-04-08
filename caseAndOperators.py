"""
1.If else statement
These are the case statement in python which executes a block of code based on a condition
2.operators
comp : > , < , == , !=, >= , <=
"""
# x = 90
# y = 10
# print("sum", x + y)
# print("difference", x - y)
# print("product", x * y)
# print("Divide", x/y)
# print("reminder", x % y)
"""
check if a number is odd or even
"""
input_number = int(input("Enter a number"))

if input_number % 2 == 0:
    print("Even")
elif input_number > 30:
    print("greater than 30")
else:
    print("odd")
