def fun():
    print('Fun')
def fun(x):
    print('In fun -- x')

print('Start')          #Start
fun()                   #TypeError: fun() missing 1 required positional argument: 'x'
fun(10)                 #--------------------------
print('End')

'''
here fun with 0 parameter is overridden by fun with 1 parameter
so if we call fun(10) before fun() it will call the function and then thrw the error
'''
