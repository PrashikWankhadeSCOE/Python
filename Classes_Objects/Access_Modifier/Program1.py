# there is nothing like private in python we can even access the private variables in python 
# just we need to goo that deep in python need to know the internal 
# how does python store the private variable 
# pythone internally does name mangling which is then converted as _className__privateVariable

class Demo:
    z = 30 # this is a public access accessModifier

    def __init__(self):
        self._x = 10  # protected is 
        self.__y = 20   # private ------ it is internally converted as _Demo__y

print(dir(Demo))
obj = Demo()
print(dir(obj))

'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'z']
['_Demo__y', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_x', 'z']
'''
