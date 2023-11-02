'''WAP to print al even number form a given range 
input :
    start = 10
    end = 20
output : 
    10 12 14 16 18 

'''

def printEven(start,end):
    if(start >= end):
        return 0
    if(start%2 == 0):
        print(start)
    return printEven(start+1,end)
printEven(10,20)
