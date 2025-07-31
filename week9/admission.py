from student import Student

class Admission:
    def __init__(self, name):
        self.name = name     # admission name
        self.__students = []   # list of students that this admission has
    
    @property
    def name(self):
        return self.__name  # private attribute

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Admission name cannot be empty")
        self.__name = value

    def add_student(self, s):
        self.__students.append(s)  # add student to the list

    def show_all(self):
        for s in self.__students:
            print(s)

    def inform(self, student, accept_grade):
        print(f"Hi, I am {self.name} from the admission office.")
        if student.is_accepted(accept_grade):
            print("I am happy to inform you that you have been accepted!")
        else:
            print("I am sorry to inform you that you have not been accepted.")