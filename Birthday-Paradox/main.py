from Birthday_Paradox import BirthdayParadox

try:
    x = BirthdayParadox(25)
    print(x)
    print(repr(x))
    x.test()
    
    
except TypeError as e:
    print("Error:", e)
except ValueError as e:
    print("Error:", e)
except Exception:
    print("An Error Occured")