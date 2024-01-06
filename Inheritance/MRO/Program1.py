class Parent1:
    def dispData(self):
        print('In dispData')
    
class Parent2:
    def printData(self):
        print('In printData')

class Child(Parent2,Parent1):
    pass

obj = Child();
obj.printData()
obj.dispData()
