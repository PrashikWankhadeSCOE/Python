'''
WAp to print the sum of all numbers from a given range
input :
    Start = 1
    end = 10
Output :
    45
'''

def sum(start, end):
    if(start==end):
        return 0;
    return start+sum(start+1,end)
print(sum(1,10))
