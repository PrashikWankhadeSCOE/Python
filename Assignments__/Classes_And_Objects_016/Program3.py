'''
Create the Parent have the @clasmethod, @staticmethod and instance method
and call all these functions by creating the object of the child class
'''

class Parent:
    @classmethod
    def cm(self):
        print("In class mehtod")
    
    @staticmethod
    def sm(self):
        print('In static method')

    def fun(self):
        print('In instance method')

class Child(Parent):
    pass

obj = Child()

obj.fun()
obj.cm()
obj.sm()


'''
Static method cannot be accesed from the child object also

'''

