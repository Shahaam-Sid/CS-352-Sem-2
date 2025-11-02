class SteamEngine:
    def __init__(self):
        self.fuel = 'Coal'
        
    def info(self):
        print('This Runs on Coal')
        
class DieselEngine:
    def __init__(self):
        self.fuel = 'Diesel'
        
    def info(self):
        print('This Runs on Diesel')
        
class ElectricEngine:
    def __init__(self):
        self.fuel = 'Electric'
        
    def info(self):
        print('This Runs on Electric')
        
class MultiEngine(SteamEngine, DieselEngine, ElectricEngine):
    def __init__(self):
        super().__init__()
        
        
print(MultiEngine.__mro__)
x = MultiEngine()
print(f"Fuel: ", x.fuel)
x.info()        

"""
Output:
===================

output (<class '__main__.MultiEngine'>, <class '__main__.SteamEngine'>, <class '__main__.DieselEngine'>, <class '__main__.ElectricEngine'>, <class 'object'>)
Fuel:  Coal
This Runs on Coal
"""


class MultiEngine(DieselEngine, ElectricEngine, SteamEngine):
    def __init__(self):
        super().__init__()
        
        
print(MultiEngine.__mro__)
x = MultiEngine()
print(f"Fuel: ", x.fuel)
x.info()        

"""
Output:
===================

(<class '__main__.MultiEngine'>, <class '__main__.DieselEngine'>, <class '__main__.ElectricEngine'>, <class '__main__.SteamEngine'>, <class 'object'>)
Fuel:  Diesel
This Runs on Diesel
"""

class MultiEngine(ElectricEngine, DieselEngine, SteamEngine):
    def __init__(self):
        super().__init__()
        
        
print(MultiEngine.__mro__)
x = MultiEngine()
print(f"Fuel: ", x.fuel)
x.info()        

"""
Output:
===================

(<class '__main__.MultiEngine'>, <class '__main__.ElectricEngine'>, <class '__main__.DieselEngine'>, <class '__main__.SteamEngine'>, <class 'object'>)
Fuel:  Electric
This Runs on Electric
"""