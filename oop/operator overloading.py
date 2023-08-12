import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius): 
        self.__radius = radius

    
    def area(self):

        return math.pi * self.__radius ** 2
    
    def __add__(self, circle_object): 
        return Circle(self.__radius, circle_object.__radius)
    

c1 = Circle(5)

c2 = Circle(4)

c3 = c1 + c2

print(c3)