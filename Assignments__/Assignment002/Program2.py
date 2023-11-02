'''
WAP to determine wheather entered angles define a right angled traingle 
take three values of angle from the user

input angle1 = 90
input angle2 = 90
input angle3 = 90

output
it is not a right angle traingle


input angle1 = 90
input angle2 = 60
input angle3 = 30

output
it is a right angle traingle

'''

angle1 = int(input("enter angle1 : "))
angle2 = int(input("enter angle2 : "))
angle3 = int(input("enter angle3 : "))

if(angle1+angle2+angle3 == 180):
    if(angle1 == 90 or angle2 == 90 or angle3 == 90):
        print("it is a right angle triangle")
    else:
        print("it is not a right angle triangle")
else:
    print("it is not a right angle triangle ")
