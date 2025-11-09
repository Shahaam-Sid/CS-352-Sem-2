class SquareUnderN:
    def __init__(self, n: int = 0):
        self.n = n

    @property
    def n(self):
        return self._n 
    @n.setter
    def n(self, value):
        if not isinstance(value, int):
            raise TypeError('Value must be an Integer')
        if value < 0:
            raise ValueError('Value must be positive')
        
        self._n = value

    def produce(self) -> list:
        return sum([x ** 2 for x in range(self.n)])
    
obj = SquareUnderN(4)
print(obj.produce())