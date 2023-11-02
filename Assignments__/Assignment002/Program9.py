'''
Take two character form user check if the ascii value of both og character are odd then print the sum of ascii values of character
'''

a = input("Enter the character : ")
b = input("Enter the character : ")

if(ord(a)%2 != 0 and ord(b)%2 != 0):
    print(ord(a)+ord(b))

