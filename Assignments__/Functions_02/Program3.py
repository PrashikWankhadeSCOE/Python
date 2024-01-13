def outer():
    def inner():
        return "This is the inner function ."
    return inner

if __name__ == "__main__":
    retobj = outer()
    retInner = retobj()

    print(retInner)

'''
This is the inner function
'''
