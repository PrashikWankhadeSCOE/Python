'''
Enter the no of rows : 3
1       3       5
3       5       7
5       7       9
'''
row = int(input("Enter the no of rows : "))
a = 1
for i in range(row):
    n = a
    for i in range(row):
        print(n,end="\t")
        n+=2
    print()
    a+=2

