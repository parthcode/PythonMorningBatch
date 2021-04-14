"""
Loops:
Why: This concept is used to execute a block of code until a specific condition is True
1.for
2.while
"""
# print 1-10:
# for i in range(10):
#     print(i)
"""
fibonacci series
1,2,3,5,8.....
ask user the range of the series and print the above series
"""
# start = 0
# end = 1
# for i in range(8):
#     result = start + end
#     print(result)
#     start = end
#     end = result
"""
Filter the string and integer from a list to a new list
"""
# list_values = [1, 2, 3, 4, 'pwd', 43, 'abc', 'xyz']
# list_int = []
# list_string = []
# for i in list_values:
#     if type(i) == type(12):
#         list_int.append(i)
#     else:
#         list_string.append(i)
# print(list_int)
# print(list_string)
list_values = [1, 2, 3, 3, 'pwd', 2, 'abc', 'pwd']
# find all the values which are repeated in the above list


list_key = [2, 3, 4, 5, 6]
dic_values = {}
# Fill the above dict with the keys from the list and relevant square as values
# example : {2:4, 3:9, 4:16...}

str_value = 'aABbc'
# convert all the cap letter to small letter
# hacker rank
print(str_value.islower())