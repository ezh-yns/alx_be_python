import math

class Shape:
    def area(self):
        """Raise an error to ensure derived classes implement this method."""
        raise NotImplementedError("Derived classes must override the area() method.")


class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize a Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """Initialize a Circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
