from base_gui import BaseGUI
from tkinter import *
from tkinter import messagebox as mb
from car import Car
from tkinter.filedialog import asksaveasfilename

class CarGUI(BaseGUI):
    def __init__(self, title='Add New Car', dimesion="400x300"):
        super().__init__("Add New Car", "400x300")

    # override the abstract method to create widgets
    def _create_widgets(self):
        lbl_title = Label(self._window, text="Add New Car")
        lbl_title.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=EW)

        lbl_brand = Label(self._window, text="Brand:")
        lbl_brand.grid(row=1, column=0, padx=5, pady=5, sticky=E)

        self.brand_var = StringVar()
        txt_brand = Entry(self._window, textvariable=self.brand_var)
        txt_brand.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        lbl_model = Label(self._window, text="Model:")
        lbl_model.grid(row=2, column=0, padx=5, pady=5, sticky=E)

        self.model_var = StringVar()
        txt_model = Entry(self._window, textvariable=self.model_var)
        txt_model.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        lbl_year = Label(self._window, text="Year:")
        lbl_year.grid(row=3, column=0, padx=5, pady=5, sticky=E)

        self.year_var = IntVar()
        txt_year = Entry(self._window, textvariable=self.year_var)
        txt_year.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        lbl_price = Label(self._window, text="Price:")
        lbl_price.grid(row=4, column=0, padx=5, pady=5, sticky=E)

        self.price_var = DoubleVar()
        txt_price = Entry(self._window, textvariable=self.price_var)
        txt_price.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        btn_submit = Button(self._window, text="Submit", command=self._btn_submit_click)
        btn_submit.grid(row=5, column=1, columnspan=2, padx=5, pady=5, sticky=E)

    def _btn_submit_click(self):
        brand = self.brand_var.get()
        model = self.model_var.get()
        year = self.year_var.get()
        price = self.price_var.get()

        try:
            car = Car(brand, model, year, price)
            f = asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if not f:
                mb.showwarning("Warning", "No file selected. Car not saved.")
                return
            with open(f, 'a') as file: # open with append mode
                file.write(f"\n{car.brand},{car.model},{car.year},{car.price}")

            mb.showinfo("Success", f"Car added successfully")
        except ValueError as e:
            mb.showerror("Error", f"Failed to add car: {e}")
        except Exception as e:
            mb.showerror("Error", f"An unexpected error occurred: {e}")

## Test the CarGUI
if __name__ == "__main__":
    app = CarGUI()
    app.run()