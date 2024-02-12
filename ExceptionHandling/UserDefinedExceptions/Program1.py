class VotingError(Exception):
    def __init__(self,msg):
        super().__init__(msg)

def voting(name,age):
    if(age<18):
        raise VotingError('Not Eligible to vote')
    else:
        print('Thanks for voting')

print('Start Code')

name = input()
try :
    age = int(input())
except ValueError:
    print('Add integer data')
    age = int (input())
try:
    voting(name,age)
except VotingError as err:
    print(err)

print('End Code')
