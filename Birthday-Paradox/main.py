from Birthday_Paradox import BirthdayParadox

try:
    
    print("****** Birthday Paradox Testing ******")
    
    samples = [x * 5 for x in range(1, 21)] #simulates n = 5, 10, 15, ..., 100
    for sample in samples:
        
        case_true = 0
        case_false = 0
        for _ in range(1, 2000):
            #more the sampling more accurate probability, but slower
            paradox = BirthdayParadox(sample + 23)
            if paradox.check_paradox():
                case_true += 1
            else:
                case_false += 1
     
        probability = (case_true) / (case_true + case_false)
        print("**************************************")
        print(f"Probability for {sample + 23} pupil is {probability:.3f}")
        if probability > 0.5:
            print("Birthday Paradox is True")
        else:
            print("Birthday Paradox is False")
        print("**************************************")
        print()
        
        
    print("************ Program End *************")
    
except TypeError as e:
    print("Error:", e)
except ValueError as e:
    print("Error:", e)
except Exception:
    print("An Error Occured")