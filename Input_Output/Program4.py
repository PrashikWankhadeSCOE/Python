# Type 1

x = 10
y = 20
print(x)
print()   # this will print \n 
print(y)

'''
10

20
'''


# Type 2

print('Prashik')
print("Prashik")
print('''Prashik''')
print("""Prashik""")

# all this three works fine 

print("Prashik"+"Wankhade") # this will not add any space and concate it 
print("Prashik","Wankhade") # this will add extra space between two strings

print(3*"Prashik") # this will print the string 3 times 

"""

Prashik
Prashik
Prashik
Prashik
PrashikWankhade
Prashik Wankhade
PrashikPrashikPrashik
 
"""

# Type 3
# print(argrument list)

x = 10
y = 20
print(x,y) # 10 20  , will add a space in between 
print(x,y,sep=":")  #10:20  # sep keyword will add seprate both variables with the character we added in sep 
print(x,y,sep=",")  #10,20  # sep will add , in between 

# Type 4
# print(formated Output)

x = 10
y = 20.5

print("x is equal to %i" %x)
print("y is equal to %f" %y)

print("x is equal to %d" %x)

'''
x is equal to 10
y is equal to 20.500000
x is equal to 10
'''

