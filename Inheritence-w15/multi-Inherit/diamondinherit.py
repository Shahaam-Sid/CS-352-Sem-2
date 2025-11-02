class Top:
    def __init__(self):
        self.location = "top"
        self.position = "Head"
        
    def explain(self):
        print('This is the top of Diamond')
        
class Left(Top):
    def __init__(self):
        super().__init__()
        self.location = "Left"
        
    def explain(self):
        print("This the Left Side")
        
class Right(Top):
    def __init__(self):
        super().__init__()
        self.location = "Right"
        
    def explain(self):
        print("This the Right Side")
        
class Bottom(Left, Right):
    def __init__(self):
        super().__init__()
        
x = Bottom()      
print(x.location)
print(x.position)
x.explain()

"""
Left
Head
This the Left Side
"""