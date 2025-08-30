class Point:
    def __init__(self, x = 0, y = 0):
        
        if isinstance(x, Point):
            self._x = x._x
            self._y = x._y
            
        else:
            self.x = x
            self.y = y
            
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @x.setter
    def x(self, value):
        if not isinstance(value, (int,float)):
            raise TypeError("x must be a Integer or Decimal")
        
        self._x = value
        
    @y.setter
    def y(self, value):
        if not isinstance(value, (int,float)):
            raise TypeError("y must be a Integer or Decimal")
        
        self._y = value
        
    def distance(self, other):
        if not isinstance(other, Point):
            raise TypeError("Both inputs must be a Point")
        
        lenght = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        
        return f"Distance b/w {self} and {other} is {lenght}"
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
            
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        return f"Point: (x, y) = ({self.x}, {self.y})"

p1 = Point(3, 4)
p2 = Point(0, 0)
# Distance between two points
print(p1.distance(p2))  # 5.0  (classic 3-4-5 triangle)