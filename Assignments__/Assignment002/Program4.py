'''
Take a number from the user and check whether it is present in the list 
if it's in the list print "Availble"

List1 = [10,20,30,40,50]
'''

List1 = [10,20,30,40]
x = int(input("Enter number you want to check : "))
if (x in List1):
    print("{} is available".format(x));
