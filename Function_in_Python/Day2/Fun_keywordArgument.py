# Keyword argument 
# all data here will be stored in key value pair in dict

def fun(**args):
    print(args)
    print(type(args))
fun(x=10,y=20,z = 30)
