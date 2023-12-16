class Employee:
    def __init__(self,empId,empName):
        self.empId = empId
        self.empName = empName
    def empInfo(self):
        print(self.empId)
        print(self.empName)

emp1 = Employee(12,'Kanhha')
emp2 = Employee(15,'Rahul')

emp1.empInfo()
emp2.empInfo()

'''
12
Kanhha
15
Rahul
'''
