class Book:
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price = price
        self.__status = True

    @property
    def status(self):
        return self.__status
    
    def borrow(self):
        self.__status = False
    
    def get_back(self):
        self.__status = True
    
    @property
    def title(self):
        return self.__title
    
    @property
    def author(self):
        return self.__author
    
    @property 
    def price(self):
        return self.__price

    @title.setter
    def title(self, new_title):
        if new_title == '':
            print('Invalid title!')
            return
        
        self.__title = new_title
    
    @author.setter
    def author(self, new_author):
        if new_author == '':
            print('Invalid author')
            return

        self.__author = new_author

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('Invalid price')
            return
        
        self.__price = new_price

    
    def display(self):
        print(f'Title: {self.__title}, author: {self.__author}, price: ${self.__price}')