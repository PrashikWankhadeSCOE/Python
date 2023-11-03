

def outer():
    def inner():
        print("In inner function")
    print("In outer function")
    inner()
print("Start code")
outer()
print("End Code")

'''
Start code
In outer function
In inner function
End Code
'''
