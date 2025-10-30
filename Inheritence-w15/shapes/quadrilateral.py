from abc import ABC, abstractmethod
from polygon import Polygon

class Quadrilateral(Polygon):
    def __init__(self, side: int | float):
        self.side = side
        
    @property
    def side(self):
        return self._side
    
    @side.setter
    def side(self, lenght):
        
        self._side = self._validate_side(lenght)
        
    def area(self):
        pass
    
    def perimeter(self):
        pass
        
    
class Square(Quadrilateral):
    def __init__(self, side: int | float):
        super().__init__(side)
        
    def area(self) -> int | float:
        return self.side ** 2
    
    def perimeter(self) -> int | float:
        return self.side * 4
    
    def __str__(self):
        return f'Sides: {self.side}'
    def __repr__(self):
        return f'Square(side={self.side})'
    
class Rectangle(Quadrilateral):
    def __init__(self, side: int | float, side_2: int | float):
        super().__init__(side)
        self.side_2 = side_2
        
    @property
    def side_2(self):
        return self._side_2
    
    @side_2.setter
    def side_2(self, length):
        
        self._side_2 = self._validate_side(length)
        
    def area(self) -> int | float:
        return self.side * self.side_2
    
    def perimeter(self) -> int | float:
        return (self.side + self.side_2) * 2
    
    def __str__(self):
        return f'Side 1: {self.side}, Side 2: {self.side_2}'
    def __repr__(self):
        return f'Square(side={self.side}, side_2={self.side_2})'