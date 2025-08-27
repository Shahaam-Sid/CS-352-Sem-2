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
        """
        Check for same dates in samples
        returns True if same dates found
        returns False if same dates not found"""
        for i in range(0, self._n):
            for j in range(i + 1, self._n):
                if self.sample_list[i] == self.sample_list[j]:
                    return True
        
        return False
        

    def __str__(self):
        return f"Birthday Paradox test for a sample of {self._n} pupils: {self.sample_list}"
    def __repr__(self):
        return f"Birthday Paradox(n = {self._n}, sample_list = {self.sample_list})"