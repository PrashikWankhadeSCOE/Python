# positional argument
# every excess thing will be stored in *argv as tuple 
# when we dont know how many element are gonnna come from function we use positional argument
# positional argument is also at the right side 

def fun(x,y,*argv):
    print(x)
    print(y)
    print(argv)
fun(10,20,30,40,50,60,70)

