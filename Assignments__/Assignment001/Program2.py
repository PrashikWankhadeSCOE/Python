'''
Program 2: Write a Program to check whether the number is Negative,
Positive or equal to Zero.
Input: -2
Output: -2 is the negative number

'''
i = int(input("Enter the number : "))

if(i<0):
    print("%i is less than zero "%i)
elif(i>0):
    print("%i is greater than zero "%i)
else:
    print("0 is zero")


