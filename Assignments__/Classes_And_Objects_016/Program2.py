'''
Create a Vehicle class with variable brand,model,year,speed and methods
accelerate, brake, honk, Create the child class of vehicle class which 
overrides the acceerate and honk method Create the Vehicle class object 
and pass the attribute to the obj same create the child class object 
and pass the same attributr to the chile classs object
'''

class Vehicle:
    
    def __init(self,brand,model,speed):
        self.brand = brand
        self.model = model
        self.speed = speed
    
    def accelaratr(self):
        print('accelates at 1000rpm')
    
    def brake(self):
        print('from 100 to 0 in 3 sec')
    
    def honk(self):
        print('121 dB')

class Child(Vehicle):
    
    def __init(self,brand,model,speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelarate(self):
        print("1206 rotation per sec")
    
    def honk(self):
        print("67 dB")

brand = input("Enter the brand of the vehicle you own")
model = input('Model no')
speed = int(input("Top speed"))

obj = Child()
obj.accelarate()
obj.honk()
obj.brake()
