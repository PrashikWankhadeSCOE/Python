x  = int(input("Enter the number : "))

y = int(input("Enter the number : "))

for i in range(x,y+1):
    if(i%2 == 0):
        print("%i is a even number "%i)
    else:
        print("%i is a odd number "%i)
