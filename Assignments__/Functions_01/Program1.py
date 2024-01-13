# what is the output of the following function?

def outer():
    def inner():
        return "Hello, I'm in the inner function!"
    return inner()

ans = outer()
print(ans)

#My prediction
"""
Hello, I'm in the inner function!
"""
