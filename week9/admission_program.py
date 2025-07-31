from student import Student
from country_student import CountryStudent
from admission import Admission

class AdmissionProgram:
    def __init__(self):
        name = input("Enter the name of the admission: ")
        self.admission = Admission(name)
        self.accept_grade = float(input("Enter the acceptance grade: "))
    
    def run(self):
        running = True

        while running:
            self.__print_menu()
            choice = input("Enter your choice: ")
            if   choice == '1': self.__add_student()
            elif choice == '2': self.__show_all()
            elif choice == '3': self.__inform()
            elif choice == '4': running = False
            else: print("Invalid choice, please try again.")

    def __print_menu(self):
        print("\n--- Admission Program Menu ---")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Inform Student")
        print("4. Exit")

    def __add_student(self):
        print("Choose student type:")
        print("1. Regular Student")
        print("2. Country Student")
        choice = input("Enter your choice: ")
        name = input("Enter student's name: ")
        avg_grade = float(input("Enter student's average grade: "))
        age = int(input("Enter student's age: "))
        if choice == '1':
            student = Student(name, avg_grade, age)
        elif choice == '2':
            addition = float(input("Enter country student addition: "))
            student = CountryStudent(name, avg_grade, age, addition)
        else:
            print("Invalid choice, returning to menu.")
            return
        self.admission.add_student(student)

    def __show_all(self):
        print("\n--- List of Students ---")
        self.admission.show_all()

    def __inform(self):
        index = int(input("Enter the index of the student to inform (0-based): "))
        student = self.admission.get_student(index)
        self.admission.inform(student, self.accept_grade)

if __name__ == "__main__":
    program = AdmissionProgram()
    program.run()