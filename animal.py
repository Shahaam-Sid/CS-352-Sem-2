class Bieng:
    
    count = 0
    
    def __init__(self, name, isPassive, naturalHabitat):
        self.name = name
        self.isPassive = isPassive
        self.naturalHabitat = naturalHabitat
        Bieng.count += 1
        
    @classmethod
    def getcount(cls):
        return f"Number of Beings: {cls.count}"
  
  
    
class LandAnimal(Bieng):
    def __init__(self, name, isPassive, naturalHabitat, doesWalk):
        super().__init__(name, isPassive, naturalHabitat)
        self.doesWalk = doesWalk
        
    def showDetails(self):
        print(f"""
Name: {self.name}
Human Friendly: {self.isPassive}
Habitat: {self.naturalHabitat}
Does it walk: {self.doesWalk}""")


        
class Bird(Bieng):
    def __init__(self, name, isPassive, naturalHabitat, doesFly):
        super().__init__(name, isPassive, naturalHabitat)
        self.doesFly = doesFly
        
    def showDetails(self):
        print(f"""
Name: {self.name}
Human Friendly: {self.isPassive}
Habitat: {self.naturalHabitat}
Does it Fly: {self.doesFly}""")
 
 
        
class Fish(Bieng):
    def __init__(self, name, isPassive, naturalHabitat, haveGills):
        super().__init__(name, isPassive, naturalHabitat)
        self.haveGills =haveGills
        
    def showDetails(self):
        print(f"""
Name: {self.name}
Human Friendly: {self.isPassive}
Habitat: {self.naturalHabitat}
Does it have Gills: {self.haveGills}""")
        
        
Tiger = LandAnimal("Tiger", False, "Forest", True)
Panda = LandAnimal("Panda", True, "Bamboo Forest", True)
Eagle = Bird("Eagle", False, "Multiple Habitats", True)
Penguin = Bird("Penguin", True, "Southern Hemisphere", False)
Dolphin = Fish("Dolphin", True, "Oceans", False)

print(Bieng.getcount())

Tiger.showDetails()
Panda.showDetails()
Eagle.showDetails()
Penguin.showDetails()
Dolphin.showDetails()

