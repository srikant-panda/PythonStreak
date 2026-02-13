class Car:
    def set_details(self,brand,color):
        self.brand = brand
        self.color = color
    
    def show_details(self):
        print(f'This car is a {self.color} {self.brand}.')
    

car1 = Car()

car1.set_details('mercedes','black')

car1.show_details()