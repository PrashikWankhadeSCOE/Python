'''
Enter no of row : 3
1       3       5
7       9       11
13      15      17
'''

row = int(input("Enter no of row : "))
n = 1
for i in range(row):
    for j in range(row):
        print(n,end="\t")
        n+=2
    print()

