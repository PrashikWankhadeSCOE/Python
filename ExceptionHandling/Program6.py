class Demo:
    def fun(self):
        print('In fun')

    def gun(self):
        print('In gun')

obj = Demo()
obj.fun()
obj = None
print(obj)
obj.gun()

#AttributeError 
