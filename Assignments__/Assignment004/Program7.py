'''
WAP that prints all positive numbers form a given range
input :
    start = -7
    end = 8
'''
def pos(start,end):
    if(start == end):
        return 0
    if(start>0):
        print(start , end=" ")
    return pos(start+1,end)
pos(-7,8)
