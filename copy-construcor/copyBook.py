class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def copy(self, other):
        self.title = other.title
        self.author = other.author
        
book1 = Book("History", "Nigel Kelly")
book2 = Book(" ", " ")

book2.copy(book1)

print(book1.title,book1.author)
print(book2.title,book2.author)