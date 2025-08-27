class WordCounter:
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
        self.counts = {}
        
    
    def count_word(self):
        for word in self._list_words:
            self.counts[word] = self.counts.get(word, 0) + 1
        
    def __str__(self):
        return f"Sentence: {self._sentence}"
    
    def __repr__(self):
        return f"WordCounter('Sentence': '{self._sentence}')"
    
    
x = WordCounter("123 is playing")

print(x)
print(repr(x))