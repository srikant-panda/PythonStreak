# Constructor is used to initialize the instance variables of a class. It is a special method that is called when an object of the class is created. The constructor method is defined using the __init__() method.

class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    
car1 = Car('mercedes','black') #Assign values to the instance variables using constructor automatically when the object is created.

print(car1.brand,car1.color)

"""
syntax:
class Classname:
        def __init__(self,parameter1,parameter2):
                self.property1 = parameter1 
                self.property2 = parameter2
___init___() creates constructor
self.property:
"""

'''
constructor types:

1. Default Costructor(self)
2. parameterized constructor (self,name)
3.constructor ith default value,(self,name='unknown')
'''