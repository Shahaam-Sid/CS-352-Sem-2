from abc import ABC, abstractmethod
#Polymorphism
class Shape:
    
    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * (self.radius ** 2)
        
class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, widht, hieght):
        self.widht = widht
        self.hieght = hieght
        
    def area(self):
        return self.hieght * self.widht * 0.5
    
class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        self.radius = radius

    
shapes = [Circle(2), Square(2), Triangle(2, 2), Pizza("Paparoni", 2)]

for shape in shapes:
    print(f" Area is {shape.area()}")
