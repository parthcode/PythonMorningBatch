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
# input_number = int(input("Enter a number"))
#
# if input_number % 2 == 0:
#     print("Even")
# elif input_number > 30:
#     print("greater than 30")
# else:
#     print("odd")



# user_name = ['alex', 'lexi', 'ramu kaka', 'lala land']
# name = input("Enter the name")
# if name in user_name:
#     print(True)
# else:
#     print(False)
user_details = {'Name': 'alex', 'age': 21, 'address': 'mumbai' }
name = input("Enter the name")
if name in user_details:
    print(True)
else:
    print(False)