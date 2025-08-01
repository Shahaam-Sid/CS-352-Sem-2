from abc import ABC, abstractmethod

class CuddlyToy(ABC):
    def __init__(self, size):
        self.size = size
    
    @property
    def size(self):
        return self._size
        
    @size.setter
    def size(self, x):
        self._size = x
        
    @abstractmethod
    def speak(self):
        pass
    
    
class TeddyBears(CuddlyToy):
    def __init__(self, size):
        super().__init__(size)
    
    def speak(self):
        return f"Grrrrrrowling.........."
    
class BunnyRabbits(CuddlyToy):
    def __init__(self, size):
        super().__init__(size)
        
    def speak(self):
        return f"Squeeeeaaak......"
    

class EngineDrivers(TeddyBears):
    def __init__(self, size):
        super().__init__(size)
        self.color = "Blue"
        self.job = "Engine Driver"
    
    def __str__(self):
        return f"I am a {self.size} sized, {self.color} Teddy Bear and I am a {self.job}"
        
class Gardeners(TeddyBears):
    def __init__(self, size):
        super().__init__(size)
        self.color = "Red"
        self.job = "Gardener"
        
    def __str__(self):
        return f"I am a {self.size} sized, {self.color} Teddy Bear and I am a {self.job}"
        
class Clowns(BunnyRabbits):
    def __init__(self, size):
        super().__init__(size)
        self.color = "White"
        self.job = "Clown"
        
    def __str__(self):
        return f"I am a {self.size} sized, {self.color} Bunny Rabbit and I am a {self.job}"
        
class BankManagers(BunnyRabbits):
    def __init__(self, size):
        super().__init__(size)
        self.color = "Black"
        self.job = "Bank Manager"
        
    def __str__(self):
        return f"I am a {self.size} sized, {self.color} Bunny Rabbit and I am a {self.job}"