"""
Functions
How to pass parameters
how to return parameters
first class functions
decorators
"""


# def add_number(a,b):
#     print("The sum is :",a+b)
#     return a+b
#
#
# a = 20
# b = 20
# add_number(a,b) # Only pass the number of parameters defined in the function
# print(add_number(a,b))

#########################################
# defination
def something(*a):
    print(a)


something('alex',12,'pwd','abc','london') #caller statement
###
#