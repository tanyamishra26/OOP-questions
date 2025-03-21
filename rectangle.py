# Find the area of a rectangle.
# Approach:
# The class name should be Rectangle.
# The constructor should accept two parameters length and height but you can't pass the values directly to it while creating the constructor. E.g., rectangle = Rectangle(length=10, height=8) <-- you can't do that while creating the instances.
# Create a method called area() which has no parameters.
# Create a method called is_square() which also has no parameters. Return True if the rectangle is a square otherwise return False.
# If you are using a if-else block inside the is_square() method, then use the one-linear syntax.

class Rectangle:
    def __init__(self):
        self.length=float(input("enter the length"))
        self.height=float(input("enter the height"))
    def area(self):
        return self.length*self.height
    def is_square(self):
        return True if self.length==self.height else False
    
 # Create a rectangle object
rectangle = Rectangle()

# Get the area of the rectangle
print(f"Area of the rectangle: {rectangle.area()}")

# Check if the rectangle is a square
print(f"Is the rectangle a square? {rectangle.is_square()}")       

