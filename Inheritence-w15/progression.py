class Progression:
    
    def __init__(self, start: int = 0) -> None:
        self.start = start
        self._current = start
        
    @property
    def start(self):
        return self._start
    
    @start.setter
    def start(self, n):
        if not isinstance(n, int):
            raise TypeError('Start Value must be an Integer')
        
        self._start = n
        
    def progession(self, n: int) -> str:
        if not isinstance(n, int):
            raise TypeError('Term Number must be an Integer Value')
        iter(self)
        return ' '.join(str(next(self)) for _ in range(n))
        
    def sum(self, n: int) -> int:
        if not isinstance(n, int):
            raise TypeError('Term Number must be an Integer Value')
        sum = 0
        iter(self)
        for _ in range(n):
            sum += next(self)
            
        return sum
            
    def _advance(self):
        self._current += 1
        
    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            answer = self._current
            self._advance()
            return answer
        
    def __iter__(self):
        self._current = self._start
        return self
    
    def __str__(self):
        return f"Start: {self.start}"
    
    
    
    
class ArithmeticProgression(Progression):
    
    def __init__(self, start: int = 0, increment: int = 1) -> None:
        super().__init__(start)
        self.increment = increment
        
    @property
    def increment(self):
        return self._increment
    
    @increment.setter
    def increment(self, n):
        if not isinstance(n, int):
            raise TypeError('Increment Value must be an Integer')
        self._increment = n
        
    def _advance(self):
        self._current += self.increment
    
    def __str__(self):
        return f"Start: {self.start}, Increment: {self.increment}"
        
        
        
        
class GeometricProgression(Progression):
    def __init__(self, start: int = 1, base: int = 2) -> None:
        super().__init__(start)
        self.base = base
        
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, n):
        if not isinstance(n, int):
            raise TypeError('Base Value must be an Integer')
        self._base = n
    
    def _advance(self):
        self._current *= self.base
        
    def __str__(self):
        return f"Start: {self.start}, Base: {self.base}"
        
        
        

class FibonacciProgression(Progression):
    def __init__(self, first_value: int = 0, second_value: int = 1) -> None:
        super().__init__(first_value) #returns the value of first_value to the constructer of parent class
        self.second_value = second_value
        self._prev = self.second_value - first_value
        
    @property
    def first_value(self):
        return self.start    
    
    @first_value.setter
    def first_value(self, n):
        if not isinstance(n, int):
            raise TypeError('First Value must be an Integer')
        
        self.start = n
        
        
    @property
    def second_value(self):
        return self._second_value
    
    @second_value.setter
    def second_value(self, n):
        if not isinstance(n, int):
            raise TypeError('Second Value must be an Integer')
        if n <= self.first_value:
            raise ValueError('Second Value must be greater then First Value')
        
        self._second_value = n
        
    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current
    
    def __iter__(self):
        super().__iter__()
        self._prev = self.second_value - self.start
        return self