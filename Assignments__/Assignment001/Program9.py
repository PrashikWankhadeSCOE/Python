'''
Program 9: Write a program to check whether the input character is a vowel or
consonant
Input: ‘a’
Output: vowel
Input: ‘b’
Output: consonant
'''

i = input("Enter the alphabet : " )

if(i=='a' or i== 'e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='U' or i=='O'):
    print('%s is a vowel '%i)
else :
    print("%s is not a vowel its a consonent " %i)
