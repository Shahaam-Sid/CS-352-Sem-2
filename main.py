from cuddlytoy import *

choice = ""

print(f"""Choose the following
    1 for Engine Driver Teddies
    2 for Gardener Teddies
    3 for CLown Bunnies
    4 for Bank Manager Bunnier""")

choice = input("Enter your Choice: ")
size = input("Enter Size(Small, Large, Medium): ")

match choice:
    case "1":
        x = EngineDrivers(size)
    case "2":
        x = Gardeners(size)
    case "3":
        x = Clowns(size)
    case "4":
        x = BankManagers(size)
        
print(x)
print(x.speak())
        
