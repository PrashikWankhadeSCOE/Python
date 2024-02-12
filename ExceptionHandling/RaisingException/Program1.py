def voting(name,age):
    if(age<18):
        raise ValueError('Not Eligible for voting')
    else:
        print('Thanks for voting')

print('Start Code')

name = input('Enter the name')
try:
    age = int(input('Enter the age'))

except ValueError :
    print('Proper integer value addd kara')

try:
    voting(name,age)
except ValueError:
    print('Value Error sapadla')
except NameError:
    print("if entered age is not num then age wont be initialized so age will throgh name error which is handeled here")
print('End Code')
