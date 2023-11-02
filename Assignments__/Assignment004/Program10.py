'''
WAP program to calculate and print the product of the count of odd
number within a given range
input :
    start = 1
    end = 11
output :
    3125
'''
def pro(start,end):
    if(start==end):
        return 1;
    if(start%2==1):
        print(start)
        return start*pro(start+1,end)
    return pro(start+1,end)
print(pro(1,11))

