#A program to calculate Need-Base and Merit Scholarship

class Scholarship:
    def __init__(self, name, netIncome, gpa):
        self.name = name
        self.netIncome = netIncome
        self.gpa = gpa
        self._meritPercent = 0.0
        self._needPercent = 0.0
    
    def __str__(self):
        return f"""Name = {self.name}
GPA = {self.gpa}
Scholarship(Total) = {self.totalPercent}"""
    
    @property
    def meritPercent(self):
        return f"{self._meritPercent * 100}"
    
    @property
    def needPercent(self):
        return f"{self._needPercent * 100}"
    
    @meritPercent.setter
    def meritPercent(self, newmp):
        if self.gpa >= 3.5:
            self._meritPercent = newmp
        elif self.gpa >= 3.0 and self.gpa < 3.5:
            self._meritPercent = newmp * 0.5
        else:
            self._meritPercent = newmp * 0
            
    @needPercent.setter
    def needPercent(self, newnp):
        if self.netIncome < 100000:
            self._needPercent = newnp
        elif self.netIncome >= 100000 and self.netIncome < 200000:
            self._needPercent = newnp * 0.5
        else:
            self._needPercent = newnp * 0.0
            
    @property
    def totalPercent(self):
        tpercentage = self._meritPercent + self._needPercent
        if tpercentage > 1:
            tpercentage = 1
        return round(tpercentage * 100, 2)
            
            
case1 = Scholarship("Daniyal", 90000, 3.7)
case2 = Scholarship("Basim", 125000, 3.3)
case3 = Scholarship("Mujtaba", 400000, 2.7)

percentage = 1

case1.needPercent = percentage
case1.meritPercent = percentage
case2.needPercent = percentage
case2.meritPercent = percentage
case3.needPercent = percentage
case3.meritPercent = percentage


print()
print(case1)
print()
print(case2)
print()
print(case3)