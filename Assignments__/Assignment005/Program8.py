'''
Enter no of rows : 3
1       3       5
1       3       5
1       3       5
'''
row = int(input("Enter no of rows : "))
for i in range(row):
    n = 1
    for j in range(row):
        print(n,end="\t")
        n+=2
    print()

