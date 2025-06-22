import math

class Shape:
    """Base class representing a geometric shape"""
    
    def area(self):
        """Calculate area of the shape (to be overridden by subclasses)"""
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    """Derived class representing a rectangle"""
    
    def __init__(self, length, width):
        """Initialize rectangle dimensions"""
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate rectangle area (length × width)"""
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle"""
    
    def __init__(self, radius):
        """Initialize circle radius"""
        self.radius = radius
    
    def area(self):
        """Calculate circle area (π × radius²)"""
        return math.pi * (self.radius ** 2)
