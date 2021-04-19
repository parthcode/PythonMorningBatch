"""
1.Write
2.read
3.append
ASK USER NAME , ADDRESS AND PHONENUMBER AND STORE IT INTO A TXT FILE(USER DETAILS)
use functions
"""
import os
file_path = os.getcwd() + '/pythonFile.txt'
name = input("Enter the name :")
# meta_data = open(file_path, 'w')
# meta_data = open(file_path, 'r')
meta_data = open(file_path, 'a')
meta_data.write('\n')
meta_data.write(f'your name is {name}')
# data = meta_data.read()
# data = meta_data.readlines()
meta_data.close()
