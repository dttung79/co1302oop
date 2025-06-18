from employee import Employee

class PartTime(Employee):
    def __init__(self, name, salary_rate, week_hours):
        super().__init__(name, salary_rate)
        self.week_hours = week_hours

    @property
    def salary(self):
        return self.salary_rate * Employee._basic_salary * (self.week_hours / 40)
    
    @property
    def week_hours(self):
        return self.__week_hours
    
    @week_hours.setter
    def week_hours(self, new_hours):
        if new_hours < 10 or new_hours > 40:
            raise ValueError('Week hours out of range')
        
        self.__week_hours = new_hours
    
    # override _str__ method
    def __str__(self):
        empoyee_info = super().__str__()
        parttime_info = empoyee_info + f', salary: {self.salary}, hours of week: {self.week_hours}'
        return parttime_info
    
## Test PartTime ###
if __name__ == '__main__':
    john = PartTime('John', 2.0, 20)
    print(john)
    paul = PartTime('Paul', 2.0, 10)
    print(paul)