from rationalnumberclass import RationalNum

try:
    a = RationalNum(4, 2)
    b = RationalNum(5, 3)

    
    
    print(f"A = {a}")
    
    print(f"B = {b}")
    
    print(f"A + B = {a + b}")
    
    print(f"A - B = {a - b}")
    
    print(f"Is A = B : {a == b}")
    
    print(f"A x B = {a * b}")
    
    print(f"A / B = {a/b}")
    
except ZeroDivisionError:
    print("Cannot Divide by Zero")
except Exception:
    print("An error occured")