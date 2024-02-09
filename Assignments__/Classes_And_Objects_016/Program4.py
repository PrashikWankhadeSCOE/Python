#remaining


'''
Create one parent class with the attribute methdods and instance variables,
write the same method in the child clas, make the object of the child class,
call the method and write the output
'''

class Parent:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    
    def att(self):
        return a+b+c

class Child(Parent):
    
    def att(self):
        return a+b+c

obj = Child(10,20,30)
print(obj.att())
