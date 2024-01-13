class Demo:
    def fun(self):
        print("Demo")

class Memo:
    def gun(self):
        print("Memo")

def callFun(obj):
    if(hasattr(obj,'fun')):
        obj.fun()
    else:
        obj.gun()

obj1 = Demo()
obj2 = Memo()

callFun(obj1)
callFun(obj2)

'''
Demo
Memo
'''
