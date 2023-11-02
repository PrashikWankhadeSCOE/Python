'''
WAP to print number from given range 
input : start = 100
input : end = 110

output : 100 101 102 103 104 105 106 107 108 109
'''

def printRange(start,end):
    if(start == end):
        return 0
    print(start)
    return printRange(start+1,end)

printRange(100,110)
