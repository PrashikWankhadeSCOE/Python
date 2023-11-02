'''
Enter no of rows : 4
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
'''
row = int(input("Enter no of rows : "))
for i in range(row):
    a = i
    for j in range(row):
        a+=1
        print(a,end=" ")
    print()

