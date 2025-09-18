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
    
    
    
    
a = vector2d(7.7, 8.0)
b = vector2d(-1.0, 2.0)
o = vector2d(0.0, 0.0)

    
    
print(f"Vector Coordinates for A: {a}")
print(f"Vector Coordinates for B: {b}")
print(f"Vector Coordinates for C: {o}")

print()

print(f"vector2d objects: ")
print(repr(a))
print(repr(b))
print(repr(o))

print()

print(f"Are A and O equal: {a == o}")

print()

print(f"A + B: {a + b}")
print(f"A - B: {a - b}")

print()

print(f"Multiply B by 2.5: {b * 2.5}")

print()

print(f"Magnitude of B: {abs(b)}")

print()

print(f"x coordinate of A: {a[0]}")
print(f"y coordinate of A: {a[1]}")