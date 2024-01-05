class Demo:
    def __init__(self):
        print('In constructor')

    def __del__(self):
        print('in decorator')

obj1 = Demo()
obj2 = Demo()
obj3 = obj1

del obj1

print('End Code')

'''
In constructor
In constructor
End Code
in decorator
in decorator
'''
