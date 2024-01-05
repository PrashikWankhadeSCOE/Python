class Parent:
    def __init__(self):
        print('In Parent constructor ')
        print(type(self))

    def parentfun(self):
        print('In  Parent Function')

class Child(Parent):
    def __init__(self):
        super().__init__()
        print('In Child Constructor')
        print(type(self))
        
    def childFun(self):
        print('In Child Functuion')

obj = Child();

