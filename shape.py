class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def describe(self):
        print(f"This a {self.name} of {self.color} color")
        
        
shape1 = Shape("Square", "Red")
shape2 = Shape("Triangle", "Violet")
shape3 = Shape("Hexagon", "Green")
shape4 = Shape("Rectangle", "Blue")
shape5 = Shape("Circle", "Orange")

shapes = [shape1, shape2, shape3, shape4, shape5]

for shape in shapes:
    shape.describe()