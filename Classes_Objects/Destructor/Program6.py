class Demo:
    def __init__(self):
        print('In Constructor')

    def __del__(self):
        print('in destructor')

print('Start code')
obj = Demo()
print('End code')

'''
Start code
In Constructor
End code
in destructor
'''
