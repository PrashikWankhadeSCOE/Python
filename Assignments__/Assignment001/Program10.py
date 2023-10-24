'''
Program 10: WAP that determines whether a given input year is a leap
year or no
'''

i = int(input("Enter the year : " ))

if(i%400 == 0):
    print("its a leap year")
elif(i%100 == 0):
    print("not a leap year")
elif(i%4==0):
    print("Its a leap year")

