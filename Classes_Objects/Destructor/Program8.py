class Demo:
    def __init__(self):
        print('In constructor')

    def __del__(self):
        print("In destructor")

def fun():
    print('in function')
    obj = Demo()
    print('End Fun')

fun()
print('End code')

'''
in function
In constructor
End Fun
In destructor
End code
'''
