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
start = 0
end = 1
for i in range(8):
    result = start + end
    print(result)
    start = end
    end = result