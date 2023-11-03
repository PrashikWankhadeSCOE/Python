def outer():
    def inner():
        print("In inner function")
    def inner2():
        print("In inner2 function ")
    return inner,inner2
ret = outer()
for i in ret:
    print(i)
    i()

'''
<function outer.<locals>.inner at 0x7fdccdb49c10>
In inner function
<function outer.<locals>.inner2 at 0x7fdccdb49ee0>
In inner2 function
'''

