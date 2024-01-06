class Manager:
    def project(self):
        print('In Project : Manager')

class TL1:
    pass

class TL2:
    def project(self):
        print('In Project : TL2')

class Developer(TL1,TL2):
    pass

obj = Developer()
obj.project()
