class Parent:
    def __init__(self):

        print('In parent constructor')

        self.x = 10
        self.y = 20

    def dispParent(self):
        print(self.x)
        print(self.y)

class Child(Parent):
    def __init__(self):

        print('In child Coonstructor')

        self.x = 30
        self.y = 40

        super().__init__()

obj = Child()
obj.dispParent()

'''
In child Coonstructor
In parent constructor
10
20

'''
