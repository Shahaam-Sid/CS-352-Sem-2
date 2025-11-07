from abc import ABC, abstractmethod
import math
from point import Point

class ShapeInterface(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
    
    
    
    
    
    
    
class Polygon(ShapeInterface):
    """Abstract base for polygons built from Point-like (x, y) tuples."""
    
    def __init__(self, vertices):
        # Normalize tuples -> Points
        self.vertices = [v if isinstance(v, Point) else Point(*v) for v in vertices]
    
    @property
    def n(self):
        return len(self.vertices)
    
    @property
    def sides(self):
        """Compute side lengths using coordinate pairs."""
        if self.n < 2:
            return []
        return [math.hypot(
            self.vertices[(i + 1) % self.n].x - self.vertices[i].x,
            self.vertices[(i + 1) % self.n].y - self.vertices[i].y,
        ) for i in range(self.n)]
    
    def perimeter(self):
        return sum(self.sides)
    
    def __str__(self):
        return f"{self.__class__.__name__} with {self.n} sides"
    
    
    
    
    
    

class RegularPolygon(Polygon):
    """A regular polygon constructed by equal angular spacing around a center."""
    
    def __init__(self, n, radius, center=Point(0, 0), rotation=0):
        if n < 3:
            raise ValueError("A polygon must have at least 3 sides.")
        
        # do not assign to self.n directly bcoz in base class n is a property:
        self._num_sides = n
        self.radius = radius
        self.center = center if isinstance(center, Point) else Point(*center)
        self.rotation = math.radians(rotation)
        
        # Compute vertices like in 'ngon'
        self.vertices = self._compute_vertices()
        # Call the Polygon initializer
        super().__init__(self.vertices)
    
    def _compute_vertices(self):
        """Generate vertex coordinates using angle increments."""
        cx, cy = self.center.x, self.center.y
        vertices = []
        angle_inc = 2 * math.pi / self.n
        angle = self.rotation
        
        for _ in range(self.n):
            x = cx + self.radius * math.cos(angle)
            y = cy + self.radius * math.sin(angle)
            vertices.append(Point(x, y))
            angle += angle_inc
        return vertices
    
    # Inherit perimeter() from Polygon (already computes from vertices)
    def area(self):
        """Area formula for a regular polygon."""
        s = self.sides[0]
        n = self.n
        # or return 0.5 * self.n * self.radius**2 * math.sin(2 * math.pi / self.n)
        return (n * s ** 2) / (4 * math.tan(math.pi / n))