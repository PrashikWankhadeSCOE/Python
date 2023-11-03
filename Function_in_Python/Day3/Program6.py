def outer():
    def inner():
        print("In inner")
    return inner
    print("in Outer")
retObj = outer()
retObj()

# In inner

