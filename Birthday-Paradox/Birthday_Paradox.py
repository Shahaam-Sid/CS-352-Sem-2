import random


class BirthdayParadox:
    """
    A class to simulate and verify the Birthday Paradox for a given sample size.
    """
    def __init__(self, n):
        """
        _n (int): Number of people in the group.
        sample_list: A list of randomly generated birthdays,
        where each birthday is represented as [day, month].
        """
        if not isinstance(n, int):
            raise TypeError("Input must be an Integer")
        if n <= 0:
            raise ValueError("Number of People must be more 0")
        
        self._n = n
        self.sample_list = []
        
        for _ in range(0, self._n):
            
            mm = random.randint(1, 12)
            #mm stands for Birth Month
            ##dd stands for Birth Date
            if mm == 2:
                #in Feb(2nd month) 29 days are maximum
                dd = random.randint(1, 29)
            elif mm in [4, 6, 9, 11]:
                #in April, June, September, November(4, 6, 9 and 11 month)
                #30 days are maximum
                dd = random.randint(1, 30)
            else:
                #in other months 31 days are maximum
                dd = random.randint(1, 31)
                
            self.sample = [dd, mm] #creates a new date [date, month]
            self.sample_list.append(self.sample) #appends it to sample dates
        
        
    
    def check_paradox(self):
        """
        Checks if at least two people in the group share the same birthday.
        Returns True if a match is found, otherwise False.
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
    A class to run multiple simulations of the Birthday Paradox
    for different sample sizes (number of people).

    This class uses the `BirthdayParadox` class to generate random
    birthday samples and check whether at least two people share
    the same birthday.
    """
    def __init__(self, sample_lengths):
        """
        _sample_lengths (list[int]): A list of integers where each integer
        represents the number of people in a group for which the paradox
        will be tested.
        """
        if not isinstance(sample_lengths, list):
            raise TypeError("Sample Lenghts must be a List")
            
        if any(not isinstance(x, int) for x in sample_lengths):
            raise TypeError("Sample Lenghts List must only contain Integer Values")
            
        self._sample_lengths = sample_lengths
        #list of integers, each integer is the number
        #of people for which paradox will be tested
            
    def sampling_birthday_paradox(self):
        """
        Runs simulations (2000 trials per sample size) and estimates
        the probability that at least two people in the group share
        the same birthday. Prints results for each sample size.
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