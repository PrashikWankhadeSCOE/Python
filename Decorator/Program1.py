def OuterFun():
    print('In outer fun')
    def inner():
        print('Inner 1')
    def inner2():
        print('Inner 2')
    return inner,inner2
ret = OuterFun()
for i in ret:
    i()
