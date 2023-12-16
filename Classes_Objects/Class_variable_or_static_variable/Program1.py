class Company(object):
    compName = 'Facebook'
    def __init__(self):
        print('In Constructor')
        self.empId = 12
        self.empName = 'Kanha'

    def compInfo(self):
        print(self.empId)
        print(self.empName)
        print(self.compName)        # you have to call class variable either by class name or self
emp1 = Company()
emp1.compInfo()
