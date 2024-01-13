class Demo:
    def fun(self):
        print("In fun: Demo")

class Memo:
    def fun(self):
        print("In fun : Memo")

def callFun(obj):
    obj.fun()

obj1 = Demo()
obj2 = Memo()

callFun(obj1)
callFun(obj2)


'''
In fun: Demo
In fun : Memo
'''
