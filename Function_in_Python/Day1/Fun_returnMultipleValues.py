# python has a special feature of returning multiple values from same function
# in python al the values are stored in a tuple and then returned if multiple values are returned

def add10(a,b,c):
    a = a+10
    b = b+10
    c = c+10
    return a,b,c
a = int(input())
b = int(input())
c = int(input())
x = add10(a,b,c)
print(x)

'''
10
20
30
(20, 30, 40)
'''
