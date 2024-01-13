def outer():
    def inner():
        return "Hello Core2Web !!"

    return inner
    print("In outer funtion")

if __name__ == "__main__":
    result = outer()()
    print(result)


"""
hello core2web !
"""

'''
Hello Core2Web !!
'''
