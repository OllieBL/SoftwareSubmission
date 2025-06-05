from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def volume(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
    def volume(self):
        return (4/3) * pi * self.radius ** 3
    
class Rectangle(Shape):
    def __init__(self, width, height, length):
        self.width = width
        self.height = height
        self.length = length

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.width)
    
    def volume(self):
        return self.width * self.length * self.height
    
class Square(Rectangle):
    def __init__(self, height):
        super().__init__(height, height, height)
    
    def area(self):
        return super().area()
    
    def perimeter(self):
        return super().perimeter()
    
    def volume(self):
        return super().volume()