def sumN(a):
    sum = 0
    for i in range(a+1):
        sum = sum + i
    return sum
x = int(input("Enter the digit you want sum till : "))
print(sumN(x))
