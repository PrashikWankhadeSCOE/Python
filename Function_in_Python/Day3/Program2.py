def outer(x,y):
    def inner():
        print("In inner function")
    print("In outer fun")
    return inner
ret = outer(10,20) # here we have returned the inner function's address
ret() # here we have called the address we have copied in ret so it will indirectly call the inner function

'''
In outer fun
In inner function
'''
