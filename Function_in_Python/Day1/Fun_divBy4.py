def divBy4(x):
    if(x%4 == 0):
        return "divisible by 4"
    else:
        return "Not divisible by 4 "

x = int(input())
print(divBy4(x))
