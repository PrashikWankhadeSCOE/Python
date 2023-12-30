class Parent:
    def __init__(self):
        print("In constructor")

    def __del__(self):
        print("In destructor")

obj1 = Parent()
obj1 = Parent()

print('End code')


'''
In constructor
In constructor
In destructor
End code
In destructor
'''
