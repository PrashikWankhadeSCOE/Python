class Data:
    pass
print(dir(object))
print(dir(Data))

#Python3

'''
here you can see that the Data has all methods from object which means that all methods are inherited from parent object
i.e object is parent of Data

['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
'''
#Python2 
'''
But whereas in python2 you can see that Data has only 2 methods and object has so many methods 
so we can say that object is not parent of Data class 
which is created by us 
in python2 to make any class parent of any class you have to compulsaty write it in brackets 
there is noting like object or anything which is ultimate parent of all the classes as it is now in python3 
where object class is the head of the hirarchy

['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

['__doc__', '__module__']
'''
