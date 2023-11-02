'''
WAp to print all the ascii values from a given character range
input :
    A
    Z

'''

def ascii(start,end):
    if(ord(start) == ord(end)+1):
        return 0
    
    print(ord(start) ," is ascii of {}".format(start))

    return ascii(chr(ord(start)+1),end)
ascii('A','Z')
