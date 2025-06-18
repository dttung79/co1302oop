from employee import Employee

class FullTime(Employee):
    def __init__(self, name, salary_rate, insurance):
        super().__init__(name, salary_rate)
        self.insurance = insurance

    @property
    def insurance(self):
        return self.__insurance
    
    @insurance.setter
    def insurance(self, new_insurance):
        if new_insurance <= 0:
            raise ValueError('Invalid insurance')
        
        self.__insurance = new_insurance

    @property
    def salary(self):
        return self.salary_rate * Employee._basic_salary
    
    # override __str__ method
    def __str__(self):
        employee_info = super().__str__()
        fulltime_info = employee_info + f', salary: ${self.salary}, insurance: ${self.insurance}'
        return fulltime_info
    
if __name__ == '__main__':
    john = FullTime('John', 2.0, 50)
    print(john)