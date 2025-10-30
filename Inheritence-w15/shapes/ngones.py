from math import tan, pi
from polygon import Polygon

class RegularNGone(Polygon):
    def __init__(self, length_side: int | float, no_of_sides: int | float):
        self.side = length_side
        self.n = no_of_sides
        
    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, length):
        
        self._side = self._validate_side(length)
        
    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, n_sides):
        
        self._n = self._validate_side(n_sides)
        
    def perimeter(self) -> int | float:
        return self.side * self.n
    
    def area(self) -> int | float:
        return (self.side / (2 * tan(pi / self.n))) * self.perimeter() * 0.5
                #1/2 * apothem * perimeter
    
    def __str__(self):
        return f"Lenght of Side: {self.side}, No. of Sides: {self.n}"
    def __repr__(self):
        return f"Polygon(side={self.side}, n={self.n})"
    
class Pentagon(RegularNGone):
    def __init__(self, side):
        super().__init__(side, 5)
        
    def __str__(self):
        return f"Side: {self.side}"
    def __repr__(self):
        return f"Pentagon(side={self.side})"
    
class Hexagon(RegularNGone):
    def __init__(self, side):
        super().__init__(side, 6)
        
    def __str__(self):
        return f"Side: {self.side}"
    def __repr__(self):
        return f"Hexagon(side={self.side})"
    
class Octagon(RegularNGone):
    def __init__(self, side):
        super().__init__(side, 8)
        
    def __str__(self):
        return f"Side: {self.side}"
    def __repr__(self):
        return f"Octagon(side={self.side})"