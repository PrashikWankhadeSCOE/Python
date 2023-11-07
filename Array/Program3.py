# Array Slicing

import array as arr

arrdata = arr.array('i',[10,20,30,40,50])
for data in arrdata[1:8]:
    print(data)
# this wont give array index out of bounds as it will stop automatically but 
'''
print(arrdata[8])
'''
# this will give array index out od range
