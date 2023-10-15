num = int(input("Enter the number : "))

if(num>0):
    print("{} is greater than zero ".format(num))
elif(num<0):
    # elif is a short form of else if 
    # if we want to use else if will also work perfectly
    print("{} is less than zero ".format(num))
else:
    print("num is zero")

