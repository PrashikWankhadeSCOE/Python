# Dictionary
# in a dictionary, keys must be unique but values can be duplicated

player = {}
print(type(player))     # <class 'dict'>

player1 = {45:'Rohit',77:'Shubman',18:'Virat',1:'Kl Rahul'}
print(type(player1))
print(player1)

'''
<class 'dict'>
{45: 'Rohit', 77: 'Shubman', 18: 'Virat', 1: 'Kl Rahul'}
'''

player2 = dict({45:'Rohit',77:'Shubman',18:'Virat',1:'Kl Rahul'})
print(player2)
print(type(player2))


# player2 = dict(45:'Rohit',77:'Shubman',18:'Virat',1:'Kl Rahul')
# SyntaxError : Invalid Syntax

'''
{45: 'Rohit', 77: 'Shubman', 18: 'Virat', 1: 'Kl Rahul'}
<class 'dict'>
'''

# all data from internet comes in key: value pair format

myInfo = {'name':'Prashik',3:['Java','Python','Flutter']}
print(myInfo)

'''
{'name': 'Prashik', 3: ['Java', 'Python', 'Flutter']}
'''

player = {45:'Rohit',77:'Shubman',18:'Virat',1:'KL Rahul','next to bat':{96:'Shreyash',63:'SKY',8:'Jaddu'}}
print(player)
print(type(player))

'''
{45: 'Rohit', 77: 'Shubman', 18: 'Virat', 1: 'KL Rahul', 'next to bat': {96: 'Shreyash', 63: 'SKY', 8: 'Jaddu'}}
<class 'dict'>
'''

print(player[18])
print(player[1])
print(player['next to bat'])
# print(player[3])      '''key error [3]'''
print(player['next to bat'][96])
# print(player['next to bat'][0])       '''key error [0]'''

'''
Virat
KL Rahul
{96: 'Shreyash', 63: 'SKY', 8: 'Jaddu'}
Shreyash
'''

player = {45:'Rohit',77:'Shubman',18:'Virat',1:'KL Rahul','next to bat':{96:'Shreyash',63:'SKY',8:'Jaddu'},77:'XYZ'}

print(player)

'''
77 key now refer to XYZ 
{45: 'Rohit', 77: 'XYZ', 18: 'Virat', 1: 'KL Rahul', 'next to bat': {96: 'Shreyash', 63: 'SKY', 8: 'Jaddu'}}
'''

# Dictionary methods
'''
1 . get() -> returns the value for key is in the dictionary else default
2 . items() -> a set like object providing a view on D's item
3 . keys() -> a set like object providing a view of D's keys
4 . values() -> an object providing a view of d's values
'''
print(player.get(18))  # Virat

for key, value in player.items():
    print(key,":",value)

'''

45 : Rohit
77 : XYZ
18 : Virat
1 : KL Rahul
next to bat : {96: 'Shreyash', 63: 'SKY', 8: 'Jaddu'}
'''

print(player.keys())             # dict_keys([45, 77, 18, 1, 'next to bat'])

print(player.values())          #   dict_values(['Rohit', 'XYZ', 'Virat', 'KL Rahul', {96: 'Shreyash', 63: 'SKY', 8: 'Jaddu'}])

# Deleting elements from the dictionary
'''
1 . pop()
2 . popitem()
3 . clear()
'''

print(player.popitem())
print(player)

'''
removes the last item and return it as a tuple of key value pair

('next to bat', {96: 'Shreyash', 63: 'SKY', 8: 'Jaddu'})
{45: 'Rohit', 77: 'XYZ', 18: 'Virat', 1: 'KL Rahul'}
'''

print(player.pop(77))
print(player)

'''
pop removes and return the value

XYZ
{45: 'Rohit', 18: 'Virat', 1: 'KL Rahul'}
'''

player.clear()
print(player)
'''
Delete all items from list
{}
'''

player = {45:'Rohit',77:'Shubman',18:'Virat',1:'Kl Rahul',96:'Shreyash',8:'Jaddu'}
print(player)
newData = player.copy()
print(player)
print(newData)
'''
{45: 'Rohit', 77: 'Shubman', 18: 'Virat', 1: 'Kl Rahul', 96: 'Shreyash', 8: 'Jaddu'}
{45: 'Rohit', 77: 'Shubman', 18: 'Virat', 1: 'Kl Rahul', 96: 'Shreyash', 8: 'Jaddu'}
{45: 'Rohit', 77: 'Shubman', 18: 'Virat', 1: 'Kl Rahul', 96: 'Shreyash', 8: 'Jaddu'}
'''
newDict = {63:"SKY",33:'Hardik'}
player.update(newDict)
print(player)
'''
{45: 'Rohit', 77: 'Shubman', 18: 'Virat', 1: 'Kl Rahul', 96: 'Shreyash', 8: 'Jaddu', 63: 'SKY', 33: 'Hardik'}
'''

# setdefault()
'''
insert key value of default if key is not in the dict
return the value for key if key is in the dict else default
'''

val1 = player.setdefault(18,"Kohli")
print(player)
print(val1)         #Virat

val2 = player.setdefault(19,'Kohli')
print(player)
print(val2)

'''
{45: 'Rohit', 77: 'Shubman', 18: 'Virat', 1: 'Kl Rahul', 96: 'Shreyash', 8: 'Jaddu', 63: 'SKY', 33: 'Hardik', 19: 'Kohli'}
Kohli
'''

#formkeys()

lang = {'Reactjs','Flutter','SpringBoot'}
teacher='Shashi sir'
print(type(lang))
print(lang)
print(player.fromkeys(lang,teacher))

'''
<class 'set'>
{'SpringBoot', 'Flutter', 'Reactjs'}
{'SpringBoot': 'Shashi sir', 'Flutter': 'Shashi sir', 'Reactjs': 'Shashi sir'}
'''
