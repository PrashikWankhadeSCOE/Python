'''
Enter the no of row : 4
1       3       5       7
5       7       9       11
9       11      13      15
13      15      17      19
'''
row = int(input('Enter the no of row : '))
a = 1
for i in range(row):
    n = a
    for i in range(row):
        print(n,end="\t")
        n+=2
    a+=4
    print()
