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