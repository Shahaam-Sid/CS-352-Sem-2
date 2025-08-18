from rationalnumberclass import RationalNum

try:
    a = RationalNum(10, 3)
    b = RationalNum(7, 5)
    
    
    print(f"A = {a}")
    
    print(f"B = {b}")
    
    print(f"Decimal Value of A = {float(a):.3f}")
    
    print(f"Decimal Value of B = {float(b):.3f}")
    
    print(f"A + B = {a + b}")
    
    print(f"A - B = {a - b}")
    
    print(f"Is A = B : {a == b}")
    
    print(f"A x B = {a * b}")
    
    print(f"A / B = {a/b}")
    

except ZeroDivisionError:
    print("Cannot Divide by Zero")

except Exception:
    print("An error occured")