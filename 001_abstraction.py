from abc import ABC, abstractmethod

class Shape(ABC):
    '''
    In Python's Object-Oriented Programming (OOP), an abstract class is a class that cannot be instantiated directly. 
    It serves as a blueprint for other classes, defining a set of methods that must be implemented by its subclasses. 
    Abstract classes are created using the abc (Abstract Base Classes) module in Python.

    To create an abstract class, you need to inherit from the ABC (Abstract Base Class) metaclass and use the 
    @abstractmethod decorator to mark the abstract methods that need to be implemented in the subclasses.
    '''
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

def main():
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    print("Circle Area:", circle.area())             # Output: Circle Area: 78.5
    print("Circle Perimeter:", circle.perimeter())   # Output: Circle Perimeter: 31.400000000000002
    print("Rectangle Area:", rectangle.area())       # Output: Rectangle Area: 24
    print("Rectangle Perimeter:", rectangle.perimeter()) # Output: Rectangle Perimeter: 20

if __name__ == "__main__":
    main()


# In this example, the Shape class is an abstract class with two abstract methods area() and perimeter(). 
# The Circle and Rectangle classes inherit from the Shape class and provide their own implementations for the abstract methods.

# Attempting to create an instance of the Shape class directly would result in an error because abstract classes cannot be instantiated. 
# The main purpose of the abstract class is to define a common interface and enforce that subclasses must implement certain methods.








