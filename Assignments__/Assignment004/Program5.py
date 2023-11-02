'''
WAP to print the number divisible by 7 but not divisible by 3 between 1 to 100
'''
def numdiv(start,end):
    if(start == end):
        return 0
    if(start%7 == 0 and start%3!= 0):
        print(start)
    return numdiv(start+1,end)
numdiv(1,100)
