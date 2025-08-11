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

    def __add__(self, other):
        num = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        den = self.denominator * other.denominator
        return RationalNum(num, den)
    
    def __sub__(self, other):
        num = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        den = self.denominator * other.denominator
        return RationalNum(num, den)
    
    def __mul__(self, other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return RationalNum(num, den)
    
    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError("Denominator Cannot Be Zero")

        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return RationalNum(num, den)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator
    
    def __float__(self):
        return float(self.numerator) / self.denominator