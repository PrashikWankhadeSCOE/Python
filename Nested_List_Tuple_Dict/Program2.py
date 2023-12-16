lang = ()
print(type(lang))  #<class 'tuple'>

lang = ('Cpp','Java','Python','Js','Dart',10.5,20,30,40)
print(lang)
print(type(lang))

'''
('Cpp', 'Java', 'Python', 'Js', 'Dart', 10.5, 20, 30, 40)
<class 'tuple'>
'''

# lang[3] = 'Go'        TypeError: 'tuple' object does not support item assignment
print(lang)

# Tuple methods 
'''
1 . count -> returns the no of occurance of the element
2 . index -> returns the first index of the occurance of the element
'''


lang = ('CPP','Java','Js','Dart','Java')
print(lang.count('Java'))
print(lang.index('Java'))

'''
2
1
'''

