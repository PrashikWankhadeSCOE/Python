'''
Program 6: Write a Program to check whether the Character is Alphabet or
not.
Input: v
Output: v is an alphabet.
'''

i = input("Enter the character : ")

if(i>='a' and i<='z') or (i>='A' and i<='Z'):
    print("%s is a alphabet "%i)
else:
    print("%s is not an alphabet"%i)
