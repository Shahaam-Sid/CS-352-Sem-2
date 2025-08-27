from Birthday_Paradox import BirthdayParadox

try:

    

    
    samples = [x * 5 for x in range(1, 20)]
    for sample in samples:
        
        case_true = 0
        case_false = 0
        for _ in range(1, 100):
            paradox = BirthdayParadox(sample + 23)
            if paradox.check_paradox():
                case_true += 1
            else:
                case_false += 1
     
        probability = (case_true) / (case_true + case_false)
        print(f"Probability for {sample + 23} pupil is {probability}")
        if probability > 0.5:
            print("Birthday Paradox is Truee")
    
        
except TypeError as e:
    print("Error:", e)
except ValueError as e:
    print("Error:", e)
except Exception:
    print("An Error Occured")