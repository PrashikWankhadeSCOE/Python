import copy as cp

lang = ['Cpp','Java','Python',['Go','Rust','Dart']]
print(lang[0])
print(lang[1])
print(lang[2])
print(lang[3])
print(lang[3][0])
print(lang[3][1])
print(lang[3][2])

'''
Cpp
Java
Python
['Go', 'Rust', 'Dart']
Go
Rust
Dart
'''

newlist = lang.copy()
print(newlist)

'''
['Cpp', 'Java', 'Python', ['Go', 'Rust', 'Dart']]
'''

lang[3][1] = 'JavaScript'
print(lang)
print(newlist)

'''
here you will see that even the change has occured in the newlist which 
was copy of lang

['Cpp', 'Java', 'Python', ['Go', 'JavaScript', 'Dart']]
['Cpp', 'Java', 'Python', ['Go', 'JavaScript', 'Dart']]
'''

player = ['Rohit','Shubman','Virat']
newlist = player.copy()

print(player)
print(newlist)

player[1] = 'Shreyash'
print(player)
print(newlist)

'''
Here you can see the change is only in the above list but not in a copied list 
this is because in normal list the elements are copied
whereas in nested list the address is stored not a copy so in above nested list 
we changed the data and the copied list also changed the data in it a

['Rohit', 'Shubman', 'Virat']
['Rohit', 'Shubman', 'Virat']
['Rohit', 'Shreyash', 'Virat']
['Rohit', 'Shubman', 'Virat']
'''

# Deep copy
# we have imported the copy class above 

newlist = cp.deepcopy(lang)
print(lang)
print(newlist)

lang[3][1] = 'Rust'
print(lang)
print(newlist)


'''
Here deepcopy function has copied only in list we wanted to replace 
it has not edited in copy of lang newlist

['Cpp', 'Java', 'Python', ['Go', 'JavaScript', 'Dart']]
['Cpp', 'Java', 'Python', ['Go', 'JavaScript', 'Dart']]
['Cpp', 'Java', 'Python', ['Go', 'Rust', 'Dart']]
['Cpp', 'Java', 'Python', ['Go', 'JavaScript', 'Dart']]
'''
