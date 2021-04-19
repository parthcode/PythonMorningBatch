import functions
from functions import add_number

first_number = int(input("Enter the first number"))
second_number = int(input("Enter the second number"))

operation = input("Enter the operation(+,*,/)")

if operation == "+":
    print(f'Sum is : {add_number(first_number,second_number)}')
elif operation == "/":
    print("Divisor is :", functions.divide(first_number, second_number))
elif operation == "*":
    print("Product is :", functions.multiply_number(first_number, second_number))
else:
    print("Please enter a valid operation")
