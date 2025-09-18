class Laptop:
    def __init__(self, brand, series, model, gen, os):
        self.brand = brand
        self.series = series
        self.model = model
        self.gen = gen
        self.os = os
        
    def infoMake(self):
        return f"""
Company: {self.brand}
Model: {self.series} {self.model}"""

    def infoSpecs(self):
        return f"""
Specifications: {self.gen}, {self.os}"""        


laptops = []

for x in range(0, 5):
    brand = input("Enter Brand: ")
    series = input("Enter Series: ")
    model = input("Enter Model: ")
    gen = input("Enter Generation: ")
    os = input("Enter Operating System: ")
    
    laptops.append(Laptop(brand, series, model, gen, os))
    
for laptop in laptops:
    print(laptop.infoMake())
    print(laptop.infoSpecs())
    