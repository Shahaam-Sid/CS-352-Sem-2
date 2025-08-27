from Birthday_Paradox import BirthdayParadox, SamplingBirthdayParadox

try:
    
    print("****** Birthday Paradox Testing ******")
    
    samples = [x * 5 for x in range(1, 21)]
    x = SamplingBirthdayParadox(samples)
    x.sampling_birthday_paradox()
        
        
    print("************ Program End *************")
    
except TypeError as e:
    print("Error:", e)
except ValueError as e:
    print("Error:", e)
except Exception:
    print("An Error Occured")