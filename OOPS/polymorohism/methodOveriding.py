
# Method Overriding is a feature in OOPs where a subclass provides a specific implementation of a method that is already defined in its superclass. The method in the subclass should have the same name, return type, and parameters as the method in the superclass. This allows the subclass to provide its own behavior while still maintaining the same interface as the superclass.


class Animal:
    def catagory(self):
        print('This is a Animal!')
    
class Parrot(Animal):
    def catagory(self):
        print('Parrot ok!')
class Cow(Animal):
    def catagory(self):
        print('This is a Cow!')
        return super().catagory()

cow1 = Cow()
cow1.catagory()