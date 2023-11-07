'''
x = 10
print(x)
print(id(x))
x = 20
print(x)
print(id(x))
# both ids are different 
'''
# Array is a first collection framework because it is collection of multicple elemnt

'''
Array can be imported in 3 ways 
import array as arr
import array
from array import *
'''
import array as arr

jerNo = arr.array('i',[45,77,18,96,1])
for data in jerNo:
    print(data)

    '''
    here jerNo : array
    arr : module
    arrray : function
    i : typecode/datatype
    [] : collection of multiple elements
    '''
