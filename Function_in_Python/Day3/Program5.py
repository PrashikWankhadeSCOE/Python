def outer():
    def inner1(x,y):
        print("In inner1 fun")
        return x+y
    def inner2(a,b):
        print("in inner2 fun")
        return a*b
    return inner1,inner2
inn1,inn2 = outer()
ret1 = inn1(5,10)
ret2 = inn2(5,10)

print(ret1+ret2)
print(inn1)
print(inn2)
'''
In inner1 fun
in inner2 fun
65
<function outer.<locals>.inner1 at 0x7f14df4e4c10>
<function outer.<locals>.inner2 at 0x7f14df4e4ee0>
'''
