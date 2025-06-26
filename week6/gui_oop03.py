from tkinter import *
from tkinter import messagebox as mb

class DemoApp:
    def __init__(self):
        self.__create_window()
        self.__create_widgets()

    def __create_window(self):
        self.window = Tk()
        self.window.title("Demo Application")
        self.window.geometry("400x300")

    def __create_widgets(self):
        self.lbl_nights = Label(self.window, text="Nights:")
        self.lbl_nights.grid(row=0, column=0, padx=5, pady=5, sticky=E)

        self.txt_nights = Entry(self.window)
        self.txt_nights.grid(row=0, column=1, padx=5, pady=5, columnspan=2, sticky=W)

        self.lbl_price = Label(self.window, text="Price:")
        self.lbl_price.grid(row=1, column=0, padx=5, pady=5, sticky=E)

        self.txt_price = Entry(self.window)
        self.txt_price.grid(row=1, column=1, padx=5, pady=5, columnspan=2, sticky=W)

        self.lbl_weekend = Label(self.window, text="Weekend:")
        self.lbl_weekend.grid(row=2, column=0, padx=5, pady=5, sticky=E)

        self.rd_yes = Radiobutton(self.window, text="Yes", value=1)
        self.rd_yes.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        self.rd_no = Radiobutton(self.window, text="No", value=0)
        self.rd_no.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        self.lbl_extra = Label(self.window, text="Extra:")
        self.lbl_extra.grid(row=3, column=0, padx=5, pady=5, sticky=E)

        self.chk_breakfast = Checkbutton(self.window, text="Breakfast")
        self.chk_breakfast.grid(row=3, column=1, padx=5, pady=5, sticky=W, columnspan=2)

        self.chk_airport = Checkbutton(self.window, text="Airport Transfer")
        self.chk_airport.grid(row=4, column=1, padx=5, pady=5, sticky=W, columnspan=2)

        self.btn_calculate = Button(self.window, text="Calculate")
        self.btn_calculate.grid(row=5, column=1, padx=5, pady=5, sticky=W, columnspan=2)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = DemoApp()
    app.run()