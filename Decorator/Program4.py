# this is also known as abstract factory design pattern

def decorFun(fun):
    print('In decor fun')

    def wrapper(*args):
    
        print('Start wrapper')
        val = fun(*args)
        print('End wrapper')
        return val

    return wrapper

@decorFun
def normalFun(x,y):
    print('in normal fun')
    return x+y

'''
normalFun = decorFun(normalFun)
'''

print(normalFun(10,20))
