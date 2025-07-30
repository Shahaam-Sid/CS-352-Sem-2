class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __eq__(self, other):
        return self.pages == other.pages

    def __lt__(self, other):
        return self.pages < other.pages
    
    def __gt__(self, other):
        return self.pages > other.pages
    
    def __add__(self, other):
        return self.pages + other.pages 
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "Title":
            return self.title
        else:
            return f"{key} was not found"
            
book1 = Book("The Alchemsit", "Poelo Coelho", 390)
book2 = Book("Harry Potter", "J.K. Rowling", 390)
book3 = Book("A Tale of Two Cities", "Charles Dickens", 760)


print(book1)
print(book2)
print(book3)

print(repr(book1))
print(repr(book2))
print(repr(book3))

print(book1 == book2)
print(book1 < book3)
print(book3 > book2)

print(book1 + book2)

print("Tale" in book3)