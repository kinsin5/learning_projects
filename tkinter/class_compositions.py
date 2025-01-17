class BookShelf:
    def __init__(self, *books):
        self.books = books
    
    def __str__(self):
        return f"Bookshelf with {len(self.books)} books"
    
#bookshelf1 = BookShelf(100)
#print(bookshelf1)

class Book:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Book name: {self.name}"
    
book1 = Book("Hary")
book2 = Book("Poota")

shelf = BookShelf(book1, book2)

print(shelf)