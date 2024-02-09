'''
Write a real-time example for classes and objects which include @classmethod ,@staticmethod and 
instance method
'''

class Parent:
    @classmethod
    def cm(self):
        print("In class mehtod")

    @staticmethod
    def sm():
        print('In static method')

    def fun(self):
        print('In instance method')

class Child(Parent):
    pass

obj = Child()

obj.fun()
obj.cm()
obj.sm()
