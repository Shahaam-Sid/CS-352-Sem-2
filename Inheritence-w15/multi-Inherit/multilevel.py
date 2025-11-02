# Multi Level Inheritence

class LevelOne:
    def __init__(self):
        self.console = "Level 1"
        
    def check_level(self):
        print('Level One Activated')
        
    def level_alpha(self):
        print('this is LEVEL 1')
        
class LevelTwo(LevelOne):
    def __init__(self):
        super().__init__()
        
    def check_level(self):
        print('Level Two Activated')
        
class LevelThree(LevelTwo):
    def __init__(self):
        super().__init__()
        self.console = "Level 3"
        
class LevelFour(LevelThree):
    def __init__(self):
        super().__init__()
        
        
for i in [LevelOne(), LevelTwo(), LevelThree(), LevelFour()]:
    print(f"===={i.console}====")
    i.check_level()
    i.level_alpha()
    print('\n\n')
    
    
"""
Output:
________________________
====Level 1====
Level One Activated
this is LEVEL 1



====Level 1====
Level Two Activated
this is LEVEL 1



====Level 3====
Level Two Activated
this is LEVEL 1



====Level 3====
Level Two Activated
this is LEVEL 1
"""