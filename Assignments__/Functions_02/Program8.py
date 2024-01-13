def outer():
    message = "I am the outer function"

    def inner():
        return message

    return inner

if __name__ == "__main__":
    in_fun = outer()
    result = in_fun()
    print(result)

'''
I ma the outer function
'''
