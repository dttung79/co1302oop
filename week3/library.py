from book import Book

class Library:
    def __init__(self):
        self.__books = []   # create an empty list of Book objects
    
    def add(self, new_book):
        self.__books.append(new_book)
        print(f'Book {new_book.title} added to library')
    
    def borrow(self, book):
        if not book.status:
            print(f'Book {book.title} is already borrowed')
            return
        
        # book is available
        book.borrow()
        print(f'Book {book.title} is borrowed success.')

    def get_back(self, book):
        if book.status == True:
            print(f'Book {book.title} is still in the library')
            return
        
        book.get_back()
        print(f'Book {book.title} is returned success.')
    
    def remove(self, old_book):
        self.__books.remove(old_book)
        print(f'Book {old_book.title} removed from library.')
    
    def show_books(self):
        print('All book in the library: ')
        for book in self.__books:
            book.display()

if __name__ == '__main__':
    python_book = Book('Python Programming', 'John Doe', 20)
    java_book = Book('Java Programming', 'John Doe', 18)
    csharp_book = Book('C# Programming', 'John Doe', 25)

    lib = Library()
    lib.add(python_book)
    lib.add(java_book)
    lib.add(csharp_book)

    lib.show_books()