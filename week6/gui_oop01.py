from tkinter import *
from tkinter import messagebox as mb

class MyWindow:
    def __init__(self):
        self.__create_window()
        self.__create_widgets()

    def __create_window(self):
        self.window = Tk()
        self.window.title("My Window")
        self.window.geometry("300x200")

    def __create_widgets(self):
        self.label = Label(self.window, text="Hello, World!")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.button = Button(self.window, text="Click Me", command=self.__btn_click)
        self.button.grid(row=1, column=0, padx=10, pady=10)

        self.txt_hello = Entry(self.window)
        self.txt_hello.grid(row=2, column=0, padx=10, pady=10)
    
    def __btn_click(self):
        mb.showinfo("Info", "Button clicked!")
        # get text from label
        label_text = self.label.cget("text")
        # set text to entry
        self.txt_hello.delete(0, END)
        self.txt_hello.insert(0, label_text)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = MyWindow()
    app.run()