#Multiple Inheritance 
# MRO => Method resolution order 

class Parent1 :
    def dispData(self):
        print('In Display data')

class Parent2 :
    def printData(self):
        print('In Parent2 Print data')

class Child(Parent1,Parent2):
    pass

obj = Child()
obj.printData()
obj.dispData()
