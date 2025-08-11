from rationalnumberclass import RationalNum

try:
    a = RationalNum(12, 16)
    
    print(a)
    print()
    print(repr(a))
    
except ZeroDivisionError:
    print("Cannot Divide by Zero")
except Exception:
    print("An error occured")