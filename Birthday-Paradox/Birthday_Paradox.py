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
        self.dd = 0
        self.mm = 0
        
        for i in range(0, self._n):
            
            self.sample = []
            self.dd = 0
            self.mm = 0
            
            self.mm = random.randint(1, 12)
            if self.mm == 2:
                self.dd = random.randint(1, 29)
            elif self.mm in [4, 6, 9, 11]:
                self.dd = random.randint(1, 30)
            else:
                self.dd = random.randint(1, 31)
                
            self.sample = [self.dd, self.mm]
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