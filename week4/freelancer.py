from employee import Employee
from job import Job

class Freelancer(Employee):
    def __init__(self, name, salary_rate, job):
        super().__init__(name, salary_rate)
        self.job = job

    @property
    def job(self):
        return self.__job
    
    @job.setter
    def job(self, new_job):
        self.__job = new_job

    @property
    def salary(self):
        return self.salary_rate * Employee._basic_salary * self.job.man_month
    
    def __str__(self):
        employee_info = super().__str__()
        freelancer_info = employee_info + f', salary: ${self.salary}'
        freelancer_info += '\n'
        freelancer_info += 'Working on ' + str(self.job)

        return freelancer_info
    
### Test Freelancer
if __name__ == '__main__':
    landing_web = Job('Landing Page', 0.5)
    john = Freelancer('John', 2.0, landing_web)

    mobile_app = Job('Mobile App', 2.5)
    paul = Freelancer('Paul', 1.5, mobile_app)

    print(john)
    print(paul)