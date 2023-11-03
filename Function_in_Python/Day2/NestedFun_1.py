# Nested Function 

def outer():
    def inner():
        print("in inner fun")
    print("in outer fun")
    inner()
outer()

#outer().inner()
# attributeErro : NoneType 
