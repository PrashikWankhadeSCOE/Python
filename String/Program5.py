# Check if str2 is present in str1 

str1 = input()
str2 = input()

if str2 in str1:
    print("Found")
else :
    print("Not found")

n = str1.find(str2)
if n == -1:
    print("Not found")
else :
    print("found")
