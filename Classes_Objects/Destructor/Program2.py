class Parent:
    def __init__(self):
        print('in constructor')
    def __del__(self):
        print('Destructor')

obj1 = Parent()
obj2 = Parent()

print("End Code")


'''
in constructor
in constructor
End Code
Destructor
Destructor
'''
