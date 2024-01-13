def outer(flag):
    def inner():
        return "This is true " if flag else "This is false"
    return inner

if __name__ == "__main__":
    true_func = outer(True)
    false_func = outer(False)

    print(true_func())
    print(false_func())

'''
This is true
this is false
'''
