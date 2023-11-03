# defasult parameter 
# defalt parameter has to be at the right side of normal parameter or it will be error
# compile time error

def add(x,y,z = 30):
    print(x)
    print(y)
    print(z)
add(10,20)
add(10,20,40)

'''
10
20
30
10
20
40
'''
