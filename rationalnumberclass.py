from math import gcd

class RationalNum:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("Denominator Cannot Be Zero")
        
        elif denominator < 0:
            numerator, denominator = -numerator, -denominator
            
            
        hcf = gcd(numerator, denominator)
            
        self.numerator = numerator // hcf
        self.denominator = denominator // hcf
            
    def __str__(self):
        return f"{self.numerator} / {self.denominator}"
    
    def __repr__(self):
        return f"Rational Number(Numerator: {self.numerator}, Denominator: {self.denominator})"
