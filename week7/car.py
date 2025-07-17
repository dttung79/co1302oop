class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str) or value == "":
            raise ValueError("Brand must be string and cannot be empty.")
        self.__brand = value

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        if not isinstance(value, str) or value == "":
            raise ValueError("Model must be string and cannot be empty.")
        self.__model = value

    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Year must be a positive integer.")
        self.__year = value

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Price must be a positive number.")
        self.__price = value