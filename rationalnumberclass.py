from math import gcd

class RationalNum:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("Denominator Cannot Be Zero")
        
        elif denominator < 0:
            numerator, denominator = -numerator, -denominator
            
        if numerator != 0:
            hcf = gcd(numerator, denominator)
                
            self.numerator = numerator // hcf
            self.denominator = denominator // hcf
        
        else:
            self.numerator, self.denominator = 0, 0
            
    def __str__(self):
        if self.numerator == 0:
            return f"{0}"
        elif self.denominator == 1:
            return f"{self.numerator}"
        else:
            return f"{self.numerator} / {self.denominator}"
    
    def __repr__(self):
        return f"Rational Number(Numerator: {self.numerator}, Denominator: {self.denominator})"

    def __add__(self, other):
        if self.numerator == 0:
            return other
        
        else:
            num = (self.numerator * other.denominator) + (other.numerator * self.denominator)
            den = self.denominator * other.denominator
            return RationalNum(num, den)
    
    def __sub__(self, other):
        if self.numerator == 0:
            return other
        else:
            num = (self.numerator * other.denominator) - (other.numerator * self.denominator)
            den = self.denominator * other.denominator
            return RationalNum(num, den)
    
    def __mul__(self, other):
        if self.numerator == 0:
            return f"{0}"
        
        else:
            num = self.numerator * other.numerator
            den = self.denominator * other.denominator
            return RationalNum(num, den)
        
    def __truediv__(self, other):
        if self.numerator == 0:
            return f"{0}"

        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return RationalNum(num, den)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator
    
    def __float__(self):
        if self.numerator == 0:
            return 0.0
        else:
            return float(self.numerator) / self.denominator