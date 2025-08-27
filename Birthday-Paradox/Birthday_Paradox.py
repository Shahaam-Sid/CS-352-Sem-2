import re
from signal import raise_signal


class BirthdayParadox:
    def __init__(self, n):
        """
        A Class to verify Birthday Pardox
        n is the Number of people in test sample
        n must be more 23
        """
        if n <= 23:
            raise ValueError("Number of People must be more 23")
        
        self._n = n
        
    def __str__(self):
        return f"Birthday Paradox test for a sample of {self._n} pupils"
    def __repr__(self):
        return f"Birthday Paradox(n = {self._n})"