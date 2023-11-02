'''
Enter the no of rows : 4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
'''

row = int(input("Enter the no of rows : "))
for i in range(row):
    for j in range(row):
        print(j+1,end =" ")
    print()
