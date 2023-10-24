'''
Program 8: Write a program to check whether the number is greater than 10 or
not
Input: 12
Output: yes 12 is greater than 10
Input: 2
Output: no 2 is less than 10
'''

i = int(input("Enter the number : "))

if(i>10):
    print("yes %i is greater than 10 "%i)

else:
    print("NO, %i is less than 10"%i)
