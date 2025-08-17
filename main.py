from rationalnumberclass import RationalNum

try:
    a = RationalNum(0, 5)
    b = RationalNum(3, 7)
    
    
    print(f"A = {a}")
    
    print(f"B = {b}")
    
    print(f"A + B = {a + b}")
    
    print(f"A - B = {a - b}")
    
    print(f"Is A = B : {a == b}")
    
    print(f"A x B = {a * b}")
    
    print(f"A / B = {a/b}")
    
    print(f"Decimal Value of A = {float(a)}")
    
    print(f"Decimal Value of B = {float(b)}")
    
except ZeroDivisionError:
    print("Cannot Divide by Zero")
except Exception:
    print("An error occured")