def decorFun(fun):
    print('In decor fun')

    def wrapper() :
        print('in wrapper')
        fun()
        print('End Wrapper')

    return wrapper

@decorFun
def normalFun():
    print('This is normal Function')

'''
normalFun = decorFun(normalFun)
normalFun()
'''

normalFun()


'''
This both things reffer to same thing if 
we write @decorFun then it will be decorator but 
you can see here how the decorator func works here
from above commented code
'''
