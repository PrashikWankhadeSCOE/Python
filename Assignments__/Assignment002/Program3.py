'''
take two number from user and print the sum of those numbers 
if the sum is even 
input num1 = 10
input num2 = 20
outpur 30 is a even 

'''

x = int(input("Enter the num 1  : "))
y = int(input("Enter num2 : "))

a = x+y

if(a%2==0):
    print("{} is a Even number ".format(a))
