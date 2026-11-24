
# Name: Aaron Daniel Legayo
# Section: IV-BSIT
# Activity: P7 - Student Management System with Classes
# Date: November 24, 2026


class Student:
    def __init__(self, student_id, name, course, grade):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.__grade = None
        self.set_grade(grade)

    # Getter method for the private grade attribute.
    def get_grade(self):
        return self.__grade

    # Setter method that validates the grade.
    def set_grade(self, grade):
        if not isinstance(grade, (int, float)) or isinstance(grade, bool):
            raise ValueError("Grade must be a number.")

        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100.")

        self.__grade = grade

    def update_information(self, name, course):
        self.name = name
        self.course = course

    def display_information(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"General Average: {self.get_grade()}")
        print("--------------------------------")


class Subject:
    def __init__(self, subject_code, subject_name):
        self.subject_code = subject_code
        self.subject_name = subject_name

    def display_subject(self):
        print(f"{self.subject_code} - {self.subject_name}")


class Section:
    def __init__(self, section_name):
        self.section_name = section_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        print(f"\nSECTION: {self.section_name}")
        print("================================")

        if not self.students:
            print("No students registered.")
            return

        for student in self.students:
            student.display_information()

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None


def main():
    print("STUDENT MANAGEMENT SYSTEM")
    print("Prepared by: Aaron Daniel Legayo")
    print("================================")

    # Create three student objects.
    student1 = Student("2024-001", "Adrian Manangan", "BSIT", 90)
    student2 = Student("2024-002", "Rhamsus Cagampan", "BSIT", 92)
    student3 = Student("2024-003", "Kevin Vila", "BSIT", 88)

    # Create a section and add the student objects.
    section = Section("IV-BSIT")
    section.add_student(student1)
    section.add_student(student2)
    section.add_student(student3)

    # Create a subject object.
    subject = Subject("IT401", "Object-Oriented Programming")

    print("\nSUBJECT INFORMATION")
    subject.display_subject()

    # Display all students before updating.
    print("\nSTUDENT LIST BEFORE UPDATE")
    section.display_students()

    # Update Adrian Manangan's information.
    print("\nUPDATING STUDENT INFORMATION")
    student_to_update = section.find_student("2024-001")

    if student_to_update:
        student_to_update.update_information(
            "Adrian Manangan", "BSIT - Section IV-B"
        )
        student_to_update.set_grade(95)
        print("Adrian Manangan's information successfully updated.")

    # Display all students after updating.
    print("\nSTUDENT LIST AFTER UPDATE")
    section.display_students()


if __name__ == "__main__":
    main()
