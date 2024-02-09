'''
Create a Class Human with instance attributes(including variables(naem,age)and method(information)), create the object of the class pass the name and the age attributes to the object and access the variable in the method information()
'''

class Human:
    def __init__(self,name,age):
        print('In human costructor')
        self.name = name
        self.age = age

    def information(self):
        print("Name is : ",self.name)
        print("age is : ",self.age)

name = input("Enter your name")
age = int(input("Enter your age"))


if __name__ == "__main__":
    obj1 = Human(name,age)
    obj1.information()


