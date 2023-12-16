class Company():
    compName = 'FaceBook'
    def __init__(self):
        print('In constructor')
    def compInfo(self):
        print(self.compName)

emp1 = Company()
emp2 = Company()

emp1.compInfo()
emp2.compInfo()

Company.compName = 'Meta'

emp1.compInfo()

'''
It will change all the values in object variables 
because the orignal data is not sent 
reference is sent 
'''
