def fun(x,y):
    print('start fun')
    while(x<=y):
        yield x
        x = x+1
    print('End fun')

for val in fun(1,10):
    print(val)
