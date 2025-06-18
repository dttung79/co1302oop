class Job:
    def __init__(self, name, man_month):
        self.name = name
        self.man_month = man_month
    
    # name property (get/set), check empty
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if new_name == '':
            raise ValueError('Error: Empty name')
        
        self.__name = new_name
    # man month property (get/set), check <= 0
    @property
    def man_month(self):
        return self.__man_month
    
    @man_month.setter
    def man_month(self, new_mm):
        if new_mm <= 0:
            raise ValueError('Error: Man month must > 0')
        
        self.__man_month = new_mm

    # __str__
    def __str__(self):
        return f'Job name: {self.name}, total {self.man_month} man month'
    

## Test Job class ###
if __name__ == '__main__':
    web_landing = Job('Landing Page', 0.5)
    print(web_landing)