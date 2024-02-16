# this will open the file which is present in the folder in read mode
# if file is not present then it will throw FileNotFoundError

fileObj = open("readme.txt",'r')
print(fileObj.read())
'''
hello this
is
readme
file
just to
read
from a py
file

'''
print(fileObj)

'''
<_io.TextIOWrapper name='readme.txt' mode='r' encoding='UTF-8'>
'''

# read , readline, readlines

f1 = open('readme.txt','r+')
print(f1.read(5))
#this will read first 5 character of the readme.txt file
'''
hello
'''
print(f1.readline())
# this will read the file till it find \n
'''
 this
'''

print(f1.readlines())

# this will store the data in list and print the list
'''
['is \n', 'readme\n', 'file \n', 'just to \n', 'read \n', 'from a py \n', 'file\n']
'''
