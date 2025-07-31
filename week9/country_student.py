from student import Student

class CountryStudent(Student):
    def __init__(self, name, avg_grade, age, addition):
        super().__init__(name, avg_grade, age)
        self.addition = addition

    @property
    def addition(self):
        return self.__addition      # private attribute

    @addition.setter
    def addition(self, value):
        self.__addition = value

    # override str method
    def __str__(self):
        info = super().__str__() + f", Addition: {self.addition:.2f}"
        return info
    
    # override is_accepted method
    def is_accepted(self, accept_grade):
        return self.avg_grade + self.addition >= accept_grade