import random


class BirthdayParadox:
    """
        A Class to verify Birthday Paradox
        n is the Number of people in test sample
        n must be more 23
        """
    def __init__(self, n):
        if not isinstance(n, int):
            raise TypeError("Input must be an Integer")
        if n <= 23:
            raise ValueError("Number of People must be more 23")
        
        self._n = n
        self.sample_list = []
        
        self.sample = []
        dd = 0
        mm = 0
        
        for i in range(0, self._n):
            
            self.sample = []
            dd = 0
            mm = 0
            
            mm = random.randint(1, 12)
            if mm == 2:
                dd = random.randint(1, 29)
            elif mm in [4, 6, 9, 11]:
                dd = random.randint(1, 30)
            else:
                dd = random.randint(1, 31)
                
            self.sample = [dd, mm]
            self.sample_list.append(self.sample)
        
        
    
    def check_paradox(self):
        counter = 0
        for i in range(0, self._n):
            for j in range(i + 1, self._n):
                if self.sample_list[i] == self.sample_list[j]:
                    return True
        
        return False
        

    def __str__(self):
        return f"Birthday Paradox test for a sample of {self._n} pupils: {self.sample_list}"
    def __repr__(self):
        return f"Birthday Paradox(n = {self._n}, sample_list = {self.sample_list})"
    
    
    
class SamplingBirthdayParadox:
    def __init__(self, sample_lenghts):
        if not isinstance(sample_lenghts, list):
            raise TypeError("Sample Lenghts must be a List")
            
        if any(not isinstance(x, int) for x in sample_lenghts):
            raise TypeError("Sample Lenghts List must only contain Integer Values")
            
        self._sample_lenghts = sample_lenghts
            
    def sampling_birthday_paradox(self):
        for sample in self._sample_lenghts:
            case_true = 0
            case_false = 0
            for _ in range(1, 2000):
                paradox = BirthdayParadox(sample + 23)
                if paradox.check_paradox():
                    case_true += 1
                else:
                    case_false += 1
                    
            probability = (case_true) / (case_true + case_false)
            print("**************************************")
            print(f"Probability for {sample + 23} pupil is {probability:.3f}")    

            if probability > 0.5:
                    print("Birthday Paradox is True for this Sample")
            else:
                print("Birthday Paradox is False for this Sample")
            print("**************************************")
            print()
            
            
            
    def __str__(self):
        return f"Sample: {self._sample_lenghts}"
    def __repr__(self):
        return f"sample_lenght({self._sample_lenghts})"