from abc import ABC, abstractmethod

# 1. Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# 2. Concrete Class: Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Implementing the abstract method specifically for Rectangle
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# 3. Concrete Class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Implementing the abstract method specifically for Circle
    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# --- Usage ---
shapes = [Rectangle(10, 5), Circle(7)]

for s in shapes:
    # We don't care IF it is a circle or rectangle.
    # We just know it is a Shape, so it MUST have an area.
    print(f"Area: {s.area()}")