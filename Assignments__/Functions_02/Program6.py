def outer():
    def inner1(a,b):
        print("In inner1")
        return a-b
    
    def inner2(obj):
        print('in inner2')
        print(obj)
        return inner2

    retInner1 = inner1(10,4)
    retInner2 = inner2(retInner1)
    return retInner2

if __name__ == "__main__":
    retObj = outer()
    print(retObj)

'''
in inner1
in inner2
6
address of inner2
'''

'''
In inner1
in inner2
6
<function outer.<locals>.inner2 at 0x7f556081aee0>
'''

