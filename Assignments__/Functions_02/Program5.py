def outer():
    def inner(outer):
        print(outer)
        return inner
    return inner(outer)

if __name__ == "__main__":
    retObj = outer()
    print(retObj)

'''
address of outer function
address of inner function
'''
