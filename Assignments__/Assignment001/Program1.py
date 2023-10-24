# Topic IF-Else
'''

1. Program 1: Write a Program to Find a Maximum between two numbers
Input: 1 2
Output: 2 is Max number between 1 & 2

'''
a = int(input("First number : "))
b = int(input('Second number : '))

if(a>b):
    print("%i is greater than {}".format(b)%a)
else:
    print("%i is greater than {}".format(a)%b)
