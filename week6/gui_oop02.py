from tkinter import *
from tkinter import messagebox as mb

class GUIApp:
    def __init__(self):
        self.__create_window()
        self.__create_widgets()

    def __create_window(self):
        self.window = Tk()
        self.window.title("GUI Application")
        self.window.geometry("400x300")

    def __create_widgets(self):
        self.lbl_first_name = Label(self.window, text="First Name:")
        self.lbl_first_name.grid(row=0, column=0, padx=10, pady=10)

        self.txt_first_name = Entry(self.window)
        self.txt_first_name.grid(row=0, column=1, padx=10, pady=10)

        self.lbl_last_name = Label(self.window, text="Last Name:")
        self.lbl_last_name.grid(row=1, column=0, padx=10, pady=10)

        self.txt_last_name = Entry(self.window)
        self.txt_last_name.grid(row=1, column=1, padx=10, pady=10)

        self.btn_full_name = Button(self.window, text="Show Full Name", command=self.__btn_full_name_click)
        self.btn_full_name.grid(row=2, column=0, padx=10, pady=10)

        self.txt_full_name = Entry(self.window)
        self.txt_full_name.grid(row=2, column=1, padx=10, pady=10)

    def __btn_full_name_click(self):
        # get first name
        first_name = self.txt_first_name.get()
        # get last name
        last_name = self.txt_last_name.get()
        # set full name
        full_name = f"{first_name} {last_name}"
        self.txt_full_name.delete(0, END)
        self.txt_full_name.insert(0, full_name)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = GUIApp()
    app.run()