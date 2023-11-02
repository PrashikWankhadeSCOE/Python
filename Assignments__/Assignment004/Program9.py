'''
WAP to print the count of all negative numbers from a given range
input :
    start = -15 
    end = 50
output :
    15
'''

def count(start,end):
    if(start==end):
        return 0;
    if(start<0):
        return 1+count(start+1,end)
    return count(start+1,end)
print(count(-15,50))
