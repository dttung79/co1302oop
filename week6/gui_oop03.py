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

        self.weekend_var = IntVar()
        self.weekend_var.set(0)
        self.rd_yes = Radiobutton(self.window, text="Yes", variable=self.weekend_var, value=1)
        self.rd_yes.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        self.rd_no = Radiobutton(self.window, text="No", variable=self.weekend_var, value=0)
        self.rd_no.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        self.lbl_extra = Label(self.window, text="Extra:")
        self.lbl_extra.grid(row=3, column=0, padx=5, pady=5, sticky=E)

        self.breakfast_var = BooleanVar()
        self.breakfast_var.set(False)
        self.chk_breakfast = Checkbutton(self.window, text="Breakfast", variable=self.breakfast_var)
        self.chk_breakfast.grid(row=3, column=1, padx=5, pady=5, sticky=W, columnspan=2)

        self.airport_var = BooleanVar()
        self.airport_var.set(False)
        self.chk_airport = Checkbutton(self.window, text="Airport Transfer", variable=self.airport_var)
        self.chk_airport.grid(row=4, column=1, padx=5, pady=5, sticky=W, columnspan=2)

        self.btn_calculate = Button(self.window, text="Calculate", command=self.__btn_calculate_click)
        self.btn_calculate.grid(row=5, column=1, padx=5, pady=5, sticky=W, columnspan=2)
    
    def __btn_calculate_click(self):
        try:
            nights = int(self.txt_nights.get())
            price = float(self.txt_price.get())
        except ValueError:
            mb.showerror("Input Error", "Please enter valid numbers for nights and price.")
            return
        
        total = nights * price

        weekend = self.weekend_var.get() # return 1 if Yes, 0 if No
        if weekend == 1:
            total *= 1.2  # 20% increase for weekends
        
        breakfast = self.breakfast_var.get()  # return True if checked, False if not
        if breakfast:
            total += 5 * nights  # Add $5 for breakfast each night
    
        airport = self.airport_var.get()    # return True if checked, False if not
        if airport:
            total += 15  # Add $15 for airport transfer
        
        bill = f'Your total bill is: ${total:.2f}'
        mb.showinfo("Bill Summary", bill)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = DemoApp()
    app.run()