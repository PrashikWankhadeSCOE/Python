'''
Enter the row : 3
* * *
* * *
* * *

Enter the row : 5
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
row = int(input("Enter the row : "))

for i in range(row):
    for j in range(row):
        print(end="* ")

    print()

