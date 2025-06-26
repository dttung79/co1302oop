from tkinter import *
from tkinter import messagebox as mb
from book import Book
class BookListGUI:
    def __init__(self):
        self.__create_window()
        self.__create_widgets()

    def __create_window(self):
        self.window = Tk()
        self.window.title("Book List")
        self.window.geometry("800x300")

    def __load_books(self):
        # create some sample books
        python = Book("Python Programming", "John Doe", 29.99)
        java = Book("Java Fundamentals", "Jane Smith", 39.99)
        csharp = Book("C# Basics", "Alice Johnson", 34.99)
        # assume csharp is borrowed
        csharp.borrow()
        # add books to the list
        self.books = [python, java, csharp]
        # insert books' titles into the listbox
        self.lst_books.delete(0, END)  # Clear the listbox
        for book in self.books:
            self.lst_books.insert(END, f"{book.title}")
    
    def __lst_books_select(self, event):
        # get the selected book index
        index = self.lst_books.curselection()[0]
        # get the selected book 
        book = self.books[index]
        # set the book details in the entry fields
        self.txt_title.delete(0, END)
        self.txt_title.insert(0, book.title)
        self.txt_author.delete(0, END)
        self.txt_author.insert(0, book.author)
        self.txt_price.delete(0, END)
        self.txt_price.insert(0, book.price)

        if book.status == True:
            self.available_var.set(1)
        else:
            self.available_var.set(0)

    def __create_widgets(self):
        self.lbl_list_books = Label(self.window, text="List of Books:")
        self.lbl_list_books.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        self.btn_load = Button(self.window, text="Load", command=self.__load_books)
        self.btn_load.grid(row=0, column=1, padx=5, pady=5, sticky=E)

        self.lst_books = Listbox(self.window, width=40, height=10, selectmode=SINGLE,               
                                                                        exportselection=False)
        self.lst_books.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, pady=5)
        # bind the select event to the listbox
        self.lst_books.bind('<<ListboxSelect>>', self.__lst_books_select)

        self.lbl_title = Label(self.window, text="Title:")
        self.lbl_title.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        self.txt_title = Entry(self.window, width=30)
        self.txt_title.grid(row=1, column=3, columnspan=2, padx=5, pady=5)

        self.lbl_author = Label(self.window, text="Author:")
        self.lbl_author.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        self.txt_author = Entry(self.window, width=30)
        self.txt_author.grid(row=2, column=3, columnspan=2, padx=5, pady=5)

        self.lbl_price = Label(self.window, text="Price:")
        self.lbl_price.grid(row=3, column=2, padx=5, pady=5, sticky=W)

        self.txt_price = Entry(self.window, width=30)
        self.txt_price.grid(row=3, column=3, columnspan=2, padx=5, pady=5)

        self.lbl_available = Label(self.window, text="Available:")
        self.lbl_available.grid(row=4, column=2, padx=5, pady=5, sticky=W)

        self.available_var = IntVar()
        self.available_var.set(1)

        self.rd_available = Radiobutton(self.window, text="Yes", variable=self.available_var, value=1)
        self.rd_available.grid(row=4, column=3, padx=5, pady=5, sticky=W)

        self.rd_unavailable = Radiobutton(self.window, text="No", variable=self.available_var, value=0)
        self.rd_unavailable.grid(row=4, column=4, padx=5, pady=5, sticky=W)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = BookListGUI()
    app.run()