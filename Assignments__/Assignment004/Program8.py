'''
WAP to pritn numbers which are divisible by 3 and 5 both given range
input :
    start 15
    end : 50
output :
    15 30 45
'''
def div(start,end):
    if(start==end):
        return 0;
    if(start%3 == 0 and start%5 ==0):
        print(start,end=" ")
    return div(start+1,end)
div(15,50)
