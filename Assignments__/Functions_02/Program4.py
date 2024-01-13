def outer():
    def inner():
        return outer
    return inner

if __name__ == "__main__":
    retobj = outer()
    retInner = retobj()
    print(retInner)

'''
prints the address or hashcode of the outer function
'''
