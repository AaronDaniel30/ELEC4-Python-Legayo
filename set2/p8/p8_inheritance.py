
# Name: Aaron Daniel Legayo
# Section: IV-BSIT
# Activity: P8 - Inheritance and Polymorphism
# Date: November 24, 2026

# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


# Student class inherits from Person
class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    # Override the introduce method
    def introduce(self):
        print(
            f"I am {self.name}, a {self.age}-year-old student. "
            f"My student ID is {self.student_id} and I take {self.course}."
        )


# Teacher class inherits from Person
class Teacher(Person):
    def __init__(self, name, age, subject, years_experience):
        super().__init__(name, age)
        self.subject = subject
        self.years_experience = years_experience

    # Override the introduce method
    def introduce(self):
        print(
            f"I am {self.name}, a {self.age}-year-old teacher. "
            f"I teach {self.subject} and have {self.years_experience} years of experience."
        )


# Create objects from different classes
people = [
    Student("Aaron Daniel Legayo", 21, "2025-001", "BSIT"),
    Student("Adrian Manangan", 22, "2026-002", "BSIT"),
    Teacher("Rhamsus Cagampan", 22, "Programming", 10)
]


# Demonstrate polymorphism
print("INHERITANCE AND POLYMORPHISM")
print("Prepared by: Aaron Daniel Legayo")
print("=" * 45)

for person in people:
    person.introduce()
    print("-" * 45)


# Explanation:
# Inheritance allows the Student and Teacher classes to reuse the
# attributes and methods of the Person parent class.
# The super() function calls the constructor of the parent class.
# Polymorphism is demonstrated by placing different objects in one list
# and calling their overridden introduce() methods using the same loop.
