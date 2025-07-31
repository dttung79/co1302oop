class Student:
    def __init__(self, name, avg_grade, age):
        self.name = name
        self.avg_grade = avg_grade
        self.age = age
    
    @property
    def name(self):
        return self._name   # protected attribute

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def avg_grade(self):
        return self._avg_grade  # protected attribute
    
    @avg_grade.setter
    def avg_grade(self, value):
        if not (0 <= value <= 10):
            raise ValueError("Average grade must be between 0 and 10")
        self._avg_grade = value

    @property
    def age(self):
        return self._age    # protected attribute
    
    @age.setter
    def age(self, value):
        if value < 18:
            raise ValueError("Age cannot be less than 18")
        self._age = value

    def __str__(self):
        info = f"Name: {self.name}, Average Grade: {self.avg_grade:.2f}, Age: {self.age}"
        return info
    
    def is_accepted(self, accept_grade):
        return self.avg_grade >= accept_grade