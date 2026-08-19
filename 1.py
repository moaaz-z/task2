class book:
    def __init__(self,title,author,available):
        self.title=title
        self.author=author
        self.available=available

class library:
    def __init__(self,books,borrowed_books):
        self.books=books
        self.borrowed_books=borrowed_books
    def show_books(self):
     for book in self.books:
        if(book.available):
            print(book.title)
    def borrow_book(self):
       self.show_books()
       book_name=input("Enter The Book You Want To Borrow:");
       for book in self.books:
                if(book.title==book_name and book.available):
                    self.borrowed_books.append(book)
                    book.available=False
       

book1 = book("The Hobbit", "J.R.R. Tolkien", True)
book2 = book("1984", "George Orwell", True)
book3 = book("Harry Potter", "J.K. Rowling", True)
book4 = book("The Alchemist", "Paulo Coelho", True)
book5 = book("Clean Code", "Robert C. Martin", True)

books = [book1, book2, book3, book4, book5]

borrowed_books = []

library = library(books, borrowed_books)
library.show_books()
        
