row = int(input("Enter the row number : "))
for i in range(row):
    for j in range(row):
        if(i%2==0):
            print(end="#\t")
        else:
            print(end="@\t")
    print()

