'''
Write the realtime example of Cricket that describes the inheritance
'''

class ICC:
    def rulesICC(self):
        print("11 players are must")

class BCCI(ICC):
    def rulesBCCI(self):
        print('no extra rules')

class IPL(BCCI):
    def rulesIPL(self):
        print("Impact Player")

class CPL(BCCI):
    def rulesCPL(self):
        print('power over added')

obj = CPL()
obj.rulesICC()
obj.rulesBCCI()
obj.rulesCPL()
