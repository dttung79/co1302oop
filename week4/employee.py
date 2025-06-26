class Employee:
    # class attribute to keep track of the next employee ID
    _id_count = 0
    # class attribute to keep track of basic salary
    _basic_salary = 1000

    def __init__(self, name, salary_rate):
        # protected attributes
        self.__set_eid()        # call private method to set eid
        self.name = name                    # call setter method to set name
        self.salary_rate = salary_rate      # call setter method to set salary rate
    
    @property
    def eid(self):
        return self._eid
    
    # private method to set new employee id
    def __set_eid(self):
        #print(f'Current ID count: {Employee._id_count}')
        Employee._id_count += 1
        self._eid = Employee._id_count
        #print(f'This employee ID: {self._eid}')


    @property
    def name(self):
        return self._name       # protected attribute
    
    @name.setter
    def name(self, new_name):
        if new_name == '':
            raise ValueError('Error: Name cannot be empty!')
        
        self._name = new_name

    @property
    def salary_rate(self):
        return self._salary_rate
    
    @salary_rate.setter
    def salary_rate(self, new_rate):
        if new_rate <= 0 or new_rate > 10:
            raise ValueError('Error: Salary rate out of range!')
        
        self._salary_rate = new_rate

    @property
    def salary(self):
        return 0
    
    def __str__(self):
        return f'{self._eid}: {self._name}, rate: {self._salary_rate:.2f}'
    
## Test Employee class ##
if __name__ == "__main__":
    e1 = Employee('John', 2.0)
    e2 = Employee('Paul', 1.5)
    # e3 = Employee('', 1.1) <<-== Error because name is empty
    # e3 = Employee('Paul', 0) # Error
    # e3 = Employee('Paul', 10.1) # Error
    print(e1.name)
    print(e1.salary_rate)
    print(e1.eid)
    print(e2.eid)
    print(e1)   # call __str__ method
    print(e2)