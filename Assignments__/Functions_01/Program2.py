# What is the output of the following function? (dry  run compulsary)

def outer():
    def inner():
        return "Hello . I am in the inner Function !!"
    return inner

ret = outer()
retin = ret()

print(retin)

'''
Hello . I am in the inner Function !! 
'''
