from book import Book
from library import Library

class LibraryManager:
    def __init__(self):
        lib = Library()
        self.load_books()
    
    def load_books(self):
        python_book = Book('Python Programming', 'John Doe', 20)
        java_book = Book('Java Programming', 'John Doe', 18)
        csharp_book = Book('C# Programming', 'John Doe', 25)

        self.lib = Library()
        self.lib.add(python_book)
        self.lib.add(java_book)
        self.lib.add(csharp_book)
    
    def run(self):
        running = True
        while running:
            self.print_menu()
            choice = int(input('Enter your choice: '))
            if choice == 1:
                self.add_book()
            elif choice == 2:
                self.borrow_book()
            elif choice == 3:
                self.return_book()
            elif choice == 4:
                self.remove_book()
            elif choice == 5:
                self.display_books()
            elif choice == 6:
                running = False
                print('Exit')
            else:
                print('Invalid choice')
    
    def print_menu(self):
        print('1. Add book.')
        print('2. Borrow book.')
        print('3. Return book.')
        print('4. Remove book.')
        print('5. Show all books.')
        print('6. Exit.')
    
    def add_book(self):
        pass

    def borrow_book(self):
        pass

    def return_book(self):
        pass

    def remove_book(self):
        pass

    def display_books(self):
        self.lib.show_books()

lib_program = LibraryManager()
lib_program.run()