from polygon import Polygon

class Triangle(Polygon):
    def __init__(self, base: int | float, height: int | float):
        
        self.height = height
        self.base = base
        
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, length):
        
        self._height = self._validate_side(length)
        
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, length):
        
        self._base = self._validate_side(length)
        
    def area(self) -> int | float:
        return self.base * self.height * 0.5
    
    def perimeter(self):
        pass
    
    
class IsoscelesTriangle(Triangle):
    def __init__(self, base, height):
        super().__init__(base, height)
        
    def perimeter(self) -> int | float:
        hyp = (((self.base / 2) ** 2) + (self.height ** 2)) ** 0.5
        return (2 * hyp) + self.base
    
    def __str__(self):
        return f"Base: {self.base}, Hieght: {self.height}"
    def __repr__(self):
        return f"IsoscelesTriangle(base={self.base}, height={self.height})"
    
class EquilateralTriangle(IsoscelesTriangle):
    def __init__(self, base, height):
        super().__init__(base, height)
        
    def perimeter(self) -> int | float:
        return self.base * 3
    
    def __str__(self):
        return f"Sides: {self.base}, Hieght: {self.height}"
    def __repr__(self):
        return f"IsoscelesTriangle(base={self.base}, height={self.height})"
        