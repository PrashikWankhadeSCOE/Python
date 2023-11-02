'''
WAP to print all the character values of a given ascii value range from the user
input :
    enter the start range 1
    enter the end ange 2
output :
    wrong input 
'''

def ascii(start,end):
    if(start == end+1):
        return 0
    print("The charachter of ascii %i is "%start , chr(start))
    return ascii(start+1,end)
ascii(65,90)
