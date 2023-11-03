def outer(x,y):
    def inner(a,b):
        print("In inner function ")
        return a+b
    print("In Outer function")
    print(x+y)
    return inner
ret = outer(10,20)
inRet = ret(5,6)
print(ret) # here ret wull print the address of the inner class 

'''
In Outer function
30
In inner function
<function outer.<locals>.inner at 0x7fb10d304c10>
'''
