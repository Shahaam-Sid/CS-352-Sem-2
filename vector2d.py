class vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"(x, y) = ({self.x}, {self.y})"
    
    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other):
        return f"(x, y) = ({self.x + other.x}, {self.y + other.y})"
        
    def __sub__(self, other):
        return f"(x, y) = ({self.x - other.x}, {self.y - other.y})"
    
    def __mul__(self, scalar):
        return f"(x, y) = ({self.x * scalar}, {self.y * scalar})"
    
    def __abs__(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def __getitem__(self, index):
        if index == 0:
            return self.x
        else:
            return self.y
        
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, newValue):
        self._x = newValue
        
        
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, newValue):
        self._y = newValue