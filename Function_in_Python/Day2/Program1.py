# multiply all numbers coming from user in function 

def mult(*args):
    mult = 1;
    for i in args :
        mult = mult*i
    return mult
ret = mult(1,2,3,4,)
print(ret)
