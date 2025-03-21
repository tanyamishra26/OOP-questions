# Write a program that has an abstract class Polygon. Derive two classes Rectangle and Triamgle from Polygon and write methods to get the details of their dimensions and hence calculate the area.

from abc import ABC, abstractmethod
class Polygon(ABC):
    @abstractmethod
    def get_dimensions(self):
        pass
    @abstractmethod
    def area(self):
        pass


class Rectangle(Polygon):
    def __init__(self):
        self.length=0
        self.breadth=0
    def get_dimensions(self):
        self.length=float(input("Enter the length of the rectangle: "))
        self.breadth=float(input("Enter the breadth of the rectangle: "))
    def area(self):
        return self.length*self.breadth
    

class Triangle(Polygon):
    def __init__(self):
        self.base=0
        self.height=0
    def get_dimensions(self):
        self.base=float(input("Enter the base of the rectangle: "))
        self.height=float(input("Enter the height of the rectangle: "))
    def area(self):
        return 0.5*self.base*self.height
    
print("RECTANGLE")
rect=Rectangle()
rect.get_dimensions()
print("Area of rectangle is:",rect.area())


print("TRIANGLE")
tri=Triangle()
tri.get_dimensions()
print("Area of triangle is:",tri.area())
