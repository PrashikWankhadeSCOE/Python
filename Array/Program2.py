# Array functions

'''
append()
buffer_info()
count()
extend()
fromlist()
index()
insert()
pop()
remove()
reverse()
tolist()
'''

import array as arr

data = arr.array('i',[10,20,30,40,50])

data.append(60)
print(data) #array('i', [10, 20, 30, 40, 50, 60])
print(data.buffer_info()) # (140039375217360, 6) # (bufferinfo address not array address,no of elements)
print(id(data)) # 139839546206768 as this is difff form upper one this is the address of array
print(data.count(30)) # 1 counts the no of time the element has occured in the array and the method has 1 parameter

# data.extend(70,80) this will be error because the method has iterable as parameter so no direct data is accepted 

data.extend([70,80])
print(data)

listdata = [10,20,30,40]
arrdata = arr.array('i',[100,200,300,400])

print(arrdata)

arrdata.fromlist(listdata)
print(arrdata)

print(arrdata.index(400)) # 3

arrdata.insert(4,500) # inset(index,value)
print(arrdata) # array('i', [100, 200, 300, 400, 500, 10, 20, 30, 40])

arrdata.pop()
print(arrdata)

arrdata.remove(100)
print(arrdata)

arrdata.reverse()
print(arrdata)

copylist = arrdata.tolist()
print(copylist)
