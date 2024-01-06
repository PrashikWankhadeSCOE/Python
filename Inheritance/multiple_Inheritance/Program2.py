class Data:
    pass

print(type(Data))
obj = Data()

print(type(obj))
print(type(object))
print(type(type))

# python2 
'''
<type 'classobj'>
<type 'instance'>
<type 'type'>
<type 'type'>
'''
#python3
'''
<class 'type'>
<class '__main__.Data'>
<class 'type'>
<class 'type'>
'''
