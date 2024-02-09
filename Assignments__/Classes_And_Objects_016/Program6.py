'''
WAP
 fot following MRO with flow diagram
'''

class A:
    pass
class C(A):
    pass
class B(C):
    pass
class D(B):
    pass
class E(D):
    pass 

print(E.__mro__)
