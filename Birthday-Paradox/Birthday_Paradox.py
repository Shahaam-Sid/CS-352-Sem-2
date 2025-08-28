import random


class BirthdayParadox:
    """
        A Class to verify Birthday Paradox
        n is the Number of people in test sample
        """
    def __init__(self, n):
        if not isinstance(n, int):
            raise TypeError("Input must be an Integer")
        if n <= 0:
            raise ValueError("Number of People must be more 0")
        
        self._n = n
        self.sample_list = []
        
        for _ in range(0, self._n):
            
            
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
        """
        Check for same dates in samples
        returns True if same dates found
        returns False if same dates not found
        """
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
    """
    This class takes Sample Lenghts, so the Paradox could be tested on them
    sample_lengths must be a list, containing only integer values
    """
    def __init__(self, sample_lengths):
        if not isinstance(sample_lengths, list):
            raise TypeError("Sample Lenghts must be a List")
            
        if any(not isinstance(x, int) for x in sample_lengths):
            raise TypeError("Sample Lenghts List must only contain Integer Values")
            
        self._sample_lengths = sample_lengths
            
    def sampling_birthday_paradox(self):
        """
        runs and checks all the cases 2000 times
        returns probability of each case
        """
        for sample in self._sample_lengths:
            case_true = 0
            case_false = 0
            for _ in range(1, 2000):
                paradox = BirthdayParadox(sample) #Composition
                if paradox.check_paradox():
                    case_true += 1
                else:
                    case_false += 1
                    
            probability = (case_true) / (case_true + case_false)
            print("**************************************")
            print(f"Probability for {sample} pupil is {probability:.3f}")    

            if sample >= 23 and  probability >= 0.5:
                print("Birthday Paradox is True for this Sample")
            else:
                print("Birthday Paradox does not hold for this Sample")
            print("**************************************")
            print()
            
            
            
    def __str__(self):
        return f"Sample: {self._sample_lengths}"
    def __repr__(self):
        return f"sample_lenght({self._sample_lengths})"