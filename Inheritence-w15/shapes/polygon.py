from abc import ABC, abstractmethod

class Polygon(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def _validate_side(self, length):
        if not isinstance(length, (int, float)):
            raise TypeError('length must be an Integer value')
        if length <= 0:
            raise ValueError('Length cannot be Zero or Negative')
        
        return length