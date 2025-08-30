class Point:
    """
    A Class that creates Point object for a canvas
    x being the x-Coordinate
    y being the y-Coordinate
    """
    def __init__(self, x = 0, y = 0):
        """
        Inputs x and y Coordinates
        Also contains copy-constructer functionality
        
        Args:
            x (int or float): Default =  0.
            y (int or float): Default =  0.
        """
        
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
        """
        Calculates the Distance b/w  two Points

        Args:
            other (Point)

        Raises:
            TypeError: if other is other then Point Object raises error

        Returns:
            Point Onject
        """
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