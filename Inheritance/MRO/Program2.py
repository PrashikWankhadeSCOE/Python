class A:
    def fun(self):
        print('A')

class B:
    def fun(self):
        print('B')

class C :
    def fun(self):
        print('C')

class D(A,B):
    def fun(self):
        print('D')
        super().fun()
class E(B,C):
    def fun(self):
        print('E')
        super().fun()

class F(D,E):
    def fun(self):
        print('F')
        super().fun()

obj = F()
obj.fun();

print(F.mro())
