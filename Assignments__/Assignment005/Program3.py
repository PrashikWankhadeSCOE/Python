
'''

Enter the number of rows : 4
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4

'''
row = int(input("Enter the number of rows : "))
for i in range(row):
    for j in range(row):
        print(i+1,end=" ")
    print()
