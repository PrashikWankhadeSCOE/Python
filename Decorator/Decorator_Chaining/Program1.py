def decorFun(fun):
    def wrapper():
        print('In wrapper 1')
        fun()
        print('End wrapper 1')
    return wrapper

def decorRun(fun):
    def wrapper():
        print('In wrapper 2')
        fun()
        print('End wrapper 2')
    return wrapper

@decorRun
@decorFun
def normalFun():
    print('In normal Fun')


normalFun()
