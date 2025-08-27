class WordCounter:
    def __init__(self, sentence):
        if not isinstance(sentence, str):
            raise TypeError("Enter a String in Constructer")
        if sentence.isspace() or sentence.isnumeric():
            raise ValueError("String must contain words only")
        
        list_words = sentence.split()
        
        if not all(word.isalpha() for word in list_words):
            raise ValueError("String must contain words only")
        
        self.list_words = list_words
        
        
    def __str__(self):
        return f"Sentence: {self._sentence}"
    
    def __repr__(self):
        return f"WordCounter('Sentence': '{self._sentence}')"
    
    
x = WordCounter("123 is playing")

print(x)
print(repr(x))