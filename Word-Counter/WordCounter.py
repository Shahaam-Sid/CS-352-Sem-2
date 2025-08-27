class WordCounter:
    """
    This Class takes a sentence as input
    Outputs how many times each word is used
    input must be string
    only letter must be used in string
    """
    def __init__(self, sentence):
        if not isinstance(sentence, str):
            raise TypeError("Enter a String in Constructer")
        if sentence.isspace() or sentence.isnumeric():
            raise ValueError("String must contain Words only")
        
        self._sentence = sentence
        list_words = self._sentence.split()
        
        if not all(word.isalpha() for word in list_words):
            raise ValueError("String must contain Words only")
        
        self._list_words = list_words
        self._counts = {}
        
    
    def count_word(self):
        """
        counts how many times each word is used
        stores it in a Dictionary '._counts'
        """
        for word in self._list_words:
            self._counts[word] = self._counts.get(word, 0) + 1
            
    def show_count(self):
        """
        print the word and its count
        """
        for word, count in self._counts.items():
            print(f"'{word}' is present {count} times")
        
    def __str__(self):
        return f"Sentence: {self._sentence}"
    
    def __repr__(self):
        return f"""
WordCounter('sentence': '{self._sentence}')
           'list_words': '{self._list_words}'
           'self._counts: '{self._counts}'
           
"""