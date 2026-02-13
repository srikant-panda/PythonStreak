class Animal:
    def speak(self):
        print('Animal make noise.')

class Dog(Animal):
    def barks(self):
        print('Dog Barks')

dog = Dog()
dog.barks()
dog.speak()