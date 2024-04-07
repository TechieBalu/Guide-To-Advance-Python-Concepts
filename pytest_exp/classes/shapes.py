import math

class Shape:
    def area(self):
        raise NotImplementedError("This method should be overridden by subclasses.")
    
    def perimeter(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius