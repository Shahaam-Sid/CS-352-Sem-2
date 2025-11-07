import math
from point import Point
from shapeInterace import RegularPolygon
from irregular import IrregularPolygon

class Square(RegularPolygon):
    """A square is a regular polygon with 4 equal sides."""
    
    def __init__(self, center=Point(0, 0), side=1, rotation=45):
        # For a square, radius = side / sqrt(2)
        radius = side / math.sqrt(2)
        super().__init__(n=4, radius=radius, center=center, rotation=rotation)
        self.side = side  # optional: keep for convenience
    
    def area(self):
        return self.side ** 2  # override with simpler formula
    
    def __str__(self):
        return (
            f"Square(side={self.side:.2f}, area={self.area():.2f}, "
            f"perimeter={self.perimeter():.2f})"
        )


class Triangle(IrregularPolygon):
    """A triangle defined by 3 arbitrary points."""
    
    def __init__(self, vertices):
        if len(vertices) != 3:
            raise ValueError("A triangle must have exactly 3 vertices.")
        super().__init__(vertices)
        # Uses Shoelace area() and perimeter() from IrregularPolygon
    
    def __str__(self):
        return f"Triangle with area={self.area():.2f}, perimeter={self.perimeter():.2f}"