class Triangles:
    _count = 0
    
    def __init__(self, *args):
        if len(args) == 0:
            self.sideA = self.sideB = self.sideC = 1.0
        elif len(args) == 1 and isinstance(args[0], (int, float)):
            self.sideA = self.sideB = self.sideC = float(args[0])
        elif len(args) == 2:
            self.sideA = self.sideB = float(args[0])
            self.sideC = float(args[1])
        elif len(args) == 3:
            self.sideA = float(args[0])
            self.sideB = float(args[1])
            self.sideC = float(args[2])
        elif len(args) == 1 and isinstance(args[0], Triangles):
            other = args[0]
            self.sideA = other.sideA
            self.sideB = other.sideB
            self.sideC = other.sideC
        else:
            raise ValueError("Invalid Arguments")
        
        Triangles._count += 1
        
    @property
    def sideA(self):
        return self._sideA
    
    @property
    def sideB(self):
        return self._sideB
    
    @property
    def sideC(self):
        return self._sideC

    @sideA.setter
    def sideA(self, value):
        self._sideA = float(value)

    @sideB.setter
    def sideB(self, value):
        self._sideB = float(value)
        
    @sideC.setter
    def sideC(self, value):
        self._sideC = float(value)
        
    def perimeter(self):
        return self.sideA + self.sideB + self.sideC
    
    def isHypotenuse(self):
        sides = [self.sideA, self.sideB, self.sideC]
        sides.sort()
        if (sides[2] ** 2) == (sides[0] ** 2) + (sides[1] ** 2):
            return True
        else:
            return False

    def clone(self):
        return Triangles(self)
    
    def __str__(self):
        return f"""Triangle Side A = {self.sideA}
Triangle Side B = {self.sideB}
Trianlge Side C = {self.sideC}"""

    @classmethod
    def counter(cls):
        return cls._count